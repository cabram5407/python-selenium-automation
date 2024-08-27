from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

import numpy
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#locate element:
driver.find_element() #By.ID or XPATH / value

#locate by ID:
driver.fine_element(By.ID, value 'twotabsearchtextbox')
driver.find_element(By.ID, value 'nav-logo-sprites')
