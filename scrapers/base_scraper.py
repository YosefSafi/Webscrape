import requests
from bs4 import BeautifulSoup

class BaseScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def fetch_page(self):
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {self.url}: {e}")
            return None

    def parse(self, html):
        raise NotImplementedError("Subclasses must implement parse method")

    def scrape(self):
        html = self.fetch_page()
        if html:
            return self.parse(html)
        return None
