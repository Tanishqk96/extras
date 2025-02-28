import scrapy
import json
import time

class SensexSpider(scrapy.Spider):
    name = "sensex"
    allowed_domains = ["bseindia.com"]
    start_urls = ["https://api.bseindia.com/BseIndiaAPI/api/GetLinknew/w?code=98"]

    custom_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.9",
        "Connection": "keep-alive",
        "Host": "api.bseindia.com",
        "Origin": "https://www.bseindia.com",
        "Referer": "https://www.bseindia.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }

    start_time = time.time()  # Store start time

    def start_requests(self):
        """Initiates request to fetch Sensex data."""
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.custom_headers, callback=self.parse)

    def parse(self, response):
        """Parses JSON response and extracts Sensex data repeatedly for 10 seconds."""
        if time.time() - self.start_time >= 20:  # Stop after 10 seconds
            self.log("✅ Finished scraping after 10 seconds.")
            return

        try:
            data = response.json()  # Parse JSON response directly

            # Extract relevant fields from JSON
            sensex_data = {
                "Index Name": data.get("IndexName", "N/A"),
                "Current Value": data.get("CurrValue", "N/A"),
                "Change": data.get("Chg", "N/A"),
                "Change Percentage": data.get("ChgPer", "N/A"),
                "Open": data.get("I_open", "N/A"),
                "High": data.get("High", "N/A"),
                "Low": data.get("Low", "N/A"),
                "Previous Close": data.get("Prev_Close", "N/A"),
                "Date & Time": data.get("DT_TM", "N/A"),
                "Market Status": "Open" if data.get("MktStatus") == "1" else "Closed"
            }

            yield sensex_data  # Output the extracted data

        except json.JSONDecodeError:
            self.log("⚠️ Failed to parse JSON response.")

        # Schedule next request after 1 second
        yield scrapy.Request(self.start_urls[0], headers=self.custom_headers, callback=self.parse, dont_filter=True)
