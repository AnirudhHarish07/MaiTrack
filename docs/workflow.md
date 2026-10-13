# CRO vendor scoring workflow (Asia: PK / ADA / toxicology)

Single working file: Google Sheet "CRO Vendor Scorecard"
(id `1J7G3_EVmlChUVFQJCAzMfmU5rHBEiODX0rNT9L81vQU`).

## Tabs
| Tab | Purpose |
|---|---|
| Legend & Rubric | Rubric text, tier bands, "Insufficient Data" rules, workflow notes (A62:A67) |
| CRO Directory | One row per company found. Cols: A name, B HQ, C type, D services, E verified, F LinkedIn, G source URL, H date added, I fully scored (Y/N), J region, K hard-gate status, L scoring status, M conference presence, N evidence by criterion, O criteria still missing, P flags for scorer, Q research basis |
| Company Details | One row per Directory row (row number = Directory row). A name, B directory row, C phone, D email, E LinkedIn, F HQ address, G site address, H website, I source URLs, J date accessed, K notes |
| Scorecard | One row per scored vendor (rows 5+; row 4 is an example). Inputs: A name, B country/city, C hard gate Y/N, D-G, I-L, N-O, Q-R, T-V, X-Y scores, AA location tier. Formulas (do not overwrite): H, M, P, S, W, Z, AB-AE. Formulas are pre-filled down to row 300 |
| Sources & Evidence Log | One row per scored criterion: vendor, sub-criterion, score, source type, source URL, specific fact, date accessed (text, leading apostrophe), confidence note |

## Order of work for every new CRO
1. Add to CRO Directory (name, HQ, type, services, LinkedIn, source URL, date added, region, conference presence).
2. Fill Company Details for the same row (public company-level contact data only).
3. Score on the Scorecard, write evidence rows, then update Directory cols I, K, L.

## Rules that matter
- "Insufficient Data" is not 0. Use 0 only when evidence shows a genuine zero.
- Only real regulator inspections count for Regulatory Inspection History; certification audits do not.
- Vendor-only claims about regulatory outcomes, data integrity, pricing or turnaround are not scored.
- Never copy facts from a similarly named entity. If identity is doubtful, say so and skip.
- Hard gate N = no valid GLP, unresolved major regulatory finding, or refuses CDA, or not a third-party contract vendor. Outside Asia = excluded (do not add).
- Tiers: >=75 Tier 1, 50-74 Tier 2, 30-49 Tier 3, else Excluded.
- Contact data: company level only. No personal names, emails or mobiles. Never invent values.

## Google Sheets write hazards
- Values are written USER_ENTERED. Any text starting with + - = @ is parsed as a formula or number. Prefix phone numbers and dates with an apostrophe (`'+86 21 ...`, `'2026-10-04`).
- `null` cells are skipped by update_values. Use "" to blank a cell.
- Hand-typed \uXXXX escapes can produce wrong CJK characters. Copy names from the source text and read them back.
- The Sheets connection can drop mid-run. Write in blocks and note progress so the next run can resume.

## Scripts and briefs in this repo
- `briefs/` are the instructions given to helper agents (scoring, gap-fill + contact details, contact details only).
- `scripts/merge_gapfill.py` merges helper outputs (`out/*.json`) into sheet updates; `scripts/make_evidence_rows.py` builds Directory status and evidence rows from per-vendor score files. They expect the working-folder layout used in the original session (`in/`, `out/`, `scores/`), so treat them as reference.
