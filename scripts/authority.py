#!/usr/bin/env python3
# Recover the signing account (authority) of an EIP-7702 authorization tuple. Pure Python, no dependencies.
# msg = keccak256(0x05 || rlp([chain_id, address, nonce]));  authority = address(ecrecover(msg, y_parity, r, s))
RC=[0x1,0x8082,0x800000000000808A,0x8000000080008000,0x808B,0x80000001,0x8000000080008081,0x8000000000008009,0x8A,0x88,0x80008009,0x8000000A,0x8000808B,0x800000000000008B,0x8000000000008089,0x8000000000008003,0x8000000000008002,0x8000000000000080,0x800A,0x800000008000000A,0x8000000080008081,0x8000000000008080,0x80000001,0x8000000080008008]
ROT=[[0,36,3,41,18],[1,44,10,45,2],[62,6,43,15,61],[28,55,25,21,56],[27,20,39,8,14]]
M=(1<<64)-1
def _f(a):
    for rc in RC:
        c=[a[x][0]^a[x][1]^a[x][2]^a[x][3]^a[x][4] for x in range(5)]
        d=[c[(x-1)%5]^(((c[(x+1)%5]<<1)|(c[(x+1)%5]>>63))&M) for x in range(5)]
        a=[[a[x][y]^d[x] for y in range(5)] for x in range(5)]
        b=[[0]*5 for _ in range(5)]
        for x in range(5):
            for y in range(5):
                r=ROT[x][y]; v=a[x][y]
                b[y][(2*x+3*y)%5]=((v<<r)|(v>>(64-r)))&M if r else v
        a=[[b[x][y]^((~b[(x+1)%5][y])&b[(x+2)%5][y]) for y in range(5)] for x in range(5)]
        a[0][0]^=rc
    return a
def keccak256(data):
    rate=136; p=bytearray(data); p.append(0x01)
    while len(p)%rate: p.append(0)
    p[-1]|=0x80
    a=[[0]*5 for _ in range(5)]
    for off in range(0,len(p),rate):
        for i in range(rate//8):
            a[i%5][i//5]^=int.from_bytes(p[off+8*i:off+8*i+8],'little')
        a=_f(a)
    return b''.join(a[i%5][i//5].to_bytes(8,'little') for i in range(4))
def _rlp_item(b):
    if len(b)==1 and b[0]<0x80: return b
    if len(b)<56: return bytes([0x80+len(b)])+b
    l=len(b).to_bytes((len(b).bit_length()+7)//8,'big'); return bytes([0xb7+len(l)])+l+b
def _int(n): return b'' if n==0 else n.to_bytes((n.bit_length()+7)//8,'big')
def rlp_list(items):
    body=b''.join(_rlp_item(i) for i in items)
    if len(body)<56: return bytes([0xc0+len(body)])+body
    l=len(body).to_bytes((len(body).bit_length()+7)//8,'big'); return bytes([0xf7+len(l)])+l+body
P=2**256-2**32-977; N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G=(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
def _add(a,b):
    if a is None: return b
    if b is None: return a
    if a[0]==b[0]:
        if (a[1]+b[1])%P==0: return None
        l=3*a[0]*a[0]*pow(2*a[1],-1,P)%P
    else: l=(b[1]-a[1])*pow(b[0]-a[0],-1,P)%P
    x=(l*l-a[0]-b[0])%P; return (x,(l*(a[0]-x)-a[1])%P)
def _mul(k,pt):
    r=None
    while k:
        if k&1: r=_add(r,pt)
        pt=_add(pt,pt); k>>=1
    return r
def recover(msg_hash,y_parity,r,s):
    if not(0<r<N and 0<s<N): return None
    y2=(pow(r,3,P)+7)%P; y=pow(y2,(P+1)//4,P)
    if y*y%P!=y2: return None
    if y&1!=y_parity: y=P-y
    z=int.from_bytes(msg_hash,'big'); ri=pow(r,-1,N)
    q=_add(_mul(s*ri%N,(r,y)),_mul((-z*ri)%N,G))
    if q is None: return None
    return '0x'+keccak256(q[0].to_bytes(32,'big')+q[1].to_bytes(32,'big'))[12:].hex()
def authority(auth):
    """auth: one entry of a transaction's authorizationList as returned by eth_getTransactionByHash / eth_getBlockByNumber."""
    h=lambda k: int(auth[k],16)
    msg=keccak256(b'\x05'+rlp_list([_int(h('chainId')),bytes.fromhex(auth['address'][2:]),_int(h('nonce'))]))
    return recover(msg,h('yParity') if 'yParity' in auth else h('v'),h('r'),h('s'))
if __name__=='__main__':
    assert keccak256(b'').hex()=='c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470', 'keccak self-test failed'
    print('keccak ok')
