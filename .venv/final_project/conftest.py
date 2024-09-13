from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

"""
pytest_addoption(parser) добавляет возможность передавать параметр --language через командную строку.  
request.config.getoption("language") считывает переданный параметр.
Браузер запускается с установленным языком через настройку chrome_options
"""