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


    #driver.maximize_window()
    driver.get(Variables.S_P500_page)
    time.sleep(5)
    #driver.get("https://ru.investing.com/indices/us-spx-500-chart")
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    time.sleep(5)
    #driver.find_element(By.XPATH, Variables.S_p_500_accept_cookie).click()
    print("\n---------------Success-----------------")
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
