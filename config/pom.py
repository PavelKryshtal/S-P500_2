import time

from base.BaseClass import BaseClass
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from base.variables import Variables
import datetime as DT

class StateFunctions(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def accept_cookie(self):
        driver = self.driver
        driver.get(Variables.S_P500_page)

        # Accept cookie files
        self.is_visible(By.XPATH, Variables.S_p_500_accept_cookie)
        driver.find_element(By.XPATH, Variables.S_p_500_accept_cookie).click()

    def get_price(self):
        # Get current S&P500 price
        driver = self.driver

        self.is_visible(By.XPATH, Variables.S_P500_price)
        Variables.SP500_number_price = driver.find_element(By.XPATH, Variables.S_P500_price).text

        # Print prices
        #print(Variables.SP500_number_price)

    def dot_remove(self):
        Variables.SP500_number_price = Variables.SP500_number_price.replace(".", "")
        Variables.SP500_number_price = Variables.SP500_number_price.replace(",", ".")

        #print(Variables.SP500_number_price)

    def write_price(self):
        print(Variables.time, Variables.SP500_number_price)
        Variables.file.write(Variables.time + " " + Variables.SP500_number_price + "\n")

    def wait_5s(self):
        time.sleep(5)

    def current_date_day(self):
        now = DT.datetime.now(DT.timezone.utc).astimezone()
        time_format = "%H:%M:%S"
        data_format = "%Y-%m-%d"
        Variables.time = f"{now:{time_format}}"
        Variables.data = f"{now:{data_format}}"
        print(Variables.data)

