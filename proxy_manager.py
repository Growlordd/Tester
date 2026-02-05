#!/usr/bin/env python3
# Proxy Manager for SocMed Booster
import requests
from concurrent.futures import ThreadPoolExecutor
import json

class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.working_proxies = []
        
    def scrape_proxies(self):
        """Scrape fresh proxies from multiple sources"""
        sources = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
            "https://www.proxy-list.download/api/v1/get?type=http"
        ]
        
        all_proxies = []
        for url in sources:
            try:
                response = requests.get(url, timeout=10)
                proxies = response.text.strip().split('\n')
                all_proxies.extend([p.strip() for p in proxies if p.strip()])
            except:
                continue
        
        # Remove duplicates
        self.proxies = list(set(all_proxies))
        print(f"🌐 Found {len(self.proxies)} proxies")
        
        # Save to file
        with open('proxies.txt', 'w') as f:
            for proxy in self.proxies:
                f.write(f"{proxy}\n")
        
        return self.proxies
    
    def test_proxy(self, proxy):
        """Test if proxy is working"""
        try:
            test_urls = [
                "https://www.tiktok.com",
                "https://www.instagram.com",
                "https://web.telegram.org"
            ]
            
            for url in test_urls:
                try:
                    response = requests.get(
                        url,
                        proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'},
                        timeout=5
                    )
                    if response.status_code == 200:
                        return proxy
                except:
                    continue
        except:
            pass
        
        return None
    
    def test_all_proxies(self):
        """Test all proxies"""
        if not self.proxies:
            self.scrape_proxies()
        
        print(f"🧪 Testing {len(self.proxies)} proxies...")
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            results = list(executor.map(self.test_proxy, self.proxies[:500]))  # Test first 500
        
        self.working_proxies = [p for p in results if p]
        
        print(f"✅ Working proxies: {len(self.working_proxies)}")
        
        # Save working proxies
        with open('working_proxies.txt', 'w') as f:
            for proxy in self.working_proxies:
                f.write(f"{proxy}\n")
        
        return self.working_proxies
