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
#*********************************************************************************************
#Target test case that opens Target.com, searches for product
#*********************************************************************************************

driver.get('https://www.target.com/')

#searches for product items
driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys('tea')

#click search button to select product
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

#verify product header shows searched item
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
expected_result = 'tea'
assert expected_result in actual_result

driver.quit()

#*********************************************************************************************
#Target test case that opens Target.com, verifies cart is empty
#*********************************************************************************************
driver.get('https://www.target.com/')

#click on shopping cart
driver.find_elements(By.XPATH, "//div[@data-test='@web/CartIcon' and @class='sc-e487bf3b-1 fSHTpu']").click()

#verify cart is empty
actual_result=driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
expected_result = 'Your cart is empty'
assert expected_result == actual_result, f'Expected {expected_result}, got {actual_result}'