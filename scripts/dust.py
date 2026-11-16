#!/usr/bin/env python3
# Among addresses involved in real USDC dust transfers in the last N blocks, collect those delegated to Poisoner. 2026-11-15
import json,subprocess,sys,time
N=int(sys.argv[1]); RPC='https://ethereum-rpc.publicnode.com'
USDC='0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'; T='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
POI='ef0100e6b97aa1490c93c28a14d86c13c9dc9c950643ed'
def rpc(p):
    for k in range(5):
        out=subprocess.run(['curl','-s','-m','40','-A','Mozilla/5.0',RPC,'-H','content-type: application/json','-d',json.dumps(p)],capture_output=True,text=True).stdout
        try:
            d=json.loads(out)
            if isinstance(d,list) or 'result' in d: return d
        except Exception: pass
        time.sleep(2)
    raise SystemExit('rpc fail '+out[:200])
head=int(rpc({'jsonrpc':'2.0','id':1,'method':'eth_blockNumber','params':[]})['result'],16)
cand=set(); nlogs=0; ndust=0
for a in range(head-N+1,head+1,10):
    logs=rpc({'jsonrpc':'2.0','id':1,'method':'eth_getLogs','params':[{'address':USDC,'topics':[T],'fromBlock':hex(a),'toBlock':hex(min(a+9,head))}]})['result']
    nlogs+=len(logs)
    for l in logs:
        if l['data']!='0x' and int(l['data'],16)<=1000:
            ndust+=1; cand.add('0x'+l['topics'][1][26:]); cand.add('0x'+l['topics'][2][26:])
print('head',head,'logs',nlogs,'dust transfers',ndust,'candidates',len(cand),flush=True)
cand=sorted(cand); poison=[]; other={}
for i in range(0,len(cand),50):
    res=rpc([{'jsonrpc':'2.0','id':j,'method':'eth_getCode','params':[x,'latest']} for j,x in enumerate(cand[i:i+50])])
    for r in res:
        c=(r.get('result') or '').lower(); x=cand[i+r['id']]
        if c[2:]==POI: poison.append(x)
        elif c.startswith('0xef0100'): other['0x'+c[8:]]=other.get('0x'+c[8:],0)+1
    time.sleep(0.2)
print('poisoner-delegated',len(poison)); print('other delegates among dust addrs',sorted(other.items(),key=lambda x:-x[1])[:8])
json.dump({'head':head,'N':N,'logs':nlogs,'dust':ndust,'candidates':len(cand),'poison':poison,'other':other},open('dust-%d.json'%head,'w'),indent=1)
