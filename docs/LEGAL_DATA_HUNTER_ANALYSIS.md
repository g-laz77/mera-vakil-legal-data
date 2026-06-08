# Legal Data Hunter — Analysis for Mera Vakil AI
**Date**: 26 May 2026

## CRITICAL FINDING: AWS OPEN DATA FOR INDIAN JUDGMENTS
Supreme Court and High Court judgments are free public AWS Open Data:
- SC: s3://indian-supreme-court-judgments — 35K judgments, 52 GB, CC-BY-4.0
- HC: s3://indian-high-court-judgments — 16.7M judgments, 1.11 TB, CC-BY-4.0
**No need for Indian Kanoon API for case law.**

## INDIA CODE SCRAPER COMPARISON
LDH's IndiaCode scraper uses the same AJAX approach but is partially broken.
Our scraper: 1,834 sections, 99.95% success — more complete than LDH.

## KEY TAKEAWAYS
1. AWS Open Data replaces Indian Kanoon for case law (free, CC-BY-4.0)
2. Our India Code scraper outperforms LDH's
3. LDH provides reference architecture (MCP tools, hybrid search, source configs)
4. 40 additional Indian sources identified for future expansion
5. llms.txt pattern recommended for AI agent self-documentation