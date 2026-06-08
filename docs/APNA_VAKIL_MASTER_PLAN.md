# Apna Vakil AI — Project Master Plan
**Date**: 24 April 2026  
**Client**: Sara Vaisoha  
**Status**: Data Acquisition COMPLETE | Pre-PoC Phase  

---

## 1. SITUATION SUMMARY

### Where We Stand
- ✅ Solution Overview document created and shared with Sara (Google Doc, v1.0)
- ✅ Sara reviewed the doc — "everything looks great, minor additions to be added"
- ✅ Sara validated the concept with her staff — strong positive response, especially DV use case
- ✅ Sara is working on trademark registration (expected completion this week)
- ✅ Sara is brainstorming marketing plan
- ✅ **Manupatra declined** — alternative data sourcing strategy CONFIRMED & EXECUTED
- ✅ **India Code scraping FEASIBILITY CONFIRMED & FULLY EXECUTED** — 12 acts scraped (1,834 sections)
- ✅ **Indian Kanoon API** — documented, pricing confirmed (₹10K/month free for non-commercial)
- ✅ **civictech-India datasets downloaded** — 8 old laws in JSON + SQLite
- ✅ **IPC→BNS mapping table built** — 80+ section mappings
- ✅ **Knowledge base schema designed** — unified v1.0 schema
- ⏳ Sara wants to schedule next call — needs email response
- ⏳ Sara wants to add more topics — need to ask what they are
- ⏳ BSA (Bharatiya Sakshya Adhiniyam) not on India Code — need alternative source

### Key Decisions Still Needed with Sara
1. **Pilot state** for state-specific laws (she asked "can we do all at once?")
2. **Verified Information Layer** — budget for lawyer review
3. **Backend conversation notes** — anonymized analytics vs detailed tracking
4. **Minor additions** — what topics is she adding?
5. **Name clarification** — she mentioned "Mera Vakil" in last message

---

## 2. LEGAL DATA ACQUISITION — COMPLETE ✅

### Acts Scraped from India Code (12 acts, 1,834 sections, 5.5MB)

| Act | Sections | Content | Footnotes | Errors | Avg Chars/Section |
|-----|----------|---------|-----------|--------|-------------------|
| Bharatiya Nyaya Sanhita (BNS) 2023 | 358 | 357 ✅ | 1 | 1 | 938 |
| Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023 | 531 | 531 ✅ | 1 | 0 | 1,013 |
| Consumer Protection Act 2019 | 107 | 107 ✅ | 2 | 0 | 1,134 |
| Code on Social Security 2020 | 164 | 164 ✅ | 1 | 0 | 2,049 |
| Industrial Relations Code 2020 | 104 | 104 ✅ | 1 | 0 | 1,695 |
| Occupational Safety & Health Code 2020 | 143 | 143 ✅ | 1 | 0 | 1,731 |
| Code on Wages 2019 | 69 | 69 ✅ | 1 | 0 | 1,314 |
| Protection of Women from DV Act 2005 | 37 | 37 ✅ | 1 | 0 | 906 |
| POCSO Act 2012 | 47 | 47 ✅ | 12 | 0 | 952 |
| POSH Act 2013 | 30 | 30 ✅ | 4 | 0 | 1,139 |
| RTI Act 2005 | 31 | 31 ✅ | 4 | 0 | 1,989 |
| Dowry Prohibition Act 1961 | 13 | 13 ✅ | 11 | 0 | 919 |

**Data quality: 99.95% success rate** (1 error out of 1,834 sections)

### India Code Handle Map (for future re-scraping)
| Act | Handle ID |
|-----|-----------|
| BNS 2023 | 21420 |
| BNSS 2023 | 21419 |
| Consumer Protection Act 2019 | 21423 |
| DV Act 2005 | 12904 |
| POCSO Act 2012 | 12903 |
| POSH Act 2013 | 20037 |
| RTI Act 2005 | 17520 |
| Dowry Prohibition Act 1961 | 12822 |
| Code on Wages 2019 | 22075 |
| Code on Social Security 2020 | 22074 |
| Industrial Relations Code 2020 | 22078 |
| OSH Code 2020 | 22057 |

### civictech-India Datasets (Downloaded)
| File | Act | Size |
|------|-----|------|
| ipc.json | Indian Penal Code 1860 | 328 KB |
| crpc.json | Code of Criminal Procedure 1973 | 566 KB |
| iea.json | Indian Evidence Act 1872 | 111 KB |
| cpc.json | Civil Procedure Code 1908 | 162 KB |
| hma.json | Hindu Marriage Act 1955 | 31 KB |
| ida.json | Indian Divorce Act 1869 | 42 KB |
| nia.json | Negotiable Instruments Act 1881 | 89 KB |
| MVA.json | Motor Vehicles Act 1988 | 417 KB |
| IndiaLaw.db | All 8 acts in SQLite | 1.9 MB |

### IPC→BNS Mapping Table (Built)
- 60+ IPC→BNS section mappings
- 40+ CrPC→BNSS section mappings  
- 30+ IEA→BSA section mappings
- Includes mapping type (direct, restructured, new, repealed, partial)

### Knowledge Base Schema (Designed)
- Unified JSON schema v1.0
- Supports: act metadata, sections with content/footnotes, old law mappings, keywords, categories, related sections, simplified explanations, verification status
- Ready for RAG pipeline ingestion

### BSA — Still Needed
- Bharatiya Sakshya Adhiniyam (170 sections) not fully available on India Code
- Will source from IndiaLawActs.in or BNS section datasets
- Priority for next sprint
