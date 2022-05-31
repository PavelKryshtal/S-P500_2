import time

import pytest
import selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from base.variables import *


@pytest.fixture
def get_webdriver():
    driver = selenium.webdriver.Chrome(executable_path="chromedriver.exe")
    return driver


@pytest.fixture(scope="function")
def setup(request, get_webdriver):
    driver = get_webdriver
    wait = WebDriverWait(driver, 10)


    driver.maximize_window()
    #time.sleep(3)
    #driver.get("https://ru.investing.com/indices/us-spx-500-chart")
    #driver.is_visible(By.XPATH, Variables.S_p_500_accept_cookie)
    #driver.find_element(By.XPATH, Variables.S_p_500_accept_cookie).click()
    print("\n---------------Success-----------------")
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
