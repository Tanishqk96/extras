from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configure Selenium WebDriver
options = Options()
options.headless = False  # Set to True to run in the background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open BSE website
driver.get('https://www.bseindia.com/')

try:
    while True:
        # Wait until the index price element is available and contains text
        price_element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(//strong[@id='idcrval'])[2]"))
        )

        sensex_price = price_element.text.strip()

        # Ensure the price is not empty before printing
        if sensex_price:
            print(f"BSE INDEX 50 Index Price: {sensex_price}")
        else:
            print("⚠️ Price data not loaded yet. Retrying...")

        time.sleep(10)  # Wait for 10 seconds before fetching again

except KeyboardInterrupt:
    print("\n🛑 Stopping the scraper...")
finally:
    driver.quit()  # Close the browser
