#!/usr/bin/env python3
# 최근 N블록의 type 4 거래에서 위임(authorization) 대상을 센다. 2026-11-15
import json,subprocess,sys,time,collections,os,concurrent.futures as cf
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from authority import authority
N=int(sys.argv[1]); RPCS=['https://ethereum-rpc.publicnode.com','https://eth.drpc.org']
def rpc(m,p,seed=0):
    # Rotate across endpoints so throttling on one (common on shared CI IPs) falls back to another.
    for k in range(6):
        url=RPCS[(k+seed)%len(RPCS)]
        out=subprocess.run(['curl','-s','-m','60','--compressed','-A','Mozilla/5.0',url,'-H','content-type: application/json','-d',json.dumps({'jsonrpc':'2.0','id':1,'method':m,'params':p})],capture_output=True,text=True).stdout
        try:
            d=json.loads(out)
            if d.get('result') is not None: return d['result']
        except Exception: pass
        time.sleep(1+k)
    raise SystemExit('rpc fail: '+m)
def get_block(b): return rpc('eth_getBlockByNumber',[hex(b),True],seed=b)
head=int(rpc('eth_blockNumber',[]),16)
samples=collections.defaultdict(dict); accts=collections.defaultdict(set); where=collections.defaultdict(set); per_acct=collections.Counter(); bad_sig=0; auth=collections.Counter(); txs=collections.Counter(); senders=collections.defaultdict(set); nonce0=collections.Counter(); ntx=0; n4=0
t0=None
# fetch blocks concurrently in chunks (bounded memory), process each chunk in block order
CHUNK=200; POOL=8
for lo in range(head-N+1,head+1,CHUNK):
  nums=list(range(lo,min(lo+CHUNK,head+1)))
  with cf.ThreadPoolExecutor(max_workers=POOL) as ex:
    blocks=dict(zip(nums,ex.map(get_block,nums)))
  for b in nums:
    blk=blocks[b]
    if t0 is None: t0=int(blk['timestamp'],16)
    t1=int(blk['timestamp'],16)
    for t in blk['transactions']:
        ntx+=1
        if t['type']!='0x4': continue
        n4+=1; seen=set()
        for a in t.get('authorizationList') or []:
            d=a['address'].lower(); auth[d]+=1; seen.add(d)
            if int(a['nonce'],16)==0: nonce0[d]+=1
            try: w=authority(a)
            except Exception: w=None
            if w is None: bad_sig+=1; continue
            accts[d].add(w); where[w].add(d); per_acct[w]+=1
            sm=samples[d]; sm.pop(w,None); sm[w]={k:a[k] for k in ('chainId','address','nonce','yParity','r','s') if k in a}
            if len(sm)>8: sm.pop(next(iter(sm)))
        for d in seen: txs[d]+=1; senders[d].add(t['from'])
    if (b-head+N)%100==0: print(b-head+N,'/',N,'type4',n4,flush=True)
contested={w for w,ds in where.items() if len(ds)>1}
res={'contested':{w:{'targets':sorted(where[w]),'authorizations':per_acct[w]} for w in sorted(contested)},'distinct_accounts':len(where),'contested_accounts':len(contested),'authorizations_from_contested':sum(per_acct[w] for w in contested),'unrecoverable_signatures':bad_sig,'head':head,'N':N,'from_ts':t0,'to_ts':t1,'total_txs':ntx,'type4_txs':n4,'delegates':[{'delegate':d,'authorizations':c,'txs':txs[d],'distinct_senders':len(senders[d]),'nonce0':nonce0[d],'distinct_accounts':len(accts[d]),'contested_accounts':len(accts[d]&contested),'samples':list(samples[d].values())} for d,c in auth.most_common()]}
json.dump(res,open(sys.argv[2] if len(sys.argv)>2 else 'auths-%d.json'%head,'w'),indent=1)
print('accounts',len(where),'contested',len(contested),'auths from contested',res['authorizations_from_contested'])
print('DONE head',head,'txs',ntx,'type4',n4,'delegates',len(auth),'authorizations',sum(auth.values()))
for x in res['delegates'][:15]: print(x)
