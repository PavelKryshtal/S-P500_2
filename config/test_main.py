import pytest
import time

from config.pom import StateFunctions
from selenium.webdriver.common.by import By

from base.variables import *


@pytest.mark.usefixtures("setup")
class TestBohUpdate:

    def test_update(self):
        library = StateFunctions(self.driver)
        driver = self.driver

        # Check version

        library.SP500()
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@id = 'onetrust-accept-btn-handler']").click()
        time.sleep(3)
        print("Success")
