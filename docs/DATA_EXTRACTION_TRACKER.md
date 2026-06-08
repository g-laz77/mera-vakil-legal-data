# Apna Vakil AI — Internal Data Extraction Tracker
**Created**: 26 May 2026 | **Last Updated**: 26 May 2026 13:20 UTC
**Status**: AWAITING GOOGLE CONNECTION (to access Sara's tracker sheet + Gemini notes)

---

## HOW TO USE THIS TRACKER

- **Status**: ✅ Complete | 🔄 In Progress | ⬜ Pending | ⚠️ Blocked | ❌ Not Applicable
- **Priority**: P1 (critical for PoC) | P2 (important) | P3 (nice to have)
- Each data point has a unique ID for reference
- This is a living document — update status as extraction progresses

---

## SECTION A: STATUTE DATA (India Code — Central Acts)

### A.1 — Already Extracted ✅

| ID | Act | Source | Sections | KB-Normalized | Priority |
|----|-----|--------|----------|---------------|----------|
| A1.1 | Bharatiya Nyaya Sanhita (BNS) 2023 | India Code (21420) | 358 | ⬜ | P1 |
| A1.2 | Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023 | India Code (21419) | 531 | ⬜ | P1 |
| A1.3 | Consumer Protection Act 2019 | India Code (21423) | 107 | ⬜ | P1 |
| A1.4 | Code on Social Security 2020 | India Code (22074) | 164 | ⬜ | P2 |
| A1.5 | Industrial Relations Code 2020 | India Code (22078) | 104 | ⬜ | P2 |
| A1.6 | Occupational Safety & Health Code 2020 | India Code (22057) | 143 | ⬜ | P2 |
| A1.7 | Code on Wages 2019 | India Code (22075) | 69 | ⬜ | P2 |
| A1.8 | Protection of Women from DV Act 2005 | India Code (12904) | 37 | ⬜ | P1 |
| A1.9 | POCSO Act 2012 | India Code (12903) | 47 | ⬜ | P1 |
| A1.10 | POSH Act 2013 | India Code (20037) | 30 | ⬜ | P1 |
| A1.11 | RTI Act 2005 | India Code (17520) | 31 | ⬜ | P1 |
| A1.12 | Dowry Prohibition Act 1961 | India Code (12822) | 13 | ⬜ | P1 |

### A.2 — Still Needed (from Sara's tracker)

| ID | Act | Target Source | Est. Sections | Priority | Notes |
|----|-----|--------------|---------------|----------|-------|
| A2.1 | Constitution of India | GitHub (Vikhram-S) | 465 ✅ | P1 | **EXTRACTED** 26 May 2026 |
| A2.2 | Citizenship Act 1955 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.3 | Passports Act 1967 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.4 | Representation of the People Act 1950/51 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.5 | Aadhaar Act 2016 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.6 | Protection of Human Rights Act 1993 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.7 | DPDP Act 2023 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.8 | NDPS Act 1985 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.9 | Indian Contract Act 1872 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.10 | Specific Relief Act 1963 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.11 | Indian Stamp Act 1899 | legislative.gov.in | TBD | P1 | 🔄 SCGP |
| A2.12-71 | Remaining 60 acts | legislative.gov.in / India Code retry | TBD | P2-P3 | 🔄 SCGP |

**Note**: India Code (indiacode.nic.in) is returning HTTP 504 Gateway Timeout from this environment. Alternative source: legislative.gov.in is reachable. SCGP = Source Check In Progress.

---

## SECTION B: OLD LAW DATA (civictech-India / Alternative)

| ID | Act | Source | Sections | KB-Normalized | Priority |
|----|-----|--------|----------|---------------|----------|
| B1 | Indian Penal Code (IPC) 1860 | civictech (ipc.json) | N/A | ⬜ | P1 |
| B2 | Code of Criminal Procedure (CrPC) 1973 | civictech (crpc.json) | N/A | ⬜ | P1 |
| B3 | Indian Evidence Act (IEA) 1872 | civictech (iea.json) | N/A | ⬜ | P2 |
| B4 | Civil Procedure Code (CPC) 1908 | civictech (cpc.json) | N/A | ⬜ | P2 |
| B5 | Hindu Marriage Act 1955 | civictech (hma.json) | N/A | ⬜ | P3 |
| B6 | Indian Divorce Act 1869 | civictech (ida.json) | N/A | ⬜ | P3 |
| B7 | Negotiable Instruments Act 1881 | civictech (nia.json) | N/A | ⬜ | P3 |
| B8 | Motor Vehicles Act 1988 | civictech (MVA.json) | N/A | ⬜ | P3 |

---

## SECTION C: MAPPING DATA

| ID | Mapping | Status | Priority | Notes |
|----|---------|--------|----------|-------|
| C1 | IPC → BNS section mapping | ✅ 130+ done | P1 | HTML + JSON files exist |
| C2 | CrPC → BNSS section mapping | ⬜ pending | P1 | Partial in existing mapping |
| C3 | IEA → BSA section mapping | ⬜ pending | P1 | Need BSA data first |

---

## SECTION D: CASE LAW DATA

| ID | Source | Format | Status | Priority | Notes |
|----|--------|--------|--------|----------|-------|
| D1 | Supreme Court judgments (AWS) | Parquet + PDF | ⬜ | P2 | 35K judgments, 52 GB, free |
| D2 | High Court judgments (AWS) | JSON + PDF | ⬜ | P3 | 16.7M judgments, 1.11 TB |
| D3 | Indian Kanoon API | REST API | ⬜ | P2 | Need signup, ₹10K/month free tier |

---

## SECTION E: SUPPLEMENTARY DATA

| ID | Data Point | Source | Status | Priority |
|----|-----------|--------|--------|----------|
| E1 | Emergency contacts (Central) | Research | ⬜ | P1 |
| E2 | Emergency contacts (State-wise) | Research | ⬜ | P2 |
| E3 | Legal aid contacts | NALSA/DSLSA | ⬜ | P2 |
| E4 | Simplified explanations | Lawyer review | ⬜ | P1 |
| E5 | FAQs per topic | Content team | ⬜ | P1 |

---

## SECTION F: KNOWLEDGE BASE NORMALIZATION

| ID | Task | Status | Priority |
|----|------|--------|----------|
| F1 | Normalize BNS to KB schema | ⬜ | P1 |
| F2 | Normalize BNSS to KB schema | ⬜ | P1 |
| F3 | Normalize DV Act to KB schema | ⬜ | P1 |
| F4 | Normalize POCSO to KB schema | ⬜ | P1 |
| F5 | Normalize POSH to KB schema | ⬜ | P1 |
| F6 | Normalize RTI Act to KB schema | ⬜ | P1 |
| F7 | Normalize Dowry Act to KB schema | ⬜ | P1 |
| F8 | Normalize Consumer Protection Act to KB schema | ⬜ | P2 |
| F9 | Normalize 4 Labour Codes to KB schema | ⬜ | P3 |
| F10 | Normalize civictech old laws to KB schema | ⬜ | P2 |

---

## EXTRACTION PROGRESS SUMMARY

| Category | Total | Done | In Progress | Pending |
|----------|-------|------|-------------|---------|
| Central Acts (Statutes) | 14+ | 12 | 0 | 2+ |
| Old Laws | 8 | 8 | 0 | 0 |
| Mappings | 3 | 1 | 0 | 2 |
| Case Law | 3 | 0 | 0 | 3 |
| Supplementary | 5+ | 0 | 0 | 5+ |
| KB Normalization | 13 | 0 | 0 | 13 |
| Sara Questions | 8 | 0 | 0 | 8 |
