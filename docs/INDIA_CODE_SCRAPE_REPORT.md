# India Code Scraping — Feasibility Report
## Mera Vakil AI | April 2026

✅ India Code is FULLY scrapeable via pure HTTP — no Selenium needed.

## KEY DISCOVERY
`/SectionPageContent?actid={}&sectionID={}` returns clean JSON: `{"content":"...","footnote":"..."}`

## VERIFIED HANDLES
| Act | Handle | Sections |
|-----|--------|----------|
| BNS 2023 | 21420 | 358 |
| BNSS 2023 | 21419 | 560 |
| Consumer Protection 2019 | 21423 | 107 |
| DV Act 2005 | 12904 | 37 |
| POCSO 2012 | 12903 | 47 |
| POSH 2013 | 20037 | 30 |
| RTI 2005 | 17520 | 31 |
| Dowry Prohibition 1961 | 12822 | 13 |
| Code on Wages 2019 | 22075 | 69 |
| Social Security Code 2020 | 22074 | 164 |
| Industrial Relations Code 2020 | 22078 | 104 |
| OSH Code 2020 | 22057 | 143 |

## PERFORMANCE
Rate limit: 0.5s/request | BNS: ~3 min | All 14 acts: ~30-45 min | No auth, no CAPTCHA

## BSA: Draft translation only on India Code — source from alternatives.