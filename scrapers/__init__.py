from .hn_scraper import HackerNewsScraper
from .bbc_scraper import BBCScraper

SCRAPERS = {
    'hacker_news': HackerNewsScraper,
    'bbc_news': BBCScraper,
}
