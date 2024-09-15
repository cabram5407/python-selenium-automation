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

driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

#verify in correct place
expected = 'Sign into your Target account'
actual=driver.find_element(By.XPATH, "//h1/span").text
assert expected == actual, f'Expected {expected}, did not match actual {actual}'

#If you don't want to compare use
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

#Make sure login button is shown
driver.find_element(By.ID, 'login')