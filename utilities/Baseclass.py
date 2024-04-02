import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures('setup')
class Baseclass:
    def waitforelement_by_xpath(self, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    def waitforelement_by_css_selector(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))

    def dropdown_select_by_text(self, locator, text):
        dropdown_field = self.driver.find_element(By.XPATH, locator)
        option = Select(dropdown_field)
        option.select_by_visible_text(text)

    def logger_method(self):
        testcase_name = inspect.stack()[1][3]
        logger = logging.getLogger(testcase_name)
        filehandler = logging.FileHandler(
            '/Users/sudhansu/Desktop/Folder/My Projects/Selenium project/seleniumPytest/Tests/Report/log_report.log')
        format = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        filehandler.setFormatter(format)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
