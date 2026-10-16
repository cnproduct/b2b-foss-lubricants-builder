#!/usr/bin/env python3
"""Yandex & IndexNow Protocol Push Notification Script

Submits updated or new URLs to Yandex IndexNow API endpoint (https://yandex.com/indexnow)
for instant crawl queuing and indexing.
"""

import json
import sys
import urllib.request
import urllib.error

INDEXNOW_ENDPOINT = "https://yandex.com/indexnow"
HOST = "www.fosslubricants.com"
KEY = "e4f8c2b19a0d4738a5e62f3c7b8d9e10"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

DEFAULT_URLS = [
    f"https://{HOST}/ru/",
    f"https://{HOST}/ru/cis-central-asia",
    f"https://{HOST}/ru/hydraulic-oil",
    f"https://{HOST}/ru/products",
    f"https://{HOST}/ru/about",
    f"https://{HOST}/ru/packaging-logistics",
    f"https://{HOST}/ru/industrial-oils",
    f"https://{HOST}/ru/contact",
    f"https://{HOST}/sitemap.xml",
]


def notify_yandex(urls=None):
    target_urls = urls or DEFAULT_URLS
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": target_urls
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "FossLubricants-IndexNow/1.0"
        },
        method="POST"
    )
    
    print(f"Submitting {len(target_urls)} URLs to Yandex IndexNow ({INDEXNOW_ENDPOINT})...")
    for u in target_urls:
        print(f"  - {u}")
        
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            code = response.getcode()
            print(f"IndexNow Response: HTTP {code} (Success)")
            return True
    except urllib.error.HTTPError as e:
        print(f"IndexNow HTTP Error: {e.code} - {e.read().decode('utf-8')}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"IndexNow Connection Notice: {e}", file=sys.stderr)
        return False


if __name__ == "__main__":
    custom_urls = sys.argv[1:] if len(sys.argv) > 1 else None
    notify_yandex(custom_urls)
