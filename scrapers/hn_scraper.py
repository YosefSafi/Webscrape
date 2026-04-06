from .base_scraper import BaseScraper
from bs4 import BeautifulSoup

class HackerNewsScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://news.ycombinator.com/")

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        headlines = []
        # HN headlines are in <span class="titleline">
        for span in soup.find_all('span', class_='titleline'):
            a_tag = span.find('a')
            if a_tag:
                headlines.append({
                    'title': a_tag.get_text(),
                    'url': a_tag['href']
                })
        return headlines[:10] # Top 10 headlines
