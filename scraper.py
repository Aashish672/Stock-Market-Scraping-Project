from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

def get_stock_data():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service('C:/webdrivers/chromedriver.exe')  # Update this path as needed
    driver = webdriver.Chrome()

    urls = [
        'https://groww.in/us-stocks/nke',
        'https://groww.in/us-stocks/ko',
        'https://groww.in/us-stocks/msft',
        'https://groww.in/stocks/m-india-ltd',
        'https://groww.in/us-stocks/axp',
        'https://groww.in/us-stocks/amgn',
        'https://groww.in/us-stocks/aapl',
        'https://groww.in/us-stocks/ba',
        'https://groww.in/us-stocks/csco',
        'https://groww.in/us-stocks/gs',
        'https://groww.in/us-stocks/ibm',
        'https://groww.in/us-stocks/intc',
        'https://groww.in/us-stocks/jpm',
        'https://groww.in/us-stocks/mcd',
        'https://groww.in/us-stocks/crm',
        'https://groww.in/us-stocks/vz',
        'https://groww.in/us-stocks/v',
        'https://groww.in/us-stocks/wmt',
        'https://groww.in/us-stocks/dis'
    ]

    all_data = []

    for url in urls:
        try:
            driver.get(url)
            time.sleep(4)  # Allow JavaScript to load

            company = driver.find_element(By.CSS_SELECTOR, "h1.usph14Head.displaySmall").text
            price = driver.find_element(By.CSS_SELECTOR, "span.uht141Pri.contentPrimary.displayBase").text

            try:
                change = driver.find_element(By.CSS_SELECTOR, "div.uht141Day.bodyBaseHeavy.contentNegative").text
            except:
                change = driver.find_element(By.CSS_SELECTOR, "div.uht141Day.bodyBaseHeavy.contentPositive").text

            try:
                volume_table = driver.find_element(By.CSS_SELECTOR, "table.tb10Table")
                volume = volume_table.find_elements(By.TAG_NAME, "td")[1].text
            except:
                volume = "N/A"

            all_data.append([company, price, change, volume])

        except Exception as e:
            print(f"Error scraping {url}: {e}")

    driver.quit()

    df = pd.DataFrame(all_data, columns=["Company", "Price", "Change", "Volume"])
    return df
