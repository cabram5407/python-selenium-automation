from selenium.webdriver.common.by import By

from pages.base_page import Page

class TargetLoginPage(Page):
USER_NAME = (By.CSS_SELECTOR, "input[id='username']")
USER_PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button[id='login']")


def login_page(self):
    self.open('https://www.target.com/login')

def open_signin_page(self):
   self.open('https://www.target.com/login')

def enter_login_info(self, USER_NAME, USER_PASSWORD, text):
    self.input_text(USER_NAME, text).send_keys(text)
    self.input_text(USER_PASSWORD, text).send_keys(text)

def click_login_button(self, LOGIN_BTN):
        self.wait_to_be_clickable_click(LOGIN_BTN)

def verify_header(self):
    self.verify_message(By.CSS_SELECTOR, "span[id='username--ErrorMessage']")
    self.verify_message(By.CSS_SELECTOR, "span[id=id='password--ErrorMessage']")