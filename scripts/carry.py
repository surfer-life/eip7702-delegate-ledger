#!/usr/bin/env python3
# When an evidence source did not answer in this run, keep the last grade we had evidence for, and say so.
# usage: carry.py previous.json current.json   (rewrites current.json in place)
import json,sys,collections
prev=json.load(open(sys.argv[1])); cur=json.load(open(sys.argv[2]))
P={r['delegate']:r for r in prev.get('delegates',[])}
when=prev.get('window',{}).get('to','an earlier run')
n=0
for r in cur['delegates']:
    p=P.get(r['delegate'])
    if r['grade']=='evidence-missing' and p and p['grade']!='evidence-missing':
        r['grade']=p['grade']; r['grade_carried_from']=p.get('grade_carried_from',when)
        for k in ('name','resembles','flagged_by_research','forwards_on_receive','probe'):
            if not r.get(k) and p.get(k): r[k]=p[k]
        keep=[x for x in (p.get('notes') or []) if not x.startswith('Farm pattern') and not x.startswith('An evidence source')]
        r['notes']=keep+[x for x in r.get('notes',[]) if x not in keep]+['An evidence source did not answer in this run; the grade is carried from the run ending %s.'%r['grade_carried_from']]
        n+=1
tot=sum(r['authorizations'] for r in cur['delegates']); by=collections.Counter()
for r in cur['delegates']: by[r['grade']]+=r['authorizations']
cur['share_of_authorizations_by_grade']={k:round(v/tot,3) for k,v in by.most_common()}
json.dump(cur,open(sys.argv[2],'w'),indent=1)
print('carried',n,cur['share_of_authorizations_by_grade'])
