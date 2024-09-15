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

#open Target help page
driver.get('https://help.target.com/help')

#Verify elements are present
driver.get.find_element(By.CSS_SELECTOR, "[class='custom-h2']").click()

#search input field
driver.get.find_element(By.CSS_SELECTOR, "[id='j_id0:j_id2:j_id32:name']".click()
driver,get.find_element(By.CSS_SELECTOR, "[class='btn-sm search-btn']".click()

#what would you like to do boxes (10)
driver.get.find.element(By.CSS_SELECTOR, "[class*='grid_6']").click()
driver.get.find.element(BY.CSS_SELECTOR, "[class*='grid_4 boxSmallr txtAC bigbox2']").click()

#pruduct recalls and contact us
driver.get.find.element(By.CSS_SELECTOR, "[class*='grid_6']").click()

#browse all help pages
driver.get.find.element(By.CSS_SELECTOR, "//*[text()='Browse all Help pages']")

