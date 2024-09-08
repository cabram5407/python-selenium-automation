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

# By CSS, by ID, use #:
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
# Same as =>
driver.find_element(By.ID, "twotabsearchtextbox")  # Note, By.ID is preferred if you only use ID

# By CSS, by class, use .
driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute")
driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")
# By CSS, by tag & class(es)
driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")
# By CSS, tag & ID & class
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input.nav-progressive-attribute")

# By CSS, attributes, use []:
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, ".nav-input[tabindex='0'][placeholder='Search Amazon']")

# By CSS, attribute, partial match:
driver.find_element(By.CSS_SELECTOR, "[href*='notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "[class*='search']")
driver.find_element(By.CSS_SELECTOR, "[id*='search']")

# By CSS, from parent => to child, separate by space:
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")
driver.find_element(By.CSS_SELECTOR, ".a-box-inner #legalTextRow [href*='privacy']")

#Homework 3 - CSS locotors

# open the url
driver.get('https://www.amazon.com/')

#From Amazon home page, click on arrow in top navigation
driver.find_element(By.XPATH, "//*[text()='Account & Lists' and @class='nav-line-2 ']")

#Click on Creat Account button
driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit")

driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name.ap_customer_name_context_message_section")
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
driver.find_element(By.XPATH, "//div[@class='a-alert-content']")
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "input#continue")

#Condition of use
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_register_notification_condition_of_use')]")

#Privacy notice
driver.find_element(By.XPATH, "//a[contains(@href,'ap_register_notification_privacy_notice')]")

#Already have an account sign-in
driver.find_element(By.XPATH, "//a[@class='a-link-emphasis']")

#Target test case that opens Target.com, clicks on cart icon and verify empty cart message
driver.get('https://www.target.com/')

#Click on shopping cart icon"
driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()

sleep(10)

#Verification that cart is empty.
actual_result=driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text

#verify is true but if false it will fail.
assert expected_result in actual_result, f'Expected {expected_result}, did not match actual {actual_result}'
print('Test case passed')
driver.quit()

#Target test case to verify a user log out and user can navigate to sign-in.
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

#side navigation menu to sign-in
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

#verify sign-in form opened
actual_result = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text

assert expected_result in actual_result, f'{expected_result}, got actual {actual_result}'
print('Test case passed')

driver.quit()