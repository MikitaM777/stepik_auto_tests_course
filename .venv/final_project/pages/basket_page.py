from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "BASKET_ITEM is presented"


    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "BASKET isn't empty"