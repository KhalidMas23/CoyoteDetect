from icrawler.builtin import GoogleImageCrawler
import os

output_dir = 'dataset/day/images/all'
os.makedirs(output_dir, exist_ok=True)

google_crawler = GoogleImageCrawler(storage={'root_dir': output_dir})
google_crawler.crawl(keyword='coyote in daylight', max_num=200, file_idx_offset=0)

print("✅ Coyote image scraping complete.")
