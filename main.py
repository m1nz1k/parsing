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
chrome_options.add_argument('--headless')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)
def get_data(url):
    try:
        driver.maximize_window()
        driver.get(url)
        time.sleep(1.5)
        product_elements = driver.find_elements(By.CSS_SELECTOR, 'li.product-listing__item')

        for click_el in product_elements:
            try:
                name = click_el.find_element(By.CSS_SELECTOR, 'span.product-listing__product-name').text
                print(name)

                phone_button = click_el.find_element(By.CSS_SELECTOR, 'div.js-company-contacts-settings')
                phone_button.click()
            except Exception:
                print("Phone button not found for this product")

        product_elements = driver.find_elements(By.CSS_SELECTOR, 'li.product-listing__item')
        for el in product_elements:
            try:
                name = el.find_element(By.CSS_SELECTOR, 'span.product-listing__product-name').text
            except Exception:
                name = ''
            try:
                company_name_element = el.find_element(By.CSS_SELECTOR, 'div.product-listing__company-name')
                company_name = company_name_element.find_element(By.CSS_SELECTOR, 'span').text.strip()
            except Exception:
                company_name = ''
            try:
                price = el.find_element(By.CSS_SELECTOR, 'div.product-listing__price-wrapper').text
            except Exception:
                price = ''
            try:
                phone_number = el.find_element(By.CLASS_NAME, 'js-company-contacts-settings').text
            except Exception:
                phone_number = ''

            print(phone_number)
    except Exception as ex:
        print(ex)
    finally:
        driver.quit()
        driver.close()


def main():
    get_data('https://perm.pulscen.ru/search/price/1003-kirpich-kamen-bloki?q=%D0%B3%D0%B0%D0%B7%D0%BE%D0%B1%D0%BB%D0%BE%D0%BA')


if __name__ == '__main__':
    main()