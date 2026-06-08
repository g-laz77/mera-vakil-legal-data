"""
Batch handle finder for missing acts in Mera Vakil tracker.
Uses India Code simple-search to find handle IDs for all 71 missing acts.
"""
import sys
sys.path.insert(0, '.')
from india_code_scraper import find_act_handle

# Sara's High Priority acts to find first
HIGH_PRIORITY = [
    "Citizenship Act 1955",
    "Passports Act 1967",
    "Representation of the People Act 1950",
    "Aadhaar Act 2016",
    "Protection of Human Rights Act 1993",
    "Digital Personal Data Protection Act 2023",
    "Narcotic Drugs and Psychotropic Substances Act 1985",
    "Indian Contract Act 1872",
    "Specific Relief Act 1963",
    "Indian Stamp Act 1899",
]

for act_name in HIGH_PRIORITY:
    print(f"\nSearching: {act_name}")
    handle = find_act_handle(act_name)
    print(f"  Result: {handle}")
