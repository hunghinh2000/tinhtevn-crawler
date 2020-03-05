import os
import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from src.spiders.tinhte_spider import TinhteSpider
from src.load_config import load_config

def main():
    json_output_path, image_output_path, tinhte_category_link, year_limit = load_config()

    process = CrawlerProcess({
        'LOG_STDOUT': True,
        'LOG_FILE': os.path.join("logs", "scrapy_tinhte_crawler_"+str(time.time())+".log"),
        'DOWNLOAD_DELAY': 15,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'
    })

    process.crawl(TinhteSpider, category_url = tinhte_category_link, 
                                json_output_path = json_output_path,
                                image_output_path = image_output_path,
                                year_limit = year_limit)
    process.start()

if __name__ == "__main__":
    main()