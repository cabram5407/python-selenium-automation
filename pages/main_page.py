from pages.base_page import Page
#inheritance allows the page to inherit the functions defined in the base page.

class MainPage(Page):

    def open_main(self):
        self.open('https://www.target.com/')


