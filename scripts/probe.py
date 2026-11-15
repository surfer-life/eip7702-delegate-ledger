#!/usr/bin/env python3
# Dry-run probe: what happens to 1 wei sent to an account delegated to each target?
# Uses eth_simulateV1 with traceTransfers (nothing is sent on-chain). usage: probe.py auths.json out.json [max_targets]
import json,subprocess,sys,time,collections,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from authority import authority
RPCS=['https://ethereum-rpc.publicnode.com','https://eth.drpc.org']
FROM='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'   # any address with a large balance works as the pretend sender
def rpc(m,p):
    for k in range(4):
        url=RPCS[k%len(RPCS)]
        try:
            j=json.loads(subprocess.run(['curl','-s','-m','40','-A','Mozilla/5.0',url,'-H','content-type: application/json','-d',json.dumps({'jsonrpc':'2.0','id':1,'method':m,'params':p})],capture_output=True,text=True).stdout)
            if 'result' in j: return j['result']
        except Exception: pass
        time.sleep(2+2*k)
    return None
def probe(account):
    r=rpc('eth_simulateV1',[{'blockStateCalls':[{'calls':[{'from':FROM,'to':account,'value':'0x1'}]}],'traceTransfers':True,'validation':False},'latest'])
    if not r: return None
    c=r[0]['calls'][0]; out=[]
    for l in c.get('logs',[]):
        if l['address'].lower()=='0x'+'e'*40 and len(l['topics'])>=3:
            f='0x'+l['topics'][1][-40:]; t='0x'+l['topics'][2][-40:]
            if f==account.lower() and t!=account.lower(): out.append(t)
    return {'ok':c.get('status')=='0x1','gas':int(c.get('gasUsed','0x0'),16),'sent_on_to':out}
if __name__=='__main__':
    A=json.load(open(sys.argv[1])); res={}; lim=int(sys.argv[3]) if len(sys.argv)>3 else 10**9
    for u in A['delegates'][:lim]:
        d=u['delegate']
        if int(d,16)==0 or not u.get('samples'): continue
        accs=[]
        for s in u['samples']:
            try: a=authority(s)
            except Exception: a=None
            if a and a not in accs: accs.append(a)
        probed=0; fwd=0; dest=collections.Counter(); reverted=0
        for acc in accs:
            if probed>=3: break
            code=(rpc('eth_getCode',[acc,'latest']) or '').lower()
            if code!='0xef0100'+d[2:]: continue          # no longer delegated to this target
            p=probe(acc); time.sleep(0.2)
            if p is None: continue
            probed+=1
            if not p['ok']: reverted+=1
            if p['sent_on_to']:
                fwd+=1
                for t in p['sent_on_to']: dest[t]+=1
        res[d]={'accounts_sampled':len(accs),'accounts_probed':probed,'forwarded':fwd,'reverted':reverted,'destinations':dict(dest)}
        if fwd: print('forwards',d,res[d],flush=True)
    json.dump(res,open(sys.argv[2],'w'),indent=1)
    print('probed targets',sum(1 for v in res.values() if v['accounts_probed']),'forwarding',sum(1 for v in res.values() if v['forwarded']))
