import time

import pytest
import openpyxl
import sys

sys.path.append("/Users/sudhansu/Desktop/Folder/My Projects/Selenium project/seleniumPytest")
from utilities.Baseclass import Baseclass
from TestData.Testdata import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Datadriven(Baseclass):
    def __init__(self, driver):
        self.driver = driver
        self.logger = self.logger_method()
        self.add_btn = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
        self.User_Role_ESS = '(//div[contains(text(),"-- Select --")])[1]'
        self.User_Role_Admin = '(//div[contains(text(),"-- Select --")])[1]'
        self.Employee_Name = '//input[@placeholder="Type for hints..."]'
        self.Status = '((//div[@class="oxd-select-text oxd-select-text--active"])[2])/div[1]'
        self.Username = '(//input[@class="oxd-input oxd-input--active"])[2]'
        self.Password = '(//input[@class="oxd-input oxd-input--active"])[3]'
        self.Confirm_Password = '(//input[@class="oxd-input oxd-input--active"])[4]'
        self.admin = '//body/div[@id="app"]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]/span[1]'
        self.adduser_text = '//h6[@class="oxd-text oxd-text--h6 orangehrm-main-title"]'

    def add_user(self):
        Testdata = TestData()
        number_of_row = Testdata.rows
        number_of_col = Testdata.cols
        sheet = Testdata.sheet
        for i in range(2, number_of_row + 1):
            excel = TestData.load_excel_file(self, r=i, c=number_of_col, sheet=sheet)
            print(excel)
            self.waitforelement_by_xpath(self.admin)
            self.driver.find_element(By.XPATH, self.admin).click()
            self.waitforelement_by_xpath(self.add_btn)
            self.driver.find_element(By.XPATH, self.add_btn).click()
            self.waitforelement_by_xpath(self.adduser_text)
            self.driver.find_element(By.XPATH,
                                     '(//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"])[1]').click()
            # self.driver.find_element(By.XPATH, self.Employee_Name).send_keys(excel['Employee Name'])
            # time.sleep(5)
            # self.driver.find_element(By.XPATH, self.Status).send_keys(excel['Status'])
            # time.sleep(5)
            # self.driver.find_element(By.XPATH, self.Username).send_keys(excel['Username'])
            # time.sleep(5)
            # self.driver.find_element(By.XPATH, self.Password).send_keys(excel['Password'])
            # time.sleep(5)
            # self.driver.find_element(By.XPATH, self.Confirm_Password).send_keys(excel['Confirm Password'])
            # time.sleep(5)
            # self.driver.refresh()
        self.logger.info('Datadriven user creation steps are completed.')
