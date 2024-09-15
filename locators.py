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


#connect by search box:
driver.fine_element(By.ID, value 'twotabsearchtextbox')

#connect to Amazon logo
driver.find_element(By.ID, value 'nav-logo-sprites')

#When there is no ID present use relative XPATH that has one attribute and name:
#XPath ="//tagname[@attribute='value']"
driver.fine_element(By.XPATH, "//img[@alt='All fashion']")
driver.find_element(By.XPATH, "(//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")

#Multiple attributes in any order to narrow the search:
driver.find_element(By.XPATH,"//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")

#identifying with text and attribute
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a   ']")

#Wildcard search only the attribute or text, useful if you don't know tag value.
driver.find_element(By.XPATH, "//*[@class=nav-a   ' and @href='gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a   ']")

#Linking to a parent element and then child elements
driver.find_element(By.XPATH, "//div[@id='nav-main']//a[text()='Best Sellers']")

#*******************************************************************************************
#Homework 2 - Create Account Locators
#*******************************************************************************************

driver.get('https://www.https://www.amazon.com/')

#Amazon logo
driver.find_element(By.XPATH,"//a[@aria-label='Amazon']")

#create account label
driver.find_element(By.XPATH,"//*[@class='a-spacing-small']")

#Email field
driver.find_element(By.ID,'ap_email')

#Continue button
driver.find_element(By.ID, 'continue')

#Conditions of use
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_register_notification_condition_of_use')]")

#Privacy notice
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]")

#already have account, sign-in
driver.find_element(By.XPATH, "//a[@class='a-link-emphasis']")

#Forgot password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#Other issues with sign-in
driver.find_element(By.ID,'ap-other-signin-issues-link')

#Create your Amazon account button
driver.find_element(By.ID,'createAccountSubmit')



