from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from base.variables import *


class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 10)
        self.__wait_1s = WebDriverWait(driver, 0.5, 0.1)
        self.wait = WebDriverWait(driver, 10)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {"id": By.ID,
                    "xpath": By.XPATH}
        return locating[find_by]

    # Check of element visibility
    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def all_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def any_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_any_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def all_visible_05s(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait_1s.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                    locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def text_present(self, find_by: str, locator: str, text: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.text_to_be_present_in_element((self.__get_selenium_by(find_by), locator)),
                                 text, locator_name)

    def text_present2(self):
        return self.__wait.until(
            ec.text_to_be_present_in_element(("xpath", "//*[@id='categoryGrid']/div[5]/div[3]/div/div[2]/div[1]"),
                                             "Category name 0"))

    # State expressions

    # Button on the left-side bar

    # Products
    def products(self):
        return self.driver.find_element(By.ID, Variables.menu_products_id)

    def categories(self):
        return self.driver.find_element(By.ID, Variables.menu_categories_id)

    def groups(self):
        return self.driver.find_element(By.ID, Variables.menu_groups_id)

    def units_of_measurement(self):
        return self.driver.find_element(By.ID, Variables.menu_units_of_measurement_id)

    # Category
    def save_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, Variables.category_save_button_css_selector)

    # Sales department
    def sales_department(self):
        return self.driver.find_element(By.ID, Variables.menu_sales_department_id)

    # Links
    def dashboard_page(self):
        return self.driver.get(Variables.link_dashboard_page)

    # Sales
    def sales(self):
        return self.driver.find_element(By.ID, Variables.menu_sales_id)

    # Discount
    def discount(self):
        return self.driver.find_element(By.ID, Variables.menu_discount_id)

