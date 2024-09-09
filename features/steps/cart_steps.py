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
driver.find_element(By.XPATH,"//h1[text()='Your cart is empty']").text



#Verification that cart is empty message is present.
actual_result=driver.find_element(By.XPATH,"//h1[text()='Your cart is empty']").text
print(actual_result)
driver.quit()