from .base_scraper import BaseScraper
from bs4 import BeautifulSoup

class BBCScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://www.bbc.com/news")

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        headlines = []
        # Find all h2 or h3 elements that often contain headlines
        for h in soup.find_all(['h2', 'h3']):
            title = h.get_text().strip()
            if title and len(title) > 10: # Basic filter
                headlines.append({
                    'title': title
                })
        return headlines[:5] # Top 5 headlines
