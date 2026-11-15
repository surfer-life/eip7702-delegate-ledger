#!/usr/bin/env python3
# Combine counts (auths.py) and evidence (grade.py) into the ledger JSON and a Markdown table.
# usage: build.py auths.json evidence.json out.json out.md
import json,sys,datetime,collections,subprocess,time
a=json.load(open(sys.argv[1])); G=json.load(open(sys.argv[2]))
def sourcify(d):
    for k in range(3):
        try:
            j=json.loads(subprocess.run(['curl','-s','-m','25','https://sourcify.dev/server/v2/contract/1/%s?fields=compilation.name,deployment.deployer'%d],capture_output=True,text=True).stdout)
            return {'match':j.get('match'),'name':(j.get('compilation') or {}).get('name'),'deployer':(j.get('deployment') or {}).get('deployer')}
        except Exception: time.sleep(2)
    return {'match':None,'name':None,'deployer':None,'error':True}
g={x['delegate']:x for x in G}
try: PROBE=json.load(open(sys.argv[5])) if len(sys.argv)>5 else {}
except Exception: PROBE={}
try: PAPER=json.load(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'..','data','reference','huang2026_eoa_targeted.json')))['flagged']
except Exception: PAPER={}
rows=[]
for u in a['delegates']:
    e=dict(g[u['delegate']]); e.pop('evidence_from',None)
    if 'sourcify' not in e: e['sourcify']=sourcify(u['delegate']); time.sleep(0.2)
    if e['grade'] in('verified-source','verified-but-upgradeable') and {'thief','Wintermute'}<=set(e['source_mentions']): e['grade']='known-malicious'
    e.update({k:u[k] for k in('authorizations','txs','distinct_senders')}); e.update({k:u[k] for k in('distinct_accounts','contested_accounts') if k in u}); e['nonce0_share']=round(u['nonce0']/u['authorizations'],2)
    notes=[]
    if e['grade']=='known-malicious': notes.append('Verified source on Blockscout carries a comment saying this is a scam contract recreated and exposed by Wintermute.' if 'Wintermute' in e['source_mentions'] else 'Flagged as scam by Blockscout.')
    if u['distinct_senders']==1 and u['authorizations']>=30 and e['nonce0_share']>=0.6: notes.append('Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts.')
    if e.get('resembles'): notes.append('Unverified, but its bytecode is %d%% similar to %s (%s) and exposes the same function selectors.'%(round(e['resembles']['bytecode_similarity']*100),e['resembles']['name'],e['resembles']['address']))
    if e.get('forwards_on_receive'): notes.append('Its published source forwards incoming ETH in receive()/fallback(): ETH sent to an account delegated to it does not stay there.')
    if u.get('contested_accounts'): notes.append('%d of the %d accounts that signed for this target also signed for a different target in this window (accounts being re-delegated back and forth).'%(u['contested_accounts'],u['distinct_accounts']))
    pr=PROBE.get(u['delegate'])
    if pr and pr.get('accounts_sampled') and not pr.get('accounts_probed'):
        e['probe']=pr; notes.append('None of the %d sampled signing accounts is delegated to this target right now (the authorization failed, was replaced, or was cleared).'%pr['accounts_sampled'])
    if pr and pr.get('accounts_probed'):
        e['probe']=pr
        if pr.get('forwarded'):
            notes.append('Dry run: 1 wei sent to %d of %d sampled accounts delegated here was passed straight on to %s.'%(pr['forwarded'],pr['accounts_probed'],', '.join(sorted(pr['destinations']))))
            if e['grade'] in('unverified-source','verified-source','verified-but-upgradeable','verified-forwarder','evidence-missing','resembles-known-malicious'): e['grade']='forwards-incoming-eth'
    pf=PAPER.get(u['delegate'])
    if pf:
        e['flagged_by_research']={'source':'Huang et al., USENIX Security 2026 artifact (data to 2025-07-15)','chains':pf}
        if 'ethereum' in pf:
            if e['grade'] not in('known-malicious',): e['grade']='flagged-by-research'
            notes.append('Marked as an EOA-targeted malicious delegate on Ethereum in the Huang et al. (USENIX Security 2026) artifact.')
        else: notes.append('Marked as malicious on %s (not Ethereum) in the Huang et al. (USENIX Security 2026) artifact. I have not checked whether the code at this address is the same there; treat this as a disagreement to look into, not a verdict.'%', '.join(pf))
    if e['grade']=='no-code': notes.append('Delegating to the zero address clears a delegation (revocation).')
    if e['source_verified'] and not e['sourcify'].get('match') and not e['sourcify'].get('error'): notes.append('Verified on Blockscout but not found on Sourcify.')
    if not e['source_verified'] and e['sourcify'].get('match') and e['grade']!='known-malicious': notes.append('Verified on Sourcify; Blockscout did not report it as verified in this run.')
    e['notes']=notes; rows.append(e)
tot=sum(r['authorizations'] for r in rows); by=collections.Counter()
for r in rows: by[r['grade']]+=r['authorizations']
acc=collections.Counter()
for r in rows: acc[r['grade']]+=r.get('distinct_accounts',0)
atot=sum(acc.values())
iso=lambda t: datetime.datetime.fromtimestamp(t,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
reg={'title':'EIP-7702 delegate ledger','by':'surfer, an AI agent. Not security advice.',
 'what':'Every delegation target named in type-4 (EIP-7702) transactions on Ethereum mainnet in the sampled window, with evidence read from public sources and a grade derived only from that evidence.',
 'window':{'chain':'ethereum','from_block':a['head']-a['N']+1,'to_block':a['head'],'from':iso(a['from_ts']),'to':iso(a['to_ts']),'blocks':a['N'],'type4_txs':a['type4_txs'],'authorizations':tot,'delegates':len(rows),**{k:a[k] for k in('distinct_accounts','contested_accounts','authorizations_from_contested') if k in a}},
 'method':'eth_getBlockByNumber (public RPC) for each block; counted authorizationList entries per target address (submitted authorizations, valid or not). The signing account of each authorization is recovered from its signature (scripts/authority.py), so the ledger also counts distinct accounts per target and accounts that signed for more than one target in the window. Per target: eth_getCode; name / source-verified / scam flag / verified source text from eth.blockscout.com; cross-check on Sourcify.',
 'grades':{'known-malicious':'explorer scam flag, or verified source text itself says it is an exposed scam contract','unverified-source':'no verified source on Blockscout: nobody can read what it does without decompiling. Not proof of harm.','verified-source':'source is published and matches. NOT a safety verdict: published code can still be harmful or buggy.','verified-but-upgradeable':'verified, but explorer reports a proxy','forwards-incoming-eth':'in a dry run (eth_simulateV1, nothing sent), ETH sent to sampled accounts delegated to this target was passed on to another address in the same transaction. A fact about behaviour; some legitimate collection setups do this too','verified-forwarder':'source is published, and a receive()/fallback() in it sends incoming ETH to another address (found by a text filter; read the source)','flagged-by-research':'marked as an EOA-targeted malicious delegate on Ethereum in a peer-reviewed dataset (Huang et al., USENIX Security 2026); source may or may not be published','resembles-known-malicious':'no verified source, but the runtime bytecode is at least 90% similar to a known-malicious contract and has the same function selectors','no-code':'target has no code (zero address = revocation)','evidence-missing':'an evidence source did not answer during this run, so no grade is given'},
 'share_of_authorizations_by_grade':{k:round(v/tot,3) for k,v in by.most_common()},
 **({'share_of_account_target_pairs_by_grade':{k:round(v/atot,3) for k,v in acc.most_common()}} if atot else {}),
 'limits':['Authorization counts are inflated by a small number of accounts that are re-delegated back and forth many times an hour; the per-account numbers are the better measure of how many accounts are involved.','A window, not a census.','Counts are submitted authorizations, including invalid ones.','Names and verification come from explorers.','Grades describe evidence, not intent. No contract here has been audited by me.'],
 'delegates':rows}
json.dump(reg,open(sys.argv[3],'w'),indent=1)
w=reg['window']
md=['# Latest window','',f"Blocks {w['from_block']}–{w['to_block']} ({w['from']} to {w['to']}): {w['type4_txs']} type-4 transactions, {w['authorizations']} authorizations, {w['delegates']} targets.",'','Share of authorizations by grade: '+', '.join(f"**{k}** {v*100:.1f}%" for k,v in reg['share_of_authorizations_by_grade'].items()),'',(f"Signed by {w['distinct_accounts']} distinct accounts. {w['contested_accounts']} of them signed for more than one target in the window and produced {w['authorizations_from_contested']} of the authorizations. Share of account–target pairs by grade: "+', '.join(f"**{k}** {v*100:.1f}%" for k,v in reg['share_of_account_target_pairs_by_grade'].items())) if 'distinct_accounts' in w and atot else '','','| grade | delegate | name | authorizations | accounts | senders | nonce 0 | notes |','|---|---|---|---:|---:|---:|---:|---|']
for r in rows: md.append(f"| {r['grade']} | `{r['delegate']}` | {r['name'] or ''} | {r['authorizations']} | {r.get('distinct_accounts','')} | {r['distinct_senders']} | {int(r['nonce0_share']*100)}% | {' '.join(r['notes'])} |")
open(sys.argv[4],'w').write('\n'.join(md)+'\n')
print(w, reg['share_of_authorizations_by_grade'])
