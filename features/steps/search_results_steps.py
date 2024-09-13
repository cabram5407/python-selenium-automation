 from selenium.webdriver.common.by import By
 from behave import given, when, then
 from time import sleep


 @then('Verify search results show {item}')
 def verify_results(context, item):
     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
     assert item == actual_result, f'Expected {item}, got actual {actual_result}'

 @then('Verify sign-in form shown')
     def verify_sign_in_form(context):
         actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
         expected_result = 'Sign into your Target account'
         assert expected_result == actual_result, f'Expected {expected_result}, got actual {actual_result}'