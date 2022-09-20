import requests
import bs4
import urllib.parse
from fake_useragent import UserAgent

url = None


def create_sessions(url: str) -> requests.models.Response:
    headers = {"User-Agent": UserAgent().random}
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url)
    return response


def search_goods(goods: str):
    global url
    url = f"https://akcenter.com.ua/index.php?route=product/search&search={urllib.parse.quote(goods)}"
    answer_site = create_sessions(url)
    answr = get_information(answer_site)
    return answr


def get_information(site_response: requests.models.Response) -> list:
    soup = bs4.BeautifulSoup(site_response.text, "lxml")
    data_url = soup.find_all('div', class_="us-module-img")
    data_model = soup.find_all('div', class_='us-module-model')
    data_price = soup.find_all('div', class_='us-module-price')
    data_photo = soup.find_all('div', class_='us-module-item d-flex flex-column')
    photo = [data.find('img').get('src') for data in data_photo]
    model = [data.text.strip() for data in data_model if "Код товару" in data.text.strip()]
    price = [f"Ціна: {data.find('span').text}" for data in data_price]
    availability = [data.text.strip() for data in data_model if "Наявність" in data.text.strip()]
    good_url = [data.find('a').get('href') for data in data_url]
    return list(zip(model, price, availability, photo, good_url))


search_goods('лялька')
