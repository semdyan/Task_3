import pytest
from requests import options

from helpers import create_and_return_user, login_and_delete_user
from selenium import webdriver

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        # options = webdriver.ChromeOptions()
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        # options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def generate_user_data():
    payload = create_and_return_user()
    email = payload.get('email')
    password = payload.get('password')
    yield email, password
    login_and_delete_user(payload)