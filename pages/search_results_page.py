from selenium.webdriver.common.by import By
from pages.base_page import Page


#Class pages use "camel case" naming convention, no underscore '_'
class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    EMPTY_CART_HEADER = (By.XPATH, "//div[@data-test='boxEmptyMsg']")
    SIGN_IN_FORM_OPEN = (By.CSS_SELECTOR, "[class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']")

    def verify_results(self, item)
        self.verify_partial_text(item, *self.SEARCH_RESULTS_HEADER)

    def verify_results_url(self, item):
        self.verify_partial_url(item)

    def sign_in_form(self):
        self.verify_sign_in_page(*self.SIGN_IN_FORM_OPEN)

   def empty_cart(self):
        expected_result = 'Your cart is empty'
        actual_result = self.driver.find_element(*self.EMPTY_CART_HEADER).text
        assert expected_result == actual_result, f'Expected {expected_result}, got {actual_result}'


