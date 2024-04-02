import time
from time import sleep

import pytest
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

sys.path.append('/Users/sudhansu/Desktop/Folder/My Projects/Selenium project/seleniumPytest')
from utilities.Baseclass import Baseclass


class Dashboard_menu(Baseclass):
    def __init__(self, driver):
        self.driver = driver
        self.logger = Baseclass.logger_method(self)
        self.logo = "//img[@alt='client brand banner']"
        self.admin = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]"
        self.pim = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]"
        self.leave = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[3]"
        self.time = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[4]"
        self.recruitment = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[5]"
        self.my_info = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[6]"
        self.performance = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[7]"
        self.dashboard = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[8]"
        self.directory = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[9]"
        self.maintenance = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[10]"
        self.claim = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[11]"
        self.buzz = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[12]"
        self.search_field = "//input [@placeholder='Search']"
        self.search = "//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/div[1]/div[1]/*[1]"
        self.menu_locators = [
            self.admin,
            self.pim,
            self.leave,
            self.time,
            self.recruitment,
            self.my_info,
            self.performance,
            self.dashboard,
            self.directory,
            self.maintenance,
            self.claim,
            self.buzz]

        self.menu_names = ["Admin",
                           "PIM",
                           'Leave',
                           'Time',
                           'Recruitment',
                           'My Info',
                           'Performance',
                           'Dashboard',
                           'Directory',
                           'Maintenance',
                           'Claim',
                           'Buzz'
                           ]

    def check_menus(self):
        admin_menu = self.driver.find_element(By.XPATH, self.admin).text
        print(admin_menu)
        assert admin_menu == "Admin"
        pim_menu = self.driver.find_element(By.XPATH, self.pim).text
        print(pim_menu)
        assert pim_menu == "PIM"
        leave_menu = self.driver.find_element(By.XPATH, self.leave).text
        print(leave_menu)
        assert leave_menu == 'Leave'
        time_menu = self.driver.find_element(By.XPATH, self.time).text
        print(time_menu)
        assert time_menu == 'Time'
        recruitment_menu = self.driver.find_element(By.XPATH, self.recruitment).text
        print(recruitment_menu)
        assert recruitment_menu == 'Recruitment'
        my_info_menu = self.driver.find_element(By.XPATH, self.my_info).text
        print(my_info_menu)
        assert my_info_menu == 'My Info'
        performance_menu = self.driver.find_element(By.XPATH, self.performance).text
        print(performance_menu)
        assert performance_menu == 'Performance'
        dashboard_menu = self.driver.find_element(By.XPATH, self.dashboard).text
        print(dashboard_menu)
        assert dashboard_menu == 'Dashboard'
        directory_menu = self.driver.find_element(By.XPATH, self.directory).text
        print(directory_menu)
        assert directory_menu == 'Directory'
        maintenance_menu = self.driver.find_element(By.XPATH, self.maintenance).text
        print(maintenance_menu)
        assert maintenance_menu == 'Maintenance'
        claim_menu = self.driver.find_element(By.XPATH, self.claim).text
        print(claim_menu)
        assert claim_menu == 'Claim'
        buzz_menu = self.driver.find_element(By.XPATH, self.buzz).text
        print(buzz_menu)
        assert buzz_menu == 'Buzz'
        self.logger.info("Second Test passed successfully.")

    def test_search_functionality(self, size, menu_names):
        self.waitforelement_by_xpath(self.logo)
        search_input = self.driver.find_element(By.XPATH, self.search_field)
        search_input.send_keys(menu_names)
        self.driver.find_element(By.XPATH, self.search).click()
        self.waitforelement_by_xpath('//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]')
        searched_result = self.driver.find_element(By.XPATH,
                                                   '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').text
        assert searched_result == menu_names
        search_inputbox = self.driver.find_element(By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[1]')
        search_inputbox.send_keys('')
        self.driver.refresh()
        print(f'{menu_names} iteration completed.')
