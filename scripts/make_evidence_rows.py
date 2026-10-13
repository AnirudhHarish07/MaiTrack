import json,glob,os
rows=json.load(open('scorecard_new.json'))['rows']
D=[];E=[]
miss=0
for r in rows:
    s=json.load(open(f'scores/{r}.json'))
    nm=s['scorecard_name']
    ins=[k for k,v in s['scores'].items() if v=="Insufficient Data"]
    gate=s['hard_gate']
    k="Y (from Scorecard)" if gate=="Y" else "N (from Scorecard): "+s['hard_gate_reason']
    l=f"Scored (see Scorecard; 2026-10-04 scoring pass). Provisional: {17-len(ins)}/17 criteria scored; {len(ins)} still Insufficient Data (queued for follow-up research)."
    D.append([r,"Y",k,l])
    for crit,v in s['scores'].items():
        if v=="Insufficient Data": continue
        ref=s['evidence_refs'].get(crit)
        if not ref: miss+=1; ref={'finding':'(see rationale)','source_url':'','source_type':'','confidence':''}
        E.append([nm,crit,v,ref.get('source_type',''),ref.get('source_url',''),ref.get('finding',''),"'2026-10-04",f"{ref.get('confidence','')} | rationale: {s['rationale'][crit]}"])
    E.append([nm,"Location Tier",s['location_tier'],"registry / vendor_site","", s['country_city'],"'2026-10-04","from directory HQ location"])
    E.append([nm,"Hard Gate (Y/N)",gate,"derived from GLP + inspection evidence rows","",s['hard_gate_reason'],"'2026-10-04","see GLP / inspection rows"])
print(len(D),len(E),miss)
json.dump(D,open('dir_i_k_l.json','w'),ensure_ascii=False)
json.dump(E,open('ev_new.json','w'),ensure_ascii=False)
print(sum(len(json.dumps(x,ensure_ascii=False)) for x in E))
print(D[0]); print(E[0])
