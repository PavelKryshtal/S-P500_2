import time
import pymysql
import socket

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

    def cardano_page(self):
        driver = self.driver
        driver.get(Variables.Cardano_page)

    def accept_cookie(self):
        driver = self.driver
        driver.get(Variables.Cardano_page)

        # Accept cookie files
        self.is_visible(By.XPATH, Variables.S_p_500_accept_cookie)
        driver.find_element(By.XPATH, Variables.S_p_500_accept_cookie).click()

    def get_price(self):
        # Get current S&P500 price
        driver = self.driver

        self.is_visible(By.XPATH, Variables.Cardano_price)
        Variables.Cardano_number_price = driver.find_element(By.XPATH, Variables.Cardano_price).text
        print(Variables.Cardano_number_price)

        # Print prices
        #print(Variables.SP500_number_price)

    def dot_remove(self):
        Variables.Cardano_number_price = Variables.Cardano_number_price.replace("$", "")
        Variables.Cardano_number_price = Variables.Cardano_number_price.replace(" USD", "")
        print(Variables.Cardano_number_price)

        #print(Variables.SP500_number_price)

    def write_price(self):
        print(Variables.time, Variables.Cardano_number_price)
        Variables.file.write(Variables.time + " " + Variables.Cardano_number_price + "\n")

    def wait_5s(self):
        time.sleep(5)

    def data_base(self):
        # Define time and data
        now = DT.datetime.now(DT.timezone.utc).astimezone()
        time_format = "%H:%M:%S"
        data_format = "%Y-%m-%d"
        Variables.time = f"{now:{time_format}}"
        Variables.date = f"{now:{data_format}}"

        # Connection to database
        connection = pymysql.connect(host="192.168.0.31", port=3306, user="pavel", passwd="1234", database="Cryptocurency")
        cursor = connection.cursor()

        # Enter data in database
        ArtistTableSql = """INSERT INTO `Cardano`(`DATE`, `TIME`, `PRICE`) VALUES ('""" + Variables.date + """', '""" + Variables.time + """', """ + Variables.Cardano_number_price + """ )"""

        cursor.execute(ArtistTableSql)
        connection.close()