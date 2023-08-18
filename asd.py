import concurrent.futures
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


def get_data(url_list):
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    results = []
    for url in url_list:
        driver.get(url)
        time.sleep(1)

        try:
            name = driver.find_element(By.CSS_SELECTOR, 'h1.product-info__header').text
        except Exception:
            name = ''
        try:
            price = driver.find_element(By.CSS_SELECTOR, 'div.product-price__value').text
        except Exception:
            price = ''
        try:
            company = driver.find_element(By.CSS_SELECTOR, 'div.product-company-info__name-link-wrapper').text
        except Exception:
            company = ''
        try:
            button = driver.find_element(By.CSS_SELECTOR, 'div.product-company-info__button').click()
        except Exception:
            pass
        time.sleep(2)
        try:
            phone = driver.find_element(By.CSS_SELECTOR, 'div.product-company-info__button').text
        except Exception:
            phone = ''

        results.append((name, company, price, phone, url))

    driver.quit()

    return results


def main():
    url_list = []
    with open('urls.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        url_list.append(line.strip())

    chunk_size = len(url_list) // 3
    url_chunks = [url_list[i:i + chunk_size] for i in range(0, len(url_list), chunk_size)]

    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for chunk in url_chunks:
            future = executor.submit(get_data, chunk)
            results.append(future)

    data = []
    for future in results:
        data.extend(future.result())

    df = pd.DataFrame(data, columns=['Название товара', 'Компания', 'Цена', 'Номер', 'url'])
    df.to_excel('parsed_data.xlsx', index=False)


if __name__ == '__main__':
    main()
