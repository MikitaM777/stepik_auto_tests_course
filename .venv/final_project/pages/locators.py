from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET = (By.CSS_SELECTOR, ".btn-group a.btn-default")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM =(By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner")