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
#Target test case that opens Target.com, clicks on cart icon and verify empty cart message
#*********************************************************************************************
driver.get('https://www.target.com/')

#Click on shopping cart icon"
driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()

sleep(10)

#Verification that cart is empty.
actual_result=driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text

#verify is true but if false it will fail.
assert expected_result in actual_result, f'Expected {expected_result}, did not match actual {actual_result}'
print('Test case passed')
driver.quit()

#*********************************************************************************************
#Target test case to verify a user log out and user can navigate to sign-in.
#*********************************************************************************************

driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

#side navigation menu to sign-in
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

#verify sign-in form opened
actual_result = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert expected_result in actual_result, f'{expected_result}, got actual {actual_result}'
print('Test case passed')

driver.quit()

