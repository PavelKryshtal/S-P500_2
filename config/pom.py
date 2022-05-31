import time

from base.BaseClass import BaseClass
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


from base.variables import Variables


class StateFunctions(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def SP500(self):
        driver = self.driver
        driver.get(Variables.S_P500_page)

        # Accept cookie files
        #self.is_visible(By.XPATH, Variables.S_p_500_accept_cookie)
        #driver.find_element(By.XPATH, Variables.S_p_500_accept_cookie).click()

        # Get current S&P500 price
        #self.is_visible(By.XPATH, Variables.S_P500_price)
        #Variables.SP500_number_price = driver.find_element(By.XPATH, Variables.S_P500_price).text

        # Print prices
        #print(Variables.SP500_number_price)
