from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.target_app_page import TargetAppPage
from pages.target_login_page import TargetLoginPage

#Reference for page objects. It acts as a library that leads to the other pages. It acts as an umbrella
class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.cart_page = CartPage(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.target_login_page = TargetLoginPage(driver)

