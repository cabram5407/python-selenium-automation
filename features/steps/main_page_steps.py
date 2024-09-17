 from selenium.webdriver.common.by import By
 from behave import given, when, then
 from time import sleep

@given('Open Target Help page')
def help_page(context):
    context.driver.get('https://help.target.com/help')


 @given('Open target main page')
 def open_main(context):
     context.driver.get('https://www.target.com/')

#Target Circle page
@given('Open target Benefits page')
     def open_benefits(context):
         context.driver.get('https://www.target.com/circle')


 @when('Click on cart icon')
 def click_cart(context):
     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()

#Target product search test case
 @when('Search for {item}')
 def search_product(context, item):
     context.driver.find_element(By.ID, 'search').send_keys(item)
     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()


 @when('Click search button')
 def click_search(context):
     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
     sleep(5)  # wait for search results page to load


@when('Add item to cart')
def add_item(context):
    context.driver.find_element(BY.CSS_Selector, "[data-test='chooseOptionsButton'.'chooseOptionsButton']").click()


 @when('Click on sign-in button')
     def sign_in_main(context):
         context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()


 @when('From side navigation, click sign-in')
     def sign_in_side(context):
         context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()


 @when('Click on Target Benefits Tab')
 def search_word(context):
         context.driver.find_element(By.CSS_SELECTOR, "#utilityNav-circle").click()






