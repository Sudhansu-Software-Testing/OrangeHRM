from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import sys

sys.path.append('/Users/sudhansu/Desktop/Folder/My Projects/Selenium project/seleniumPytest')
from utilities.Baseclass import Baseclass


class Login_page(Baseclass):

    def __init__(self, driver):
        self.driver = driver
        self.logger = Baseclass.logger_method(self)
        self.orangehrm_logo = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]'
        self.login_text = '.oxd-text oxd-text--h5 orangehrm-login-title'
        self.username = '//input[@name="username"]'
        self.password = '//input[@name="password"]'
        self.login_btn = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]'
        self.dashboard_text = ".oxd-text--h6"
        self.logo_after_login = '//img [@alt="client brand banner"]'

    def login_to_orangeHrm(self):
        print("")
        self.waitforelement_by_xpath(self.orangehrm_logo)
        self.driver.find_element(By.XPATH, self.username).send_keys('Admin')
        self.driver.find_element(By.XPATH, self.password).send_keys('admin123')
        self.driver.find_element(By.XPATH, self.login_btn).click()
        self.waitforelement_by_xpath(self.logo_after_login)
        dashboard_element_text = self.driver.find_element(By.CSS_SELECTOR, self.dashboard_text).text
        self.logger.info("Login action is completed.")
        assert dashboard_element_text == 'Dashboard'
