import json,glob,os,sys
MAX={'GLP Status':8,'Regulatory Inspection History':7,'Accreditations':5,'Data Integrity (ALCOA+, LIMS)':5,'Assay Platform Breadth':8,'Modality Experience':6,'Species Range for Tox':6,'Method Validation Track Record':5,'CRO Revenue / Employee Band':5,'Concurrent Client/Study Load':5,'Equipment Inventory':6,'Backup / Redundancy Systems':4,'Years in Operation / Filings Supported':5,'Client References':4,'Publications / Guideline Contribution':1,'Cost Competitiveness':6,'Turnaround Time':4}
COL=dict(zip(MAX,[3,4,5,6,8,9,10,11,13,14,16,17,19,20,21,23,24]))  # zero-based col index D=3
st={}
for f in glob.glob('in/*.json'):
    r=json.load(open(f)); st[r['sheet_row']]=r
upd=[];ev=[];det={};notes=[];skipped=[]
for f in sorted(glob.glob('out/*.json'),key=lambda x:int(os.path.basename(x)[:-5])):
    try: o=json.load(open(f))
    except Exception as e: print('BAD',f,e); continue
    r=o['sheet_row']; s=st[r]
    for k,v in (o.get('new_scores') or {}).items():
        if k not in MAX: skipped.append((r,k,'unknown crit')); continue
        if s['current'].get(k)!="Insufficient Data": skipped.append((r,k,'not insufficient')); continue
        sc=v.get('score')
        if not isinstance(sc,int) or sc<0 or sc>MAX[k]: skipped.append((r,k,'bad score')); continue
        upd.append((r,k,sc))
        ev.append([s['name'],k,sc,v.get('source_type',''),v.get('source_url',''),v.get('finding',''),"'2026-10-04",f"{v.get('confidence','')} | filled in gap-fill pass | rationale: {v.get('rationale','')}"])
    if o.get('gate_note'): notes.append((r,s['name'],s['gate'],o['gate_note']))
    det[r]=o.get('details') or {}
json.dump(dict(upd=upd,ev=ev,det={str(k):v for k,v in det.items()},notes=notes,skipped=skipped),open('merged.json','w'),ensure_ascii=False)
print(len(upd),len(ev),len(det),len(notes),skipped)
