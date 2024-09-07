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
driver.find_element(By.XPATH, "//*[text()='Account & Lists' and @class='nav-line-2 ']")

#Click on Creat Account button
driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit")

driver.find_element(By.XPATH, "//h1[@class='a-spacing-small')
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
driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon')").click

sleep(10)

#Verification that cart is empty.
actual_result=driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text

#verify is true but if false it will fail.
assert expected_result in actual_result, f'{expected_result}, got actual {actual_result}'
print('Test case passed')
driver.quit()

#Target test case to verify a user log out and user can navigate to sign-in.

