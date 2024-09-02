#Default settings for all test automation
from IPython.utils.coloransi import value
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#installs chrome driver
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver: WebDriver = webdriver.Chrome(service=service)
driver.maximize_window()


#Practice with locators portion of homework
driver.get("https://www.amazon.com/")

#Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
#Email field
driver.find_element(By.ID,"ap_email")
#Continue button
driver.find_element(By.ID, "continue")
#Conditions of use
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
#Privacy notice
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
#Need help
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#Forgot password link
driver.find_element(By.ID, "auth-fpp-link-bottom")
#Other issues with sign-in
driver.find_element(By.ID,"ap-other-signin-issues-link")
#Create Amazon account
driver.find_element(By.ID,"createAccountSubmit")

#Test Case #1
#Open Target page
driver.get("https://www.target.com/")

#Click Sign-in button
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()

#Click sign-in from side navigation
driver.find_element(By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']").click()
#Verify sign-in page opened
actual_result = driver.find_element(By.XPATH, ("//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']").text
expected_result = 'Sign into your Target account'

