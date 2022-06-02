import pytest
import time

from config.pom import StateFunctions
from selenium.webdriver.common.by import By

from base.variables import *


@pytest.mark.usefixtures("setup")
class TestBohUpdate:

    def test_update(self):
        library = StateFunctions(self.driver)

        Variables.file = open('SP500_price.txt', 'w')

        library.accept_cookie()
        while Variables.i < 3:
            Variables.day_yesterday = Variables.date
            library.current_date_day()

            library.get_price()
            library.dot_remove()
            library.write_price()
            library.wait_5s()
            if Variables.date != Variables.date_yesterday:
                print(Variables.date)

        Variables.file.close()
        print("Success")
