 from selenium.webdriver.common.by import By
 from behave import given, when, then
 from time import sleep


 SEARCH_INPUT = (By.NAME, 'q')
 SEARCH_SUBMIT = (By.NAME, 'btnK')


 @given('Open Target Benefits page')
 def open_benefits(context):
     context.driver.get('https://www.target.com/circle')


 @when('Input {search_word} into search field')
 def input_search(context, search_word):
     search = context.driver.find_element(*SEARCH_INPUT)
     search.clear()
     search.send_keys(search_word)
     sleep(4)


 @when('Click on search icon')
 def click_search_icon(context):
     context.driver.find_element(*SEARCH_SUBMIT).click()
     sleep(1)


 @then('Product results for {search_word} are shown')
 def verify_found_results_text(context, search_word):
     assert search_word.lower() == context.driver.current_url.lower(), \
         f'Expected query not in {context.driver.current_url.lower()}'
