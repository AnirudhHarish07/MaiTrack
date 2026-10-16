You are continuing an automated Asia-region CRO discovery and scoring project in Google Sheets. Each run you (1) first finish anything the previous run left unfinished, then (2) add new CROs until the day's total is about 15, with details and directory entries filled together, every company verified by a second helper, and then scored. Use the Google Sheets and Google Drive connectors. Do not create new files; work only in the existing sheet "CRO Vendor Scorecard", id 1J7G3_EVmlChUVFQJCAzMfmU5rHBEiODX0rNT9L81vQU. If a repo is checked out, docs/workflow.md, docs/rubric.md and briefs/scoring_brief.md hold the full rules; the Legend & Rubric tab holds the rubric and the notes at A62:A67.

START OF EVERY RUN: FINISH WHAT IS UNFINISHED FIRST
1. Read the last rows of the "Run Log" tab, especially column G "Unfinished / follow-up for next run". Also scan the CRO Directory for rows added by earlier runs where column I is not "Y", and for any Directory row that has no matching Company Details row (same row number), Scorecard row, or evidence rows.
2. Complete those companies first, using the same research, verification and writing steps as for new companies. For these rows you may fill only EMPTY cells (missing details, LinkedIn, scores, evidence rows). Never overwrite a cell that already has a value.
3. Items listed in the Run Log under "Re-check later" are flags for the user, not unfinished work. Do not touch them.
4. Companies you finish from the previous run count toward the day's 15. Then add new companies until the total handled this run is about 15.
5. Log in the Run Log how many previously unfinished companies you completed.

SCOPE
- Companies in Asia only (China, India, Japan, South Korea, Taiwan, SE Asia, other Asia incl. Israel/Central/West Asia) that offer PK/TK, ADA/immunogenicity bioanalysis or toxicology (GLP or nonclinical) as contract services. Skip anything outside Asia.
- Before adding, read the CRO Directory (A:A, G:G and the name/website columns) and Company Details and skip any company already there, including renamed/merged/duplicate names and parent-company variants.
- Find candidates from web search, regulator GLP registries (NGCMA/dst.gov.in, CDSCO, NMPA, MFDS, TFDA/TAF, PMDA/FAMIC, FDA nonclinical GLP list https://www.fda.gov/media/89825/download), AAALAC directory, toxicology/bioanalysis conference exhibitor and speaker lists (SOT, EUROTOX, AAPS, WRIB, EBF, CPHI, BioAsia, BioJapan, JSOT/KSOT/CSOT), PubMed affiliations, and Google search results.
- If the session limit or a connector failure stops you early, stop cleanly and log exactly which companies and which fields are unfinished.

LINKEDIN FOR EVERY COMPANY (required)
- For every company, search Google for its LinkedIn company page, for example: site:linkedin.com/company "<company name>", then again with the local-language name and with the city if the first search finds nothing. No LinkedIn connector is available and you must not log in to LinkedIn or try to defeat its anti-bot; use only what appears in search results.
- Record the company page URL (linkedin.com/company/<id>) in Directory column F and Company Details column E. Accept a result only if the snippet or page matches the company on name AND at least one of location, website or industry. Company pages only: never record personal profiles.
- If nothing matches after the searches above, leave it blank and write "LinkedIn searched on Google, not found" in the Company Details notes. Do not guess a URL.
- The verifier helper rechecks every LinkedIn URL for identity.

APPEND-ONLY (hard rule)
- New companies go AFTER the existing data: new rows below the last used row of CRO Directory, Company Details, Scorecard and Sources & Evidence Log.
- Never edit, reorder, sort, move, delete or rescore any existing row, cell, formula or tab (the Tier View tab is a live formula view; do not touch it). The only exception is filling empty cells of a half-finished row from a previous run, as described above.
- If an existing entry looks wrong, do not fix it: add a line to the Run Log "Notes/problems" for the user.
- Before each write, read the target range and confirm it is empty.

TWO-STEP WORK: RESEARCHER THEN VERIFIER (use the Agent tool for helpers)
- Step 1, researcher helpers: each takes a few candidate companies and writes ONE JSON file per company in a scratch folder (Directory fields, Company Details fields including LinkedIn, 17 proposed scores each with finding, source_url, source_type, confidence, rationale, hard gate and reason). Researchers do NOT write to the sheet.
- Step 2, verifier helper(s), a different agent from the researcher: for every company, independently re-open the cited source URLs (curl via the proxy, or search) and judge each item: (a) is this the right entity, not a similarly named one; (b) does the page really contain the stated finding; (c) does the score follow the rubric band and the rules below; (d) do the phone, email, address, website and LinkedIn URL match an official, registry or search-result source; (e) is any vendor-only claim being scored. The verifier returns per item: verified / corrected (with the corrected value) / rejected, plus a short reason.
- Only verified or corrected items are written to the sheet. Rejected scores become "Insufficient Data" (not 0); rejected contact details and LinkedIn URLs are left blank; the Directory flag column P says what was rejected. A company whose identity cannot be verified is not added; list it in the Run Log.
- Add a Directory note (Q, research basis) saying "researched and independently verified <date>".

FOR EACH VERIFIED COMPANY, IN THIS ORDER (details and directory together, then score)
1. CRO Directory: append at the first empty row below the existing data. Columns: A name, B HQ City/Country, C type, D services, E verified Y/N, F LinkedIn URL, G source URL, H date added (text, e.g. '2026-10-16), I fully scored Y/N, J region, K hard gate status, L scoring status, M conference presence, N evidence by criterion, O criteria still missing, P flags for scorer, Q research basis.
2. Company Details: write to the row with the same number as the Directory row. A name, B directory row, C phone, D email, E LinkedIn, F HQ address, G site address (where the work is done), H website, I source URLs (newline separated), J date accessed (text), K notes. Public company-level info only, taken from the official site, a regulator/registry listing or an accreditation directory (LinkedIn per the rule above). No personal names, emails or mobile numbers. Never invent; leave blank if not found and say so in the notes.
3. Scorecard: write to the first empty row below the last vendor (formulas in H, M, P, S, W, Z, AB-AE are pre-filled to row 300; if you would pass row 300, copy the formulas down first and never overwrite them). Inputs: A name (clean; for Chinese-only names "Chinese name (English name)"), B Country/City, C Hard Gate Y/N, D-G, I-L, N-O, Q-R, T-V, X-Y scores, AA Location Tier (exact text: "India or China", "Nearby Asia (SE Asia/Japan/S.Korea/Taiwan)", "Other Asia", "Outside Asia").
4. Sources & Evidence Log: append one row per numeric score: vendor, sub-criterion, score, source type, source URL, specific fact (<=230 chars), date accessed (text with leading apostrophe), confidence | rationale. Also add Location Tier and Hard Gate rows.
5. Update the Directory row: I = Y, K = hard gate result with reason, L = scoring status.

SCORING RULES (same as the existing vendors)
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
At the end append one row to the "Run Log" tab (create it with a header row if missing). Columns: A Date, B Companies added, C Directory rows (first-last), D Scored, E Tier 1/2/3/Excluded counts for this run, F Notes/problems, G Unfinished / follow-up for next run. In F also state: how many previously unfinished companies you completed, and how many of this run's companies got a LinkedIn page (found / total). In G list every company or field still unfinished so the next run completes it first (leave "Nothing half-finished" if none). Put "Re-check later" items for the user in G under that label.

FINAL OUTPUT
Reply with: how many previously unfinished companies completed, how many new companies added and scored, the Directory row range, tier counts for the new vendors, LinkedIn found/total, and any problems (connector drops, blocked sites, doubtful identities). Do not send any email or message to anyone.
