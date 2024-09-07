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

driver.get('https://www.https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0/')

#Amazon logo
driver.find_element(By.XPATH,"//a[@aria-label='Amazon']")
#Email field
driver.find_element(By.ID,'ap_email')
#Continue button
driver.find_element(By.ID, 'continue')
#Conditions of use
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
#Privacy notice
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]")
#Need help
driver.find_element(By.XPATH, "//a[@class='a-expander-prompt']")
#Forgot password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')
#Other issues with sign-in
driver.find_element(By.ID,'ap-other-signin-issues-link')
#Create Amazon account
driver.find_element(By.ID,'createAccountSubmit')

#Test Case to navigate sign-in page
#Open Target page
driver.get('https://www.target.com/')

#Click Sign-in button
driver.find_element(By.XPATH, "//*[@data-test=@web/Accounting']").click()

#Click sign-in from side navigation
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

#Verify sign-in page opened
expected='Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1/span").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'                                 ")

driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

#Login button is shown
driver.find_element(By.ID, 'login')
