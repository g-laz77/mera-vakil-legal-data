"""
India Code Scraper for Mera Vakil AI
======================================
Uses India Code's hidden AJAX endpoint: /SectionPageContent?actid={}&sectionID={}
No Selenium needed — pure HTTP requests work perfectly.

Run: python scripts/india_code_scraper.py
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re

BASE_URL = "https://www.indiacode.nic.in"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}
AJAX_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}
RATE_LIMIT_SECONDS = 0.5


def clean_html(html_text):
    """Remove HTML tags and clean up text."""
    if not html_text:
        return ""
    soup = BeautifulSoup(html_text, 'lxml')
    text = soup.get_text(separator='\n')
    lines = [line.strip() for line in text.split('\n')]
    lines = [l for l in lines if l]
    return '\n'.join(lines)


def get_act_page(handle_id):
    """Fetch act page, extract metadata + section list."""
    url = f"{BASE_URL}/handle/123456789/{handle_id}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'lxml')
    
    # Extract act metadata
    act_meta = {}
    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) >= 2:
                key = cells[0].text.strip().rstrip(':')
                value = cells[1].text.strip()
                if key and value:
                    act_meta[key] = value
        if len(rows) > 3:
            break
    
    # Extract section links
    sections = []
    section_table = soup.find('table', {'id': 'myTableActSection'})
    if section_table:
        for link in section_table.find_all('a', href=True):
            href = link['href']
            text = link.text.strip()
            if '/show-data?' in href and 'sectionId=' in href:
                params = {}
                for param in href.split('?')[1].split('&'):
                    if '=' in param:
                        k, v = param.split('=', 1)
                        params[k] = v
                section_id = params.get('sectionId', '')
                section_no = params.get('sectionno', '')
                act_id = params.get('actid', '')
                
                if section_id:
                    match = re.match(r'Section\s+(\d+[A-Za-z]*)\.\s*(.*)', text, re.DOTALL)
                    if match:
                        sec_num = match.group(1)
                        sec_title = match.group(2).strip()
                    else:
                        sec_num = section_no
                        sec_title = text
                    
                    sections.append({
                        'section_number': sec_num,
                        'section_title': sec_title,
                        'section_id': section_id,
                        'order_number': params.get('orderno', ''),
                        'act_id': act_id,
                        'orgactid': params.get('orgactid', ''),
                    })
    
    return {
        'handle_id': handle_id,
        'metadata': act_meta,
        'total_sections': len(sections),
        'sections': sections,
    }


def get_section_content(act_id, section_id, referer_handle=None):
    """Fetch section content via AJAX API."""
    url = f"{BASE_URL}/SectionPageContent"
    params = {'actid': act_id, 'sectionID': section_id}
    headers = dict(AJAX_HEADERS)
    if referer_handle:
        headers['Referer'] = f"{BASE_URL}/handle/123456789/{referer_handle}"
    
    resp = requests.get(url, headers=headers, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    
    return {
        'content_html': data.get('content', ''),
        'footnote_html': data.get('footnote', ''),
        'content_text': clean_html(data.get('content', '')),
        'footnote_text': clean_html(data.get('footnote', '')),
    }


def scrape_act(handle_id, output_dir='output'):
    """Complete scrape of an act: metadata + all section content."""
    print(f"[*] Fetching act page: handle/123456789/{handle_id}")
    act_data = get_act_page(handle_id)
    print(f"[*] Found: {act_data['metadata'].get('Short Title', 'Unknown')}")
    print(f"[*] Total sections: {act_data['total_sections']}")
    
    for i, section in enumerate(act_data['sections']):
        print(f"  [{i+1}/{act_data['total_sections']}] Section {section['section_number']}: {section['section_title'][:50]}...")
        try:
            content = get_section_content(
                section['act_id'],
                section['section_id'],
                referer_handle=handle_id
            )
            section['content_text'] = content['content_text']
            section['footnote_text'] = content['footnote_text']
            section['content_html'] = content['content_html']
            section['footnote_html'] = content['footnote_html']
        except Exception as e:
            print(f"    ERROR: {e}")
            section['content_text'] = ''
            section['footnote_text'] = ''
            section['error'] = str(e)
        time.sleep(RATE_LIMIT_SECONDS)
    
    os.makedirs(output_dir, exist_ok=True)
    short_title = act_data['metadata'].get('Short Title', f'act_{handle_id}')
    safe_filename = re.sub(r'[^\w\s-]', '', short_title)[:50].strip().replace(' ', '_')
    output_path = os.path.join(output_dir, f"{safe_filename}.json")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(act_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n[✓] Saved to {output_path}")
    print(f"[✓] Total sections scraped: {len(act_data['sections'])}")
    return act_data


def find_act_handle(act_name):
    """Search India Code for an act and return its handle ID."""
    search_url = f"{BASE_URL}/handle/123456789/2180/simple-search"
    params = {'query': act_name, 'locale': 'en'}
    resp = requests.get(search_url, headers=HEADERS, params=params, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'lxml')
    for link in soup.find_all('a', href=True):
        text = link.text.strip()
        href = link['href']
        if text == 'View...' and '/handle/123456789/' in href:
            match = re.search(r'/handle/123456789/(\d+)', href)
            if match:
                return match.group(1)
    return None


# KNOWN ACT HANDLES
KNOWN_ACTS = {
    'BNS_2023': '21420',
    'BNSS_2023': '21419',
    'Consumer_Protection_2019': '21423',
    'DV_Act_2005': '12904',
    'POCSO_2012': '12903',
    'POSH_2013': '20037',
    'RTI_2005': '17520',
    'Dowry_1961': '12822',
    'Code_on_Wages_2019': '22075',
    'Social_Security_Code_2020': '22074',
    'Industrial_Relations_Code_2020': '22078',
    'OSH_Code_2020': '22057',
}

if __name__ == '__main__':
    import sys
    print("=" * 70)
    print("  INDIA CODE SCRAPER — Mera Vakil AI")
    print("  Uses AJAX endpoints — no Selenium required")
    print("=" * 70)
    
    # Default: scrape BNS
    handle = sys.argv[1] if len(sys.argv) > 1 else '21420'
    result = scrape_act(handle, output_dir='scraped_acts')
    
    if result['sections']:
        first = result['sections'][0]
        print(f"\n[✓] First section: Section {first['section_number']}: {first['section_title']}")
        print(f"    Content preview: {first.get('content_text', 'N/A')[:200]}...")
    print(f"\n[✓] Scraping COMPLETE — {len(result['sections'])} sections extracted")
