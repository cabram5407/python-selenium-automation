from selenium.webdriver.common.by import By

from pages.base_page import Page

class TargetAppPage(Page):
    PP_LINK = (By.XPATH, "//a[text()='Privacy policy']")
    CONDITIONS_LINK = (By.CSS_SELECTOR, "[href='/c/terms-conditions/-/N-4sr7l']")

    def open_signin_page(self):
        self.open('https://www.target.com/login')


    def open_target_app(self):
        self.open('https://www.target.com/c/target-app/')


    def click_terms_link(self):
        self.wait_to_be_clickable(*self.CONDITIONS_LINK)


    def click_pp_link(self):
        self.wait_to_be_clickable_click(*self.PP_LINK)


    def verify_terms_page_open(self):
        self.verify_partial_url('terms-conditions')


    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy/')