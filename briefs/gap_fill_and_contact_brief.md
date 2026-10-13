# Brief: fill "Insufficient Data" cells and collect company contact details (Asia CRO shortlist: ADA / PK / toxicology)

Read first: rubric.txt (17 sub-criteria, max points, bands) and the scoring conventions in pre/score_brief.md (section "Scoring conventions"; follow it exactly; it overrides anything vague here).

Your vendors are listed in your group file (a JSON list of sheet_row numbers). For each, read fill/in/<sheet_row>.json: it has the vendor name, city, hard gate, the 17 current scores ("Insufficient Data" = no usable evidence so far), `missing_research` (the criteria to try to fill), and `prior_evidence` (facts already found; do not re-research those, and do not change numeric scores that already exist).

## Task A - fill the gaps
For each criterion in `missing_research`, look for real evidence and propose a score ONLY if you find usable evidence; otherwise leave it out (it stays "Insufficient Data"). Cost Competitiveness and Turnaround Time are NOT in scope unless you stumble on a public fee schedule / published TAT.
Good sources: the vendor website (about, facilities, equipment, services, news, careers), regulator registries (fda.gov nonclinical GLP inspection list https://www.fda.gov/media/89825/download and warning letters, dst.gov.in NGCMA GLP PDFs, TFDA/TAF GLP lists, MFDS, PMDA/FAMIC, WHO PQ inspection reports, NMPA), AAALAC directory, NABL/CNAS/TAF, stock-exchange filings, PubMed/PMC papers with the vendor's affiliation, conference exhibitor/speaker lists (SOT, EUROTOX, AAPS, WRIB, EBF, CPHI, BioAsia, BIO Asia, BioJapan, JSOT/KSOT/CSOT), news, job postings (instruments, LIMS), LinkedIn search-result text.
Conventions that matter most here:
- Regulatory Inspection History needs a REAL regulator inspection (FDA/EMA/PMDA/MHRA/WHO/NMPA/MFDS/TFDA etc.). Certification audits alone are not inspections.
- Data Integrity needs a regulator/audit comment or a named validated LIMS/e-system with evidence; a bare vendor claim is not enough. Backup/Redundancy needs documented power/data/instrument redundancy; Concurrent Load needs capacity/backlog evidence. These are often not public: leave out rather than guess.
- Vendor-authored pages are fine for concrete capability facts (platforms, species, equipment lists, staff counts, facility size, years) at medium-low score; vendor-only claims about regulatory outcomes, quality, pricing, turnaround => do not score.
- Never copy facts from another entity with a similar name; if identity is doubtful, say so and skip.
- If a finding changes the picture for the hard gate (e.g. GLP certificate found valid, or an unresolved warning letter, or the entity is not a contract vendor), say so in `gate_note`.
Search budget: about 10 WebSearch calls per vendor at most, shared session limit; stop searching if a search errors. The WebFetch tool is blocked here; you may fetch specific public pages with Bash curl through the pre-configured proxy (HTTPS_PROXY + CA bundle /root/.ccr/ca-bundle.crt already set), e.g. curl -sS -L -m 30 -A 'Mozilla/5.0' URL | head -c 200000 then extract text. Never disable TLS verification, never unset the proxy, never use curl against search engines. LinkedIn returns an anti-bot block to automated requests: do not try to defeat it; use only URLs seen in search results. Date accessed: 2026-10-04.

## Task B - company contact details (public company-level info only)
For each vendor also record: official website; LinkedIn company page URL (only if seen in a search result or loaded page and clearly the right entity); head-office / site address (the facility that would do the work and the registered HQ if different); general company phone number (switchboard / business development line shown on the official site); general company email (info@/contact/BD address shown on the official site). Company-level only: do NOT record personal names, personal emails, personal mobile numbers or social-media profiles of individuals. Take values only from the official site, a regulator/registry listing or an accreditation directory; if not found, use null. Never invent anything.

## Output
For each vendor write ONE JSON file: fill/out/<sheet_row>.json
{
 "sheet_row": <int>,
 "vendor": "<name>",
 "new_scores": { "<criterion exact name>": {"score": <int within max>, "finding": "<=230 chars, the specific fact>", "source_url": "<url>", "source_type": "regulator_registry|regulator_inspection_db|accreditation_body|vendor_site|linkedin|conference|publication|news|third_party_database|job_posting|stock_exchange_filing", "confidence": "high|medium|low", "rationale": "<one sentence: why this score under the rubric band>"} },
 "gate_note": "<null or one sentence>",
 "details": {"website": null, "linkedin_url": null, "hq_address": null, "site_address": null, "phone": null, "email": null, "detail_sources": ["<urls>"], "detail_notes": "<null or short caveat>"},
 "still_missing": ["<criteria still without evidence>"]
}
Use the exact criterion names: "GLP Status","Regulatory Inspection History","Accreditations","Data Integrity (ALCOA+, LIMS)","Assay Platform Breadth","Modality Experience","Species Range for Tox","Method Validation Track Record","CRO Revenue / Employee Band","Concurrent Client/Study Load","Equipment Inventory","Backup / Redundancy Systems","Years in Operation / Filings Supported","Client References","Publications / Guideline Contribution","Cost Competitiveness","Turnaround Time".
Write each file as soon as you finish that vendor (so work survives an interruption). Do vendors in the order of the group file. If you run out of budget, still write files for the remaining vendors with new_scores {} and whatever details you have.
Final reply: ONE line per vendor: sheet_row, name, number of new scores, whether website/phone/email were found (Y/N each). Nothing else.
