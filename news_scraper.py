import requests
from bs4 import BeautifulSoup
import time
import random
import os

class AdvancedScraper:
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
        'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36'
    ]

    def __init__(self, url, tag, class_name):
        self.url = url
        self.tag = tag
        self.class_name = class_name
        self.data_items = []

    def _get_html_response(self):
        random_agent = random.choice(self.USER_AGENTS)
        headers = {'User-Agent': random_agent}
        time.sleep(random.uniform(1, 3))
        
        try:
            print(f"Fetching URL: {self.url}")
            response = requests.get(self.url, headers=headers, timeout=15)
            response.raise_for_status()
            return response.content
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the webpage: {e}")
            return None

    def scrape(self):
        html_content = self._get_html_response()
        
        if html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser')
        
        if self.class_name:
            elements = soup.find_all(self.tag, class_=self.class_name)
        else:
            elements = soup.find_all(self.tag)

        for element in elements:
            item_text = element.get_text(strip=True)
            if item_text:
                self.data_items.append(item_text)
        
        print(f"Scraped {len(self.data_items)} items.")

    def save_to_file(self, filename="scraped_headlines.txt"):
        if not self.data_items:
            print("No data to save.")
            return

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for item in self.data_items:
                    f.write(item + '\n')
            
            print(f"Success: Data saved to {filename} in {os.getcwd()}")
            
        except IOError as e:
            print(f"Error writing to file: {e}")

if __name__ == "__main__":
    
    # --- कॉन्फ़िगरेशन (Configuration) ---
    # Hindustan Times के लिए वर्किंग कॉन्फ़िगरेशन
    NEWS_URL = 'https://www.hindustantimes.com/latest-news' 
    TARGET_TAG = 'h3' 
    TARGET_CLASS = 'hdg3' 
    
    OUTPUT_FILE = 'scraped_headlines.txt'
    # -----------------------------------

    scraper = AdvancedScraper(NEWS_URL, TARGET_TAG, TARGET_CLASS)
    scraper.scrape()
    scraper.save_to_file(OUTPUT_FILE)