# Mera Vakil AI — Indian Legal Data Hub

**Mera Vakil** (Meravakil Ai Solutions Pvt Ltd) is building India's multilingual AI legal assistant.

This repository contains the complete legal data extraction pipeline:

## What's Inside

| Directory | Contents |
|-----------|----------|
| `docs/` | Project documentation, master plan, extraction tracker, meeting prep |
| `schemas/` | Knowledge base schema, IPC→BNS mappings, handle maps |
| `scripts/` | India Code scraper, handle finder, report builder |
| `scraped_acts/` | 13 current acts scraped from India Code + Constitution (JSON) |
| `civictech_datasets/` | 8 legacy acts from civictech-India open source (JSON) |
| `reports/` | HTML and DOCX data reports |

## Key Stats

- **21 Indian laws** collected (13 current + 8 legacy)
- **3,610+ legal sections** 
- **132 old→new law mappings** (IPC→BNS, CrPC→BNSS, IEA→BSA)
- **₹0 data acquisition cost**
- **99.95% scraping success rate**

## Data Sources

| Source | Type | Status |
|--------|------|--------|
| India Code (indiacode.nic.in) | Central Acts | 12 acts scraped |
| GitHub (Vikhram-S/IndianConstitution-js) | Constitution | Extracted |
| civictech-India (GitHub) | Legacy Acts | 8 acts downloaded |
| AWS Open Data | SC/HC Judgments | Available (Phase 2) |

## Quick Start

```bash
# Install dependencies
pip install requests beautifulsoup4 lxml

# Run scraper
python scripts/india_code_scraper.py

# Find handles for missing acts
python scripts/find_handles.py

# Build DOCX report
node scripts/build_report.cjs
```

## License

This repository contains public legal data sourced from the Government of India.
Data license: CC-BY-4.0 where applicable. Code: MIT.

---
*Part of the Mera Vakil AI project — making Indian law accessible to everyone.*
