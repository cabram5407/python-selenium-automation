from IPython.utils.coloransi import value
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import numpy

#installs chrome driver
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)

#starts the browser you are using
driver: WebDriver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(4)

#Target test case that opens Target.com, clicks on cart icon and verify empty cart message
driver.get('https://www.target.com/circle')

#Click on Target Circle - top navigation"
driver.find_element(By.CSS_SELECTOR, "#utilityNav-circle").click()

#Verify Target 360 Benefits page.
driver.find_element(By.XPATH, "//*[@aria-label='Target circle TM']").text


#Verify Target has 10 benefits present (CSS Selector)
driver.find_element(By.CSS_SELECTOR,"[data-test='filmstrip']")
driver.find_element(By.CSS_SELECTOR,"[@class='sc-fb3945a7-1 coTiYO']")




