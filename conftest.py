import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.app import Application


@pytest.fixture
def app():
    url = 'https://only.digital/'
    chrome_options = Options()
    chrome_options.add_argument("window-size=1800,1080")
    driver = webdriver.Chrome('/Users/nick/chromedriver')
    app = Application(driver, url)
    yield app
    app.quit()


