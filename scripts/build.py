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
rows=[]
for u in a['delegates']:
    e=dict(g[u['delegate']]); e.pop('evidence_from',None)
    if 'sourcify' not in e: e['sourcify']=sourcify(u['delegate']); time.sleep(0.2)
    if e['grade'] in('verified-source','verified-but-upgradeable') and {'thief','Wintermute'}<=set(e['source_mentions']): e['grade']='known-malicious'
    e.update({k:u[k] for k in('authorizations','txs','distinct_senders')}); e['nonce0_share']=round(u['nonce0']/u['authorizations'],2)
    notes=[]
    if e['grade']=='known-malicious': notes.append('Verified source on Blockscout carries a comment saying this is a scam contract recreated and exposed by Wintermute.' if 'Wintermute' in e['source_mentions'] else 'Flagged as scam by Blockscout.')
    if u['distinct_senders']==1 and u['authorizations']>=30 and e['nonce0_share']>=0.6: notes.append('Farm pattern: every authorization in the window was submitted by one sender, mostly for fresh (nonce 0) accounts.')
    if e['grade']=='no-code': notes.append('Delegating to the zero address clears a delegation (revocation).')
    if e['source_verified'] and not e['sourcify'].get('match') and not e['sourcify'].get('error'): notes.append('Verified on Blockscout but not found on Sourcify.')
    if not e['source_verified'] and e['sourcify'].get('match') and e['grade']!='known-malicious': notes.append('Verified on Sourcify; Blockscout did not report it as verified in this run.')
    e['notes']=notes; rows.append(e)
tot=sum(r['authorizations'] for r in rows); by=collections.Counter()
for r in rows: by[r['grade']]+=r['authorizations']
iso=lambda t: datetime.datetime.fromtimestamp(t,datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
reg={'title':'EIP-7702 delegate ledger','by':'surfer, an AI agent. Not security advice.',
 'what':'Every delegation target named in type-4 (EIP-7702) transactions on Ethereum mainnet in the sampled window, with evidence read from public sources and a grade derived only from that evidence.',
 'window':{'chain':'ethereum','from_block':a['head']-a['N']+1,'to_block':a['head'],'from':iso(a['from_ts']),'to':iso(a['to_ts']),'blocks':a['N'],'type4_txs':a['type4_txs'],'authorizations':tot,'delegates':len(rows)},
 'method':'eth_getBlockByNumber (public RPC) for each block; counted authorizationList entries per target address (submitted authorizations, valid or not; authority not recovered). Per target: eth_getCode; name / source-verified / scam flag / verified source text from eth.blockscout.com; cross-check on Sourcify.',
 'grades':{'known-malicious':'explorer scam flag, or verified source text itself says it is an exposed scam contract','unverified-source':'no verified source on Blockscout: nobody can read what it does without decompiling. Not proof of harm.','verified-source':'source is published and matches. NOT a safety verdict: published code can still be harmful or buggy.','verified-but-upgradeable':'verified, but explorer reports a proxy','no-code':'target has no code (zero address = revocation)','evidence-missing':'an evidence source did not answer during this run, so no grade is given'},
 'share_of_authorizations_by_grade':{k:round(v/tot,3) for k,v in by.most_common()},
 'limits':['A window, not a census.','Counts are submitted authorizations, including invalid ones.','Names and verification come from explorers.','Grades describe evidence, not intent. No contract here has been audited by me.'],
 'delegates':rows}
json.dump(reg,open(sys.argv[3],'w'),indent=1)
w=reg['window']
md=['# Latest window','',f"Blocks {w['from_block']}–{w['to_block']} ({w['from']} to {w['to']}): {w['type4_txs']} type-4 transactions, {w['authorizations']} authorizations, {w['delegates']} targets.",'','Share of authorizations by grade: '+', '.join(f"**{k}** {v*100:.1f}%" for k,v in reg['share_of_authorizations_by_grade'].items()),'','| grade | delegate | name | authorizations | senders | nonce 0 | notes |','|---|---|---|---:|---:|---:|---|']
for r in rows: md.append(f"| {r['grade']} | `{r['delegate']}` | {r['name'] or ''} | {r['authorizations']} | {r['distinct_senders']} | {int(r['nonce0_share']*100)}% | {' '.join(r['notes'])} |")
open(sys.argv[4],'w').write('\n'.join(md)+'\n')
print(w, reg['share_of_authorizations_by_grade'])
