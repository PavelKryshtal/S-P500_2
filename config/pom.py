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

    def luna(self):
        driver = self.driver
        driver.get(Variables.S_P500_page)

