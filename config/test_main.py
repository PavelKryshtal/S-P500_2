import pytest

from config.pom import StateFunctions

from base.variables import *


@pytest.mark.usefixtures("setup")
class TestBohUpdate:

    def test_update(self):
        library = StateFunctions(self.driver)
        library.cardano_page()

        while Variables.i < 3:
            Variables.day_yesterday = Variables.date

            library.get_price()
            library.dot_remove()
            library.write_price()
            library.wait_5s()

            library.data_base()
            #Variables.i = 3
        Variables.file.close()
        print("Success")
