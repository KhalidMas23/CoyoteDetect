import os
from icrawler.builtin import GoogleImageCrawler

output_dir = 'dataset/day/images/all'
os.makedirs(output_dir, exist_ok=True)

# Automatically find the highest image number already downloaded
existing_files = [f for f in os.listdir(output_dir) if f.endswith('.jpg')]
existing_numbers = [
    int(f.split('.')[0]) for f in existing_files if f.split('.')[0].isdigit()
]
start_index = max(existing_numbers) + 1 if existing_numbers else 0

# Change the keyword for each run
search_term = "coyote in field daytime"

# Keyword tracker
# coyote in daytime
# coyote in forest daytime
# coyote in tall grass
# coyote in field daytime

google_crawler = GoogleImageCrawler(storage={'root_dir': output_dir})
google_crawler.crawl(keyword=search_term, max_num=100, file_idx_offset=start_index)

print(f"✅ Scraped {search_term} starting at index {start_index}")
