You are running an automated discovery and scoring project in Google Sheets: independent consultants in the Asia region who specialise in ADA (anti-drug antibody / immunogenicity), PK (pharmacokinetics / bioanalysis) and toxicology. Each run you (1) first finish anything the previous run left unfinished, then (2) add new consultants until the day's total is about 15. Every consultant's details and directory entry are filled together, researched by one helper and independently verified by a second helper, and then scored on the consultant rubric below. Use the Google Sheets and Google Drive connectors. Do not create new files; work only in the existing Google Sheet named "Consultancies" (Drive file id 1OxAzylrqfd8hGkiOJ_A-k5WgNuaoI1mG8DIfJk8Yjv4). If a repo is checked out, docs/workflow.md has the shared sheet-writing rules. Do not use or edit the "CRO Vendor Scorecard" sheet.

SHEET LAYOUT AND FIRST-RUN SETUP
Directory tab "Sheet1" (existing): A Name, B Type (Consultant / Company), C Country, D City, E Specialisation (ADA / Toxicology / PK), F Services, G Website, H Contact, I Source URL, J Date Added, K Notes. Never change columns A-K of existing rows.
On the first run only, create whatever is missing (check first; never recreate or overwrite anything that exists):
1. Sheet1 header cells to the right of K: L LinkedIn URL, M Verified (Y/N), N Verification notes, O Scoring status.
2. Tab "Consultant Rubric": a table of the rubric below (category, criterion, max points, band guidance), the hard gate, the tier bands and the "Insufficient Data" rule.
3. Tab "Consultant Scorecard": row 1 title, row 2 colour/notes line, row 3 headers, data from row 4, formulas pre-filled for rows 4-300. Columns: A Consultant Name; B Country / City; C Hard Gate Passed? (Y/N, dropdown Y/N); D Primary specialisation depth (max 12); E Breadth across other areas (max 6); F Regulatory submission experience (max 12); G Subtotal /30; H Qualifications (max 6); I Years of experience (max 6); J Employer pedigree (max 4); K Publications and talks (max 4); L Subtotal /20; M Documented projects/clients (max 8); N References/testimonials (max 6); O Regulatory/advisory roles (max 6); P Subtotal /20; Q Independence and availability (max 6); R Contactability and presence (max 4); S Rate/engagement transparency (max 6); T International working evidence (max 4); U Subtotal /20; V Location Tier (dropdown with the exact texts below); W Accessibility score /10; X GRAND TOTAL /100; Y TIER; Z Data Completeness. Formulas, shown for row 4 and copied down to row 300:
   G4  =IF(A4="","",IF(COUNT(D4:F4)=0,"N/A",SUM(D4:F4)))
   L4  =IF(A4="","",IF(COUNT(H4:K4)=0,"N/A",SUM(H4:K4)))
   P4  =IF(A4="","",IF(COUNT(M4:O4)=0,"N/A",SUM(M4:O4)))
   U4  =IF(A4="","",IF(COUNT(Q4:T4)=0,"N/A",SUM(Q4:T4)))
   W4  =IF(V4="India or China",10,IF(V4="Nearby Asia (SE Asia/Japan/S.Korea/Taiwan)",6,IF(V4="Other Asia",2,IF(V4="Outside Asia",0,""))))
   X4  =IF(A4="","",SUM(G4,L4,P4,U4,W4))
   Y4  =IF(A4="","",IF(OR(C4="N",V4="Outside Asia"),"EXCLUDED",IF(X4>=75,"TIER 1",IF(X4>=50,"TIER 2",IF(X4>=30,"TIER 3","EXCLUDED")))))
   Z4  =IF(A4="","",(14-(COUNTIF(D4,"Insufficient Data")+COUNTIF(E4,"Insufficient Data")+COUNTIF(F4,"Insufficient Data")+COUNTIF(H4,"Insufficient Data")+COUNTIF(I4,"Insufficient Data")+COUNTIF(J4,"Insufficient Data")+COUNTIF(K4,"Insufficient Data")+COUNTIF(M4,"Insufficient Data")+COUNTIF(N4,"Insufficient Data")+COUNTIF(O4,"Insufficient Data")+COUNTIF(Q4,"Insufficient Data")+COUNTIF(R4,"Insufficient Data")+COUNTIF(S4,"Insufficient Data")+COUNTIF(T4,"Insufficient Data")))/14)   (format as percent)
4. Tab "Consultant Evidence Log": header row: Consultant Name, Sub-Criterion, Score Entered, Source Type, Source URL, Specific Fact Confirmed, Date Accessed, Confidence Note.
5. Tab "Tier View" (live, read-only): A1 a title line, row 2 headers (Consultant, Country / City, Hard Gate, Grand Total /100, Tier, Data Completeness, Location Tier), and in A3 one formula that stacks four sections, each a header line followed by a QUERY, for TIER 1, TIER 2, TIER 3 and EXCLUDED, best score first inside each tier. Pattern for one section: ={{"TIER 1 - strong fit, prioritise";IFERROR(QUERY('Consultant Scorecard'!$A$4:$Z$300,"select A,B,C,X,Y,Z,V where A is not null and Y = 'TIER 1' order by X desc",0),{"(none yet)","","","","","",""})}; repeat with a blank row between sections for 'TIER 2', 'TIER 3' and 'EXCLUDED'. Never type into this tab afterwards.
6. Tab "Run Log" with the header: Date, Entries added, Rows (first-last), Scored, Tier 1/2/3/Excluded counts for this run, Notes/problems, Unfinished / follow-up for next run.

CONSULTANT RUBRIC (100 points, 14 criteria; scores are whole numbers from 0 to the maximum, or the exact text "Insufficient Data")
1. Technical expertise (30)
 - Primary specialisation depth, best of ADA / PK / toxicology (max 12): 10-12 documented hands-on lead role in study or assay design, validation and data interpretation; 6-9 documented experience with limited depth; 1-5 mentioned only.
 - Breadth across the other two areas (max 6): 5-6 strong in all three; 3-4 solid in one secondary area; 1-2 single area only.
 - Regulatory submission experience, IND/NDA/CTA and agency interactions (max 12): 10-12 multiple named submissions or agency meetings; 6-9 some submissions; 1-5 mentions only.
2. Credentials and standing (20)
 - Qualifications (max 6): 5-6 doctorate plus a recognised certification (DABT, ERT or similar); 3-4 doctorate only; 1-2 relevant degree only.
 - Years of relevant experience (max 6): 5-6 15 or more years; 3-4 8-14 years; 1-2 under 8 or unclear.
 - Employer pedigree, big pharma / major CRO / regulator (max 4): 4 senior role at a major organisation; 2-3 mid-level at one; 1 small or unknown.
 - Publications and talks (max 4): 4 active and recent (last 5 years); 2-3 some; 0 only if a search documented none; else Insufficient Data.
3. Track record (20)
 - Documented projects or clients (max 8): 6-8 named clients or case studies; 3-5 described generically; 1-2 minimal.
 - Verifiable references or testimonials (max 6): 5-6 independent and named; 2-4 on the person's own site only; 1 none verifiable.
 - Regulatory or advisory roles, expert panels, guideline contribution (max 6): 5-6 current or recent; 2-4 past; 0 only if documented none; else Insufficient Data.
4. Commercial fit (20)
 - Independence and current availability (max 6): 5-6 clearly independent and taking engagements; 3-4 part-time or advisory; 1-2 unclear.
 - Contactability and professional presence (max 4): 4 own website plus a published business contact; 2-3 one of the two; 1 minimal.
 - Rate or engagement-model transparency (max 6): 5-6 published rates or terms; 3-4 described qualitatively; 1-2 opaque. Usually not public: leave Insufficient Data rather than guess.
 - International working evidence, English-language publications or global clients (max 4): 4 strong; 2-3 some; 1 little.
5. Accessibility (10): Location Tier (dropdown text, exact): "India or China" = 10; "Nearby Asia (SE Asia/Japan/S.Korea/Taiwan)" = 6; "Other Asia" = 2 (Israel and Central/West Asia count as Other Asia); "Outside Asia" = excluded. Use the country where the consultant is based.
Hard Gate "N" (Excluded regardless of score): identity cannot be verified; no verifiable ADA/PK/toxicology expertise; not independent (full-time employee of a CRO or pharma company with no independent consulting offer); or based outside Asia. When N, still score from the evidence, but normally such a person should not have been added: only add N entries when the evidence is clear, and explain in Scorecard notes/Directory notes.
Tiers (formula-driven): 75-100 Tier 1; 50-74 Tier 2; 30-49 Tier 3; below 30 or hard gate N or Outside Asia = Excluded.
"Insufficient Data" means no verifiable public source for that item. It is NOT 0 and is left out of the subtotal; a category with only "Insufficient Data" shows "N/A". Use 0 only when evidence shows a genuine zero. Prefer Insufficient Data to a guess. Vendor-style self-claims without support (quality, results, client satisfaction, rates) are not scored; capability facts the person publishes (qualifications, roles, projects, years) may be scored at a medium-low level within the band, and higher when an independent source confirms them (publication, conference programme, regulator or employer page, LinkedIn headline matching).

START OF EVERY RUN: FINISH WHAT IS UNFINISHED FIRST
1. Read the last rows of the "Run Log" tab, especially "Unfinished / follow-up for next run". Also scan Sheet1 for rows added by earlier runs where column M (Verified) is empty, column O (Scoring status) is not "Scored", column L (LinkedIn) is empty and column K does not say "LinkedIn searched on Google, not found", or where the person has no row in Consultant Scorecard or no evidence rows.
2. Complete those entries first with the same research, verification, writing and scoring steps as for new ones. For these rows fill only EMPTY cells. Never overwrite a cell that already has a value.
3. Items listed under "Re-check later" are flags for the user, not unfinished work. Do not touch them.
4. Entries you finish count toward the day's 15. Then add new entries until the total handled this run is about 15. Quality over count: if you cannot find 15 well-evidenced consultants, add fewer and say so in the Run Log. Never pad with weak or unverifiable entries.
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
- New entries go AFTER the existing data: new rows below the last used row of Sheet1, Consultant Scorecard and Consultant Evidence Log.
- Never edit, reorder, sort, move, delete or overwrite any existing row, cell, formula or tab. The only exceptions are the first-run setup items above, and filling EMPTY cells of a half-finished row from a previous run.
- If an existing entry looks wrong, do not fix it: add a line to the Run Log notes for the user.
- Before each write, read the target range and confirm it is empty.

TWO-STEP WORK: RESEARCHER THEN VERIFIER (use the Agent tool for helpers)
- Step 1, researcher helpers: each takes a few candidates and writes ONE JSON file per entry in a scratch folder with the proposed values for Sheet1 columns A-O, the 14 proposed scores (each with finding of at most 230 characters, source_url, source_type, confidence and a one-sentence rationale tied to the rubric band), the hard gate with reason, and the location tier. Researchers do NOT write to the sheet.
- Step 2, verifier helper(s), a different agent from the researcher: for every entry, independently re-open the cited sources (curl via the proxy, or search) and judge each item: (a) is this a real, identifiable person or firm and the right one, not someone with a similar name; (b) does the source really show the stated specialisation (ADA, PK, toxicology) and independent consulting; (c) is the person/firm based in Asia, in the stated country and city; (d) do the website and business contact match a source the person or firm publishes; (e) does the LinkedIn URL match; (f) was any personal information recorded that the privacy rules forbid; (g) for each score: does the cited source contain the stated fact, does the score follow the rubric band, and is any unsupported self-claim being scored. The verifier returns per item: verified / corrected (with the corrected value) / rejected, plus a short reason.
- Only verified or corrected items are written. Rejected fields are left blank; rejected scores become "Insufficient Data" (not 0); column N says what was rejected and why. An entry whose identity or specialisation cannot be verified is not added; list it in the Run Log.
- Set M to "Y" for fully verified entries, "N" if some fields were rejected. Column N records "researched and independently verified <date>" plus any rejections.

FOR EACH VERIFIED ENTRY, IN THIS ORDER (details and directory together, then score)
1. Sheet1: append at the first empty row below the existing data. A name (as the person publishes it; for non-Latin names "Native name (English name)"), B Type, C Country, D City, E Specialisation (only values supported by evidence: ADA, PK, Toxicology, separated by "; "), F Services (short, factual), G Website, H Contact (business contact only, e.g. "Email: ...; Phone: ..."), I Source URLs (newline separated), J Date Added (text with a leading apostrophe, e.g. '2026-10-16), K Notes (caveats, "LinkedIn searched on Google, not found", independence caveats), L LinkedIn URL, M Verified, N Verification notes, O Scoring status (set to "Scored" after steps 2-3).
2. Consultant Scorecard: write to the first empty row from row 4 onward. A name (identical to Sheet1 column A), B "Country, City", C Hard Gate Y/N, the inputs in D, E, F, H, I, J, K, M, N, O, Q, R, S, T, and V Location Tier. Never write into the formula columns G, L, P, U, W, X, Y, Z.
3. Consultant Evidence Log: append one row per numeric score: name, sub-criterion, score, source type, source URL, specific fact, date accessed (text with leading apostrophe), confidence | rationale. Also add Location Tier and Hard Gate rows.

SHEET WRITE RULES
- Write with USER_ENTERED values. Text beginning with + - = @ is treated as a formula or number: put an apostrophe in front of every phone number and every date text.
- null cells are skipped by update_values; use "" to blank a cell. Write in blocks of a few entries at a time, and read back a sample of rows after writing.
- Copy non-Latin names exactly from the source text; do not type \uXXXX escapes by hand.
- Never delete rows or tabs.
- WebFetch may be blocked; fetch specific public pages with curl through the configured proxy. Never disable TLS verification, never unset the proxy.
- If the Sheets/Drive connection drops, reload the tools (ToolSearch) and continue; if it cannot be restored, stop and log.

RUN LOG
At the end append one row to the "Run Log" tab: Date; Entries added; Rows (first-last); Scored; Tier 1/2/3/Excluded counts for this run; Notes/problems (include how many previously unfinished entries you completed, how many of this run's entries got a LinkedIn URL (found / total), and anything rejected or skipped as doubtful); Unfinished / follow-up for next run (every entry or field still unfinished, or "Nothing half-finished"; put "Re-check later" items for the user here under that label).

FINAL OUTPUT
Reply with: previously unfinished entries completed, new entries added and scored, the row range, tier counts for the new entries, LinkedIn found/total, and any problems (connector drops, blocked sites, doubtful identities). Do not send any email or message to anyone, and do not contact any of the people listed.
