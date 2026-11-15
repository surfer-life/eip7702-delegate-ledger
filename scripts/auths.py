#!/usr/bin/env python3
# 최근 N블록의 type 4 거래에서 위임(authorization) 대상을 센다. 2026-11-15
import json,subprocess,sys,time,collections
N=int(sys.argv[1]); RPC='https://ethereum-rpc.publicnode.com'
def rpc(m,p):
    for k in range(5):
        out=subprocess.run(['curl','-s','-m','60','--compressed','-A','Mozilla/5.0',RPC,'-H','content-type: application/json','-d',json.dumps({'jsonrpc':'2.0','id':1,'method':m,'params':p})],capture_output=True,text=True).stdout
        try:
            d=json.loads(out)
            if d.get('result') is not None: return d['result']
        except Exception: pass
        time.sleep(2)
    raise SystemExit('rpc fail')
head=int(rpc('eth_blockNumber',[]),16)
auth=collections.Counter(); txs=collections.Counter(); senders=collections.defaultdict(set); nonce0=collections.Counter(); ntx=0; n4=0
t0=None
for b in range(head-N+1,head+1):
    blk=rpc('eth_getBlockByNumber',[hex(b),True])
    if t0 is None: t0=int(blk['timestamp'],16)
    t1=int(blk['timestamp'],16)
    for t in blk['transactions']:
        ntx+=1
        if t['type']!='0x4': continue
        n4+=1; seen=set()
        for a in t.get('authorizationList') or []:
            d=a['address'].lower(); auth[d]+=1; seen.add(d)
            if int(a['nonce'],16)==0: nonce0[d]+=1
        for d in seen: txs[d]+=1; senders[d].add(t['from'])
    if (b-head+N)%100==0: print(b-head+N,'/',N,'type4',n4,flush=True)
res={'head':head,'N':N,'from_ts':t0,'to_ts':t1,'total_txs':ntx,'type4_txs':n4,'delegates':[{'delegate':d,'authorizations':c,'txs':txs[d],'distinct_senders':len(senders[d]),'nonce0':nonce0[d]} for d,c in auth.most_common()]}
json.dump(res,open('auths-%d.json'%head,'w'),indent=1)
print('DONE head',head,'txs',ntx,'type4',n4,'delegates',len(auth),'authorizations',sum(auth.values()))
for x in res['delegates'][:15]: print(x)
