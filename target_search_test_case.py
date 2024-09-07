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
driver: WebDriver = webdriver.Chrome(service=service)
driver.maximize_window()

#Target test case
driver.get('https://www.target.com/')

#Search for text, "Tea"
driver.find_element(By.ID, 'search').send_keys('tea')

#click on tea
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()
sleep(10)

#Verification for result
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
expected_result = 'tea'

assert expected_result in actual_result, f'{expected_result}, got actual {actual_result}'
print['Test case passed']
driver.quit()
