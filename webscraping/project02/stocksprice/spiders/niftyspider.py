#fetches data dynamically so gives none (use selenium)
# import scrapy
# from datetime import datetime

# class niftyspiderSpider(scrapy.Spider):
#     name = "niftyspider"
#     start_urls = ["https://www.bseindia.com"]

#     def parse(self, response):
#         # Extract Sensex price using the correct CSS selector
#         price = response.css("div#tdsp::text").get()

#         # Get fetch time
#         fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         yield {
#             "price": price.strip() if price else "N/A",
#             "time": fetch_time
#         }

import scrapy
from datetime import datetime
import time

class NiftyspiderSpider(scrapy.Spider):
    name = "niftyspider"
    start_urls = ["https://groww.in/options/nifty"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_time = time.time()  # Track 5 seconds

    def parse(self, response):
        # Run for 5 seconds
        if time.time() - self.start_time < 30:
            # Extract NIFTY price
            price = response.css(".SpotPrice_spotPriceText__6G_Na span::text").get()

            # Fetch current timestamp
            fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Yield price and timestamp
            yield {
                "price": price.strip() if price else "N/A",
                "time": fetch_time
            }

            # Schedule another request
            time.sleep(10)  # Wait 1 second before the next request
            yield scrapy.Request(url=self.start_urls[0], callback=self.parse)
