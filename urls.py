import requests
from bs4 import BeautifulSoup
def get_data(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')

    elements = soup.find_all('a', class_='aui-link js-bp-title js-ga-link js-catalogue-ecommerce js-conversion-event')
    for el in elements:
        el = el.get('href')
        with open('urls.txt', 'a', encoding='utf-8') as file:
            file.writelines(el + '\n')


def main():
    for i in range(1, 26):
        get_data(f'https://perm.pulscen.ru/search/price/1003-kirpich-kamen-bloki?q=%D0%B3%D0%B0%D0%B7%D0%BE%D0%B1%D0%BB%D0%BE%D0%BA&page={i}')



if __name__ == '__main__':
    main()