import pytest

from config.pom import StateFunctions
from selenium.webdriver.common.by import By

from base.variables import *


@pytest.mark.usefixtures("setup")
class TestBohUpdate:

    def test_update(self):
        library = StateFunctions(self.driver)

        # Check version
        library.luna()
        print("Success")
