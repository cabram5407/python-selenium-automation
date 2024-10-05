#Things related to libraries goes at top of page
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
#Best practice to put locators under page header
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(8)

def click_cart(self):
    # self.wait_to_be_clickable(*self.CART_BTN)
    cart_btn = self.driver.find_element(*self.CART_BTN)
    cart_btn.click()
