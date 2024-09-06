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

# open the url
driver.get('https://www.amazon.com/')


driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")
driver.find_element(By.CSS_SELECTOR, "[class*='Create account']")
driver.find_element(By.CSS_SELECTOR, "[id='ap_customer_name']")
driver.find_element(By.CSS_SELECTOR, "[id='ap_email']")
driver.find_element(By.CSS_SELECTOR, "[id='ap_password']")
