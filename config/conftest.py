import pytest
import selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from base.variables import *


@pytest.fixture
def get_webdriver():
    driver = selenium.webdriver.Chrome(executable_path="./chromedriver.exe")
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


@pytest.fixture(scope="function")
def setup(request, get_webdriver):
    driver = get_webdriver
    wait = WebDriverWait(driver, 10)

    driver.maximize_window()

    print("\n---------------Success-----------------")
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
