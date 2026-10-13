You are continuing an automated Asia-region CRO discovery and scoring project in Google Sheets. Today you add 20-25 NEW CROs, fill their details and directory entries together, then score them. Use the Google Sheets and Google Drive connectors. Do not create new files; work only in the existing sheet "CRO Vendor Scorecard", id 1J7G3_EVmlChUVFQJCAzMfmU5rHBEiODX0rNT9L81vQU. If a repo is checked out, docs/workflow.md, docs/rubric.md and briefs/scoring_brief.md hold the full rules; the Legend & Rubric tab holds the rubric and the notes at A62:A67.

SCOPE
- Companies in Asia only (China, India, Japan, South Korea, Taiwan, SE Asia, other Asia incl. Israel/Central/West Asia) that offer PK/TK, ADA/immunogenicity bioanalysis or toxicology (GLP or nonclinical) as contract services. Skip anything outside Asia.
- Before adding, read the CRO Directory (A:A, G:G and the name/website columns) and Company Details and skip any company already there, including renamed/merged/duplicate names and parent-company variants.
- Find candidates from web search, regulator GLP registries (NGCMA/dst.gov.in, CDSCO, NMPA, MFDS, TFDA/TAF, PMDA/FAMIC, FDA nonclinical GLP list https://www.fda.gov/media/89825/download), AAALAC directory, toxicology/bioanalysis conference exhibitor and speaker lists (SOT, EUROTOX, AAPS, WRIB, EBF, CPHI, BioAsia, BioJapan, JSOT/KSOT/CSOT), PubMed affiliations, LinkedIn search-result text. Do not try to log in to or defeat LinkedIn anti-bot; use LinkedIn URLs only if seen in search results and clearly the right entity.
- Target 20-25 new companies. If the session limit or a connector failure stops you early, stop cleanly and log how far you got.

FOR EACH NEW COMPANY, IN THIS ORDER (details and directory together, then score)
1. CRO Directory: append at the first empty row. Columns: A name, B HQ City/Country, C type, D services, E verified Y/N, F LinkedIn URL, G source URL, H date added (text, e.g. '2026-10-14), I fully scored Y/N, J region, K hard gate status, L scoring status, M conference presence, N evidence by criterion, O criteria still missing, P flags for scorer, Q research basis.
2. Company Details: write to the row with the same number as the Directory row. A name, B directory row, C phone, D email, E LinkedIn, F HQ address, G site address (where the work is done), H website, I source URLs (newline separated), J date accessed (text), K notes. Public company-level info only, taken from the official site, a regulator/registry listing or an accreditation directory. No personal names, emails or mobile numbers. Never invent; leave blank if not found and say so in the notes.
3. Scorecard: write to the first empty row from row 150 onward (formulas in H, M, P, S, W, Z, AB-AE are pre-filled to row 300; if you would pass row 300, copy the formulas down first and never overwrite them). Inputs: A name (clean; for Chinese-only names "Chinese name (English name)"), B Country/City, C Hard Gate Y/N, D-G, I-L, N-O, Q-R, T-V, X-Y scores, AA Location Tier (exact text: "India or China", "Nearby Asia (SE Asia/Japan/S.Korea/Taiwan)", "Other Asia", "Outside Asia").
4. Sources & Evidence Log: append one row per numeric score: vendor, sub-criterion, score, source type, source URL, specific fact (<=230 chars), date accessed (text with leading apostrophe), confidence | rationale. Also add Location Tier and Hard Gate rows.
5. Update the Directory row: I = Y, K = hard gate result with reason, L = scoring status.

SCORING RULES (same as the existing 145 vendors)
- 17 criteria with maximum points: GLP Status 8; Regulatory Inspection History 7; Accreditations 5; Data Integrity (ALCOA+, LIMS) 5; Assay Platform Breadth 8; Modality Experience 6; Species Range for Tox 6; Method Validation Track Record 5; CRO Revenue/Employee Band 5; Concurrent Client/Study Load 5; Equipment Inventory 6; Backup/Redundancy 4; Years in Operation/Filings 5; Client References 4; Publications 1; Cost Competitiveness 6; Turnaround Time 4. Follow the tier bands in the Legend & Rubric tab literally.
- Score only from evidence you found. "Insufficient Data" (exact text) means no usable evidence and is NOT 0. Use 0 only when evidence shows a genuine zero. Prefer Insufficient Data to a guess. Cost and Turnaround stay Insufficient Data unless a public fee schedule or published TAT exists.
- Regulatory Inspection History needs a real regulator inspection (FDA/EMA/PMDA/MHRA/WHO/NMPA/MFDS/TFDA...). Certification audits alone are not inspections.
- Data Integrity needs a regulator/audit comment or a named validated LIMS/e-system with evidence. Vendor-only claims about regulatory outcomes, data integrity, client satisfaction, pricing or turnaround are not scored.
- Vendor-authored pages are fine for concrete capability facts (platforms, species, equipment, staff count, facility size, years) at a medium-low score.
- GLP Status: OECD GLP + local certificate = 8; local only = 4-5; pending = 1-3; none/expired = 0-1. Cap at 5 if GLP scope is not pharma-relevant, and say so.
- Hard Gate N if no valid GLP, unresolved major regulatory finding, refuses a CDA, or not a third-party contract vendor (in-house lab, academic unit with no contract service evidence). When N, still score the 17 items from the evidence.
- Never copy facts from another entity with a similar name or address. If identity is doubtful, say so and skip.
- Tiers (formula-driven): >=75 Tier 1, 50-74 Tier 2, 30-49 Tier 3, else Excluded.

SHEET WRITE RULES
- Write with USER_ENTERED values. Text beginning with + - = @ is treated as a formula or number: put an apostrophe in front of every phone number and every date text.
- null cells are skipped by update_values; use "" to blank a cell. Write in blocks of a few companies at a time, and read back a sample of rows after writing.
- Copy non-Latin names exactly from the source text; do not type \uXXXX escapes by hand.
- Do not overwrite or rescore existing vendors. Never delete rows or tabs.
- WebFetch may be blocked; fetch specific public pages with curl through the configured proxy. Never disable TLS verification, never unset the proxy.
- If the Sheets/Drive connection drops, reload the tools (ToolSearch) and continue; if it cannot be restored, stop and log.

RUN LOG
At the end append one row to a tab named "Run Log" (create it if missing; columns: Date, Companies added, Directory rows (first-last), Scored, Tier 1/2/3/Excluded counts for this run, Notes/problems). Also note any company you could not finish so the next run can complete it first.

FINAL OUTPUT
Reply with: how many companies added and scored, the Directory row range, tier counts for the new vendors, and any problems (connector drops, blocked sites, doubtful identities). Do not send any email or message to anyone.
