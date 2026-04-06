from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from .base_scraper import BaseScraper
import time

class JSBaseScraper(BaseScraper):
    def __init__(self, url):
        super().__init__(url)
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless") # Run in headless mode
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")

    def fetch_page(self):
        try:
            # Note: This requires chromedriver to be installed and in PATH
            driver = webdriver.Chrome(options=self.chrome_options)
            driver.get(self.url)
            time.sleep(3) # Wait for JS to load
            html = driver.page_source
            driver.quit()
            return html
        except Exception as e:
            print(f"Error fetching {self.url} with Selenium: {e}")
            return None
