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
driver.implicitly_wait(4)

#Target test case that opens Target.com, clicks on sign-in and navigates to side navigation
driver.get('https://www.target.com/circle')

#Click Sign-in button
driver.find_element(By.XPATH, "//*[@data-test=@web/Accounting']").click()

#Click sign-in from side navigation
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

#Verify sign-in page opened
expected='Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1/span").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'                                 ")









