from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def check_name(self):
        expected_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        actual_name = self.browser.find_element(By.CSS_SELECTOR, "div.alertinner strong").text
        assert  expected_name == actual_name, f"expected: {expected_name}, got: {actual_name}"


    def check_price(self):
        expected_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        actual_price = self.browser.find_element(By.CSS_SELECTOR, ".alertinner p strong").text
        assert  expected_price == actual_price, f"expected: {expected_price}, got: {actual_price}"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), "SUCCESS_ALERT is presented"


    def should_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), "SUCCESS_ALERT didn't disappear"


    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()


