# Brief: score CRO vendors on the 17-criterion scorecard

You are scoring vendors for an ADA / PK / toxicology CRO shortlist (Asia). Read FIRST, fully:
1. rubric.txt  (the rubric: 17 sub-criteria, max points, tier bands, hard gate, "Insufficient Data" rule)
2. evidence_examples.json  (real evidence rows for 3 vendors already scored this way: match their reasoning style)
3. Your vendors' evidence files: pre/score_in/<directory_row>.json  (rows listed in your group file). Each holds directory data, the researched entity type/services, hard-gate flags, notes, conference presence and criteria_findings (finding text, source url, source_type, confidence, verification) collected by earlier research. Do NOT search the web for this task; score only from what is in the file. (If a finding is clearly ambiguous, say so in the rationale and score conservatively.)

## The 17 sub-criteria and maximum points
GLP Status 8; Regulatory Inspection History 7; Accreditations 5; Data Integrity (ALCOA+, LIMS) 5; Assay Platform Breadth 8; Modality Experience 6; Species Range for Tox 6; Method Validation Track Record 5; CRO Revenue / Employee Band 5; Concurrent Client/Study Load 5; Equipment Inventory 6; Backup / Redundancy Systems 4; Years in Operation / Filings Supported 5; Client References 4; Publications / Guideline Contribution 1; Cost Competitiveness 6; Turnaround Time 4.
Scores are whole numbers from 0 to the maximum, or the exact text "Insufficient Data".

## Scoring conventions (apply consistently; these match how the earlier vendors in the scorecard were scored)
- "Insufficient Data" = no usable evidence for that item in the file. It is NOT 0. Use 0 only when evidence shows the item genuinely scores zero (e.g. a documented search that finds no publications; GLP certificate expired and none current; unresolved warning letter).
- Follow the tier bands in the rubric literally. Examples: GLP Status 8 needs OECD GLP + local certificate (NGCMA/NMPA/MFDS/TFDA-TAF/PMDA/FAMIC etc. count as the OECD-MAD local cert); local cert only = 4-5; pending = 1-3; none/expired = 0-1. Scope matters: GLP limited to agrochemical, device-biocompatibility or analytical-chemistry scope for a vendor evaluated for pharma PK/ADA/tox should be noted, and the GLP score should reflect pharma-relevant scope (cap at 5 and say why if the scope is not pharma-relevant).
- Source quality: regulator registries / inspection databases / accreditation bodies / stock-exchange filings / peer-reviewed papers / independent news are best. Vendor-authored statements MAY be used for concrete capability facts (platforms named, species housed, equipment listed, facility size, years, staff count) at medium-low score within the band; vendor-only claims about regulatory outcomes, data integrity, client satisfaction, pricing or turnaround without independent support => "Insufficient Data" (Data Integrity needs a regulator/audit comment or a named validated LIMS with evidence; a bare vendor statement is not enough).
- Regulatory Inspection History scores real inspections by FDA/EMA/PMDA/MHRA/WHO/NMPA/MFDS/TFDA etc.: clean/NAI/VAI-resolved = high; minor 483 resolved = 4-5; major finding resolved = 1-3; unresolved Warning Letter/OAI/data-integrity failure = 0. Certification audits only (NGCMA/TAF certification) are not USFDA/EMA/PMDA audits: Insufficient Data unless a regulator inspection is evidenced.
- Accreditations: AAALAC + NABL/CNAS/TAF + ISO 17025 = 5; 2 of those = 3; only 1 or local-only = 1.
- CRO Revenue / Employee Band: mid-size regional (roughly 50-500 staff, regional CRO) = 4-5; large multinational or growing small CRO = 3; very small/single-lab/brand-new = 1.
- Years/Filings: 10+ yrs and multiple IND/NDA/CTA = 5; 5-10 yrs/some filings = 3; <5 yrs or unverifiable = 1.
- Publications: 1 if active publication/conference presence documented; 0 only if a search documented none; else Insufficient Data. (The conference_presence list counts as presence.)
- Location Tier (dropdown text, exact): "India or China", "Nearby Asia (SE Asia/Japan/S.Korea/Taiwan)", "Other Asia", "Outside Asia". Israel/Central or West Asia = "Other Asia". Use the facility that would perform the work.
- Hard Gate "N" if: no valid GLP status (certificate expired with no evidence of renewal, never certified, or GLP only for an irrelevant scope AND no pharma-relevant GLP), OR an unresolved major regulatory finding (e.g. unresolved FDA Warning Letter / data-integrity failure), OR refuses a CDA. Otherwise "Y". An entity that is NOT a third-party contract vendor (in-house lab, lab-animal supplier, academic facility with no contract service evidence) gets "N" with that stated in the rationale. When the gate is N, still score the 17 items from the evidence (the earlier vendors were scored this way).
- Never copy a score from another entity that shares a name or street (several files carry identity warnings: follow them).
- Be conservative and transparent. Prefer "Insufficient Data" to a guess.

## Output
For each vendor write ONE JSON file: pre/scores/<directory_row>.json
{
 "directory_row": <int>,
 "scorecard_name": "<clean vendor name for the scorecard: directory name without bracketed 'also listed as'/URL suffixes; for Chinese-only names write 'Chinese name (English name)'>",
 "country_city": "<City, Country>",
 "hard_gate": "Y" or "N",
 "hard_gate_reason": "<one sentence>",
 "location_tier": "<exact dropdown text>",
 "scores": { "GLP Status": 8|"Insufficient Data", ... all 17 keys exactly as listed above ... },
 "rationale": { "<each of the 17 keys>": "<one short sentence: why this score, with the source type/confidence; for Insufficient Data say what was missing>" },
 "evidence_refs": { "<key>": {"finding":"<<=230 chars: the specific fact used>", "source_url":"<url from the file or null>", "source_type":"<from file>", "confidence":"high|medium|low"} }   // include an entry for every key that has a numeric score
 "directory_note": "<one sentence: what this vendor is and the main caveat for a user choosing it>"
}
When done reply with ONE line per vendor: row, name, hard gate, total of numeric scores, number of "Insufficient Data" items. Nothing else.
