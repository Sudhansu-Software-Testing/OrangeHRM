import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.manager import DriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome', help='my options are : chrome,edge etc')


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption('browser')
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    chrome_option.add_argument("--disable-gpu")
    chrome_option.add_argument('--ignore-certificate-errors')
    global driver
    if browser_name == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_option)
    elif browser_name == 'edge':
        driver = webdriver.Edge()
    else:
        pass
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print(driver.title)
    request.cls.driver = driver
    yield
    driver.close()


def _capture_screenshot(name):
    filepath = '/Users/sudhansu/Desktop/Folder/My Projects/Selenium project/seleniumPytest/Tests/screenshots'
    driver.get_screenshot_as_file(filename=filepath+"/"+random.randint(1,100))
