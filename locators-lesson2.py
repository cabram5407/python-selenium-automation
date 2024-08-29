from IPython.utils.coloransi import value
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

import numpy
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver: WebDriver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#locate element:
driver.find_element() #By.ID or XPATH / value

#locate by ID:
driver.fine_element(By.ID, value 'twotabsearchtextbox')
driver.find_element(By.ID, value 'nav-logo-sprites')

#When there is no ID present use relative XPATH that has one attribute and name:
#XPath ="//tagname[@attribute='value']
driver.fine_element(By.XPATH, "//img[@alt='All fashion']")
driver.find_element(By.XPATH, "(//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")

#When you use attributes you can place them in any order to narrow the search:
driver.find_element(By.XPATH,"//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a   ']")

driver.find_element(By.XPATH, "*[@class=nav-a   ' and @href='gp/bestsellers/?ref_=nav_cs_bestsellers']")








