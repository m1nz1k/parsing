from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
chrome_options = Options()
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)
def get_data(url_list):

    driver.maximize_window()
    for url in url_list:
        driver.get(url)
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
            print(phone)
        except Exception:
            phone = ''
        print(name)
        print(price)
        print(company)



def main():
    url_list = []
    with open('urls.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        url_list.append(line.strip())
    get_data(url_list)



if __name__ == '__main__':
    main()