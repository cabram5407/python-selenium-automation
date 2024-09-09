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