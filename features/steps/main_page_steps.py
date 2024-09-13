 from selenium.webdriver.common.by import By
 from behave import given, when, then
 from time import sleep


 @given('Open target main page')
 def open_main(context):
     context.driver.get('https://www.target.com/')


 @when('Click on cart icon')
 def cart_icon(context):
     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()


 @when('Search for a product')
 def search_product(context):
     # Search field => enter tea
     context.driver.find_element(By.ID, 'search').send_keys('{item}')
     # Search button => click
     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
     sleep(5)  # wait for search results page to load

 @when('Click on sign-in button')
     def sign_in_main(context):
         context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

 @when('From side navigation, click sign-in')
     def sign_in_side(context):
         context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
