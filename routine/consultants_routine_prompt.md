You are running an automated discovery project in Google Sheets: independent consultants in the Asia region who specialise in ADA (anti-drug antibody / immunogenicity), PK (pharmacokinetics / bioanalysis) and toxicology. Each run you (1) first finish anything the previous run left unfinished, then (2) add new consultants until the day's total is about 15, with every entry researched by one helper and independently verified by a second helper before it is written. Use the Google Sheets and Google Drive connectors. Do not create new files; work only in the existing Google Sheet named "Consultancies" (Drive file id 1OxAzylrqfd8hGkiOJ_A-k5WgNuaoI1mG8DIfJk8Yjv4). If a repo is checked out, docs/workflow.md has the shared sheet-writing rules. Do not use or edit the "CRO Vendor Scorecard" sheet.

SHEET LAYOUT
The data tab is "Sheet1". Existing columns: A Name, B Type (Consultant / Company), C Country, D City, E Specialisation (ADA / Toxicology / PK), F Services, G Website, H Contact, I Source URL, J Date Added, K Notes.
On the first run only, add these header cells to the RIGHT of the existing headers (never change columns A-K): L LinkedIn URL, M Verified (Y/N), N Verification notes. Create a tab "Run Log" with the header: Date, Entries added, Rows (first-last), Notes/problems, Unfinished / follow-up for next run.

START OF EVERY RUN: FINISH WHAT IS UNFINISHED FIRST
1. Read the last rows of the "Run Log" tab, especially the column "Unfinished / follow-up for next run". Also scan Sheet1 for rows added by earlier runs where column M (Verified) is empty, or column L (LinkedIn) is empty and column K does not say "LinkedIn searched on Google, not found".
2. Complete those entries first with the same research, verification and writing steps as for new ones. For these rows fill only EMPTY cells. Never overwrite a cell that already has a value.
3. Items listed under "Re-check later" are flags for the user, not unfinished work. Do not touch them.
4. Entries you finish from the previous run count toward the day's 15. Then add new entries until the total handled this run is about 15. Quality over count: if you cannot find 15 well-evidenced consultants, add fewer and say so in the Run Log. Never pad with weak or unverifiable entries.
5. Log how many previously unfinished entries you completed.

SCOPE
- Independent consultants (individuals, or one-person / small boutique consultancies) based in Asia (China, India, Japan, South Korea, Taiwan, SE Asia, other Asia incl. Israel/Central/West Asia) who offer consulting in at least one of: ADA/immunogenicity assessment, PK/TK/bioanalysis, nonclinical toxicology/safety assessment. Type = "Consultant" for an individual, "Company" for a small independent consultancy. Skip consultants based outside Asia, and skip large CROs and large consulting firms (CROs belong in the CRO Vendor Scorecard project).
- An entry needs evidence of BOTH the specialisation (for example a professional bio, services page, publications, conference talks, regulatory-agency expert listings) AND that the person or firm offers independent consulting. Employees of a CRO or pharma company who do not advertise independent consulting are not independent consultants: skip them.
- Before adding, read all of Sheet1 and skip anyone already listed, including name variants, transliterations and the same person listed under their consultancy's name.
- Find candidates from Google search, consultant directories and expert networks, conference speaker lists (AAPS, WRIB, EBF, SOT, EUROTOX, JSOT/KSOT/CSOT, BioAsia, CPHI), PubMed author affiliations, regulatory-agency expert pages, company websites, and Google search results.
- If the session limit or a connector failure stops you early, stop cleanly and log exactly which entries and fields are unfinished.

PRIVACY RULES (people, not companies)
- Record only professional information that the person or firm publishes themselves for business purposes or that appears in a professional listing: name, specialisation, services, location (country and city only), professional website, a business contact the person publishes for consulting enquiries, and their professional LinkedIn profile URL.
- Do NOT record home addresses, personal mobile numbers, personal email addresses unless the person publishes that address as their consulting contact, age, family, health, political or any other personal details. Do not infer or guess contact details.
- Use a business-contact form or website instead if no public business email or phone is published.

LINKEDIN FOR EVERY ENTRY (required)
- For every entry, search Google for the LinkedIn profile or company page, for example: site:linkedin.com/in "<name>" <specialisation or employer>, or site:linkedin.com/company "<firm name>". Try the local-language name and the city if the first search finds nothing. No LinkedIn connector is available and you must not log in to LinkedIn or try to defeat its anti-bot; use only what appears in search results.
- Record the URL in column L. Accept a result only if it matches the person or firm on name AND at least two of: location, specialisation/headline, current or former organisation, website. Never record a LinkedIn URL for a different person with a similar name.
- If nothing matches, leave L blank and write "LinkedIn searched on Google, not found" in column K. Do not guess a URL.
- The verifier rechecks every LinkedIn URL for identity.

APPEND-ONLY (hard rule)
- New entries go AFTER the existing data: new rows below the last used row of Sheet1.
- Never edit, reorder, sort, move, delete or overwrite any existing row or cell. The only exceptions are the one-time header cells in L-N, and filling EMPTY cells of a half-finished row from a previous run as described above.
- If an existing entry looks wrong, do not fix it: add a line to the Run Log notes for the user.
- Before each write, read the target range and confirm it is empty.

TWO-STEP WORK: RESEARCHER THEN VERIFIER (use the Agent tool for helpers)
- Step 1, researcher helpers: each takes a few candidates and writes ONE JSON file per entry in a scratch folder with the proposed values for columns A-N, plus for each field the source URL and a one-line evidence note. Researchers do NOT write to the sheet.
- Step 2, verifier helper(s), a different agent from the researcher: for every entry, independently re-open the cited sources (curl via the proxy, or search) and judge each item: (a) is this a real, identifiable person or firm and the right one, not someone with a similar name; (b) does the source really show the stated specialisation (ADA, PK, toxicology) and independent consulting; (c) is the person/firm based in Asia, in the stated country and city; (d) do the website and business contact match a source the person or firm publishes; (e) does the LinkedIn URL match; (f) was any personal information recorded that the privacy rules forbid. The verifier returns per item: verified / corrected (with the corrected value) / rejected, plus a short reason.
- Only verified or corrected items are written. Rejected fields are left blank; column N says what was rejected and why. An entry whose identity or specialisation cannot be verified is not added; list it in the Run Log.
- Set M to "Y" for fully verified entries, "N" if some fields were rejected. Column N records "researched and independently verified <date>" plus any rejections.

WRITING EACH VERIFIED ENTRY
Append at the first empty row below the existing data. A name (as the person publishes it; for non-Latin names "Native name (English name)"), B Type, C Country, D City, E Specialisation (only values supported by evidence: ADA, PK, Toxicology, separated by "; "), F Services (short, factual), G Website, H Contact (business contact only, e.g. "Email: ...; Phone: ..."), I Source URLs (newline separated), J Date Added (text with a leading apostrophe, e.g. '2026-10-16), K Notes (caveats, "LinkedIn searched on Google, not found", independence caveats), L LinkedIn URL, M Verified, N Verification notes.

SHEET WRITE RULES
- Write with USER_ENTERED values. Text beginning with + - = @ is treated as a formula or number: put an apostrophe in front of every phone number and every date text.
- null cells are skipped by update_values; use "" to blank a cell. Write in blocks of a few entries at a time, and read back a sample of rows after writing.
- Copy non-Latin names exactly from the source text; do not type \uXXXX escapes by hand.
- Never delete rows or tabs.
- WebFetch may be blocked; fetch specific public pages with curl through the configured proxy. Never disable TLS verification, never unset the proxy.
- If the Sheets/Drive connection drops, reload the tools (ToolSearch) and continue; if it cannot be restored, stop and log.

RUN LOG
At the end append one row to the "Run Log" tab: Date; Entries added; Rows (first-last); Notes/problems (include how many previously unfinished entries you completed, how many of this run's entries got a LinkedIn URL (found / total), and anything rejected or skipped as doubtful); Unfinished / follow-up for next run (every entry or field still unfinished, or "Nothing half-finished"; put "Re-check later" items for the user here under that label).

FINAL OUTPUT
Reply with: previously unfinished entries completed, new entries added, the row range, LinkedIn found/total, and any problems (connector drops, blocked sites, doubtful identities). Do not send any email or message to anyone, and do not contact any of the people listed.
