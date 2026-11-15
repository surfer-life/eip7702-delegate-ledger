#!/usr/bin/env python3
# 방금 USDC를 받은 주소들의 EIP-7702 위임 여부를 센다. 2026-11-15
import json,subprocess,sys,collections,time
chain=sys.argv[1]; nblocks=int(sys.argv[2])
RPC={'eth':'https://ethereum-rpc.publicnode.com','base':'https://mainnet.base.org'}[chain]
USDC={'eth':'0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48','base':'0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913'}[chain]
T='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
def rpc(payload):
    for k in range(4):
        out=subprocess.run(['curl','-s','-A','Mozilla/5.0',RPC,'-H','content-type: application/json','-d',json.dumps(payload)],capture_output=True,text=True).stdout
        try:
            d=json.loads(out)
            if isinstance(d,list) or 'result' in d: return d
            err=d
        except Exception: err=out[:200]
        time.sleep(1.5)
    raise SystemExit('rpc fail %s'%err)
head=int(rpc({'jsonrpc':'2.0','id':1,'method':'eth_blockNumber','params':[]})['result'],16)
rec=set(); step=5 if chain=='eth' else 20
for a in range(head-nblocks+1,head+1,step):
    b=min(a+step-1,head)
    logs=rpc({'jsonrpc':'2.0','id':1,'method':'eth_getLogs','params':[{'address':USDC,'topics':[T],'fromBlock':hex(a),'toBlock':hex(b)}]})['result']
    for l in logs: rec.add('0x'+l['topics'][2][26:])
rec=sorted(rec); print(chain,'head',head,'blocks',nblocks,'unique recipients',len(rec))
codes={}
for i in range(0,len(rec),40):
    batch=[{'jsonrpc':'2.0','id':j,'method':'eth_getCode','params':[x,'latest']} for j,x in enumerate(rec[i:i+40])]
    res=rpc(batch)
    if not isinstance(res,list): raise SystemExit(res)
    for r in res: codes[rec[i+r['id']]]=r.get('result','ERR')
    time.sleep(0.3)
eoa=[a for a,c in codes.items() if c=='0x']
deleg={a:'0x'+c[8:48] for a,c in codes.items() if c.lower().startswith('0xef0100') and len(c)==48}
contract=len(codes)-len(eoa)-len(deleg)
print('EOA(no code)',len(eoa),'delegated',len(deleg),'contract',contract)
nc=len(eoa)+len(deleg)
print('delegated / (EOA+delegated) = %.2f%%'%(100*len(deleg)/max(nc,1)), ' / all = %.2f%%'%(100*len(deleg)/max(len(codes),1)))
for d,n in collections.Counter(deleg.values()).most_common(15): print(n,d)
json.dump({'chain':chain,'head':head,'nblocks':nblocks,'codes_summary':{'eoa':len(eoa),'delegated':len(deleg),'contract':contract},'delegated':deleg},open('%s-%d.json'%(chain,head),'w'),indent=1)
