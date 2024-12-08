import pytest
from selenium import webdriver
from urls import URLs, UrlsAPi
from helpers import create_random_user_data
import requests


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    # Создание экземпляра веб-драйвера в зависимости от параметра
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_user_fixture():
    # Создание данных для пользователя
    payload = create_random_user_data()
    created_response = requests.post(UrlsAPi.CREATE_USER, json=payload)
    if created_response.status_code == 200:
        access_token = created_response.json()['accessToken']
        yield payload
        headers = {'Authorization': access_token}
        requests.delete(UrlsAPi.DELETE_USER, headers=headers)
    else:
        yield payload
