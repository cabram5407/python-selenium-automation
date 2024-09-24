from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH, "//h1[text()='Your cart is empty']")

    def verify_empty_cart(self):
        expected_text = 'Your cart is empty'
        self.verify_text(expected_text, *self.CART_EMPTY_MSG)

