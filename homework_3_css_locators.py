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

#From Amazon home page, click on arrow in top navigation
driver.find_element((By.CSS_SELECTOR, ".Account & Lists' and @class='nav-line-2")

#Click on Creat Account button
driver.find_element(By.ID, "createAccountSubmit")

driver.find_element((By.CSS_SELECTOR, "h1.a-spacing-small")
driver.find_element(By.ID, "ap_customer_name")
driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "ap_password")
driver.find_element((By.CSS_SELECTOR, "div.a-alert-content")
driver.find_element(By.ID, "ap_password_check")
driver.find_element(By.ID, "continue")

#Condition of use
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_condition_of_use')]")

#Privacy notice
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice')]")

#Already have an account sign-in
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")


#Target test case that opens Target.com, clicks on cart icon and verify empty cart message
driver.get('https://www.target.com/')

#Click on shopping cart icon"
driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()

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
driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()

#verify sign-in form opened
actual_result = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text

assert expected_result in actual_result, f'{expected_result}, got actual {actual_result}'
print('Test case passed')

driver.quit()
