 from selenium.webdriver.common.by import By
 from behave import given, when, then
 from time import sleep


 @then('Verify search results shown {item}')
 def verify_results(context, item):
     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
     assert item == actual_result, f'Expected {item}, got actual {actual_result}'

 @then('Verify sign-in form shown')
     def verify_sign_in_form(context):
         actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
         expected_result = 'Sign into your Target account'
         assert expected_result == actual_result, f'Expected {expected_result}, got actual {actual_result}'


 @then('Verify 10 benefit links')
     def verify_benefit_links(context):
         actual_result = context.driver.find_element(By.CSS_SELECTOR,driver.find_elements(By.CSS_SELECTOR,"[data-component='Cells Component Container'] [class*='cell-item-content']").text
         expected_result = 'Sign into your Target account'
         assert expected_result == actual_result, f'Expected {expected_result}, got actual {actual_result}'