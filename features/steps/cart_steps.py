from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')

#Click on shopping cart icon"
driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()

sleep(10)

#Verification that cart is empty.
actual_result=driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text

#verify is true but if false it will fail.
assert expected_result in actual_result, f'Expected {expected_result}, did not match actual {actual_result}'
print(actual_result)

driver.quit()