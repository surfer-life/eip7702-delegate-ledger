#!/usr/bin/env python3
# 위임 대상 계약마다 증거를 모아 등급을 붙인다. 입력: 대상 주소 목록(JSON 배열 파일). 2026-11-15
# 등급은 내가 직접 읽은 증거로만 정한다. 증거가 없으면 'unknown'이다.
import json,subprocess,sys,time
RPC='https://ethereum-rpc.publicnode.com'
def curl(u,data=None):
    a=['curl','-s','-m','40','-A','Mozilla/5.0',u]
    if data: a+=['-H','content-type: application/json','-d',json.dumps(data)]
    for k in range(3):
        try:
            j=json.loads(subprocess.run(a,capture_output=True,text=True).stdout)
            if isinstance(j,dict): return j
        except Exception: pass
        time.sleep(4)
    return {}
def sourcify(d):
    j=curl('https://sourcify.dev/server/v2/contract/1/%s?fields=compilation.name,deployment.deployer'%d)
    if 'address' not in j: return {'match':None,'name':None,'deployer':None,'error':True}
    return {'match':j.get('match'),'name':(j.get('compilation') or {}).get('name'),'deployer':(j.get('deployment') or {}).get('deployer')}
def grade(d):
    code=curl(RPC,{'jsonrpc':'2.0','id':1,'method':'eth_getCode','params':[d,'latest']}).get('result','0x')
    info=curl('https://eth.blockscout.com/api/v2/addresses/'+d)
    sc=curl('https://eth.blockscout.com/api/v2/smart-contracts/'+d) if info.get('is_verified') else {}
    src=(sc.get('source_code') or '')
    sf=sourcify(d)
    explorer_ok='hash' in info      # False = the explorer did not answer; do not read that as 'unverified'
    e={'delegate':d,'code_bytes':(len(code)-2)//2,'name':info.get('name') or sf.get('name'),'source_verified':bool(info.get('is_verified')),
       'explorer_answered':explorer_ok,'sourcify':sf,
       'explorer_scam_flag':bool(info.get('is_scam')),'proxy_type':(info.get('proxy_type') or sc.get('proxy_type')),
       'verified_at':sc.get('verified_at'),'source_chars':len(src),
       'source_mentions':[w for w in ['address poisoning','scam','thief','Wintermute','sweep','drain'] if w.lower() in src.lower()],
       'evidence_from':'eth_getCode at publicnode; eth.blockscout.com address + smart-contract API'}
    if e['code_bytes']==0: g='no-code'      # 코드 없는 주소에 위임 = 위임 해제이거나 실수
    elif e['explorer_scam_flag'] or 'address poisoning' in e['source_mentions']: g='known-malicious'
    elif not e['source_verified'] and not sf.get('match'):
        g='unverified-source' if (explorer_ok and not sf.get('error')) else 'evidence-missing'
    elif e['proxy_type']: g='verified-but-upgradeable'
    else: g='verified-source'
    if info.get('is_verified') and 'source_code' not in sc and g!='known-malicious': g='evidence-missing'   # verified, but the source text could not be read this run
    e['grade']=g
    return e
if __name__=='__main__':
    L=json.load(open(sys.argv[1])); out=[]
    for d in L:
        e=grade(d); out.append(e); print(e['grade'],'|',d,'|',e['name'],'|',e['code_bytes'],'|',e['proxy_type'],'|',e['source_mentions'],flush=True); time.sleep(0.5)
    json.dump(out,open(sys.argv[2],'w'),indent=1)
