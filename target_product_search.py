from IPython.utils.coloransi import value
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import numpy

#installs chrome driver
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)

#starts the browser you are using
driver: WebDriver = webdriver.Chrome(service=service)
driver.maximize_window()

#Target test case that opens Target.com, clicks on cart icon and verify empty cart message
driver.get('https://www.target.com/')

#search for product
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

#Verify search item shown
driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")