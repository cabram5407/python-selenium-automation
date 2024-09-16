 from selenium.webdriver.common.by import By
 from behave import given, when, then
 from time import sleep

 @when('Confirm Add to Cart - Side Navigation')
 def side_nav_click_add_to_cart(context):
     context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
     sleep(3)


 @then('Verify search results show {item}')
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
         assert expected_result == actual_result, f'Expected {expected_result}, got actual {actual_result}' \


 @ then('Verify header has {amount} links')
         def verify_header_links(context, amount):
             expected_amount = int(amount)
             links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
             assert len(links) == int(amount), f'Expected {amount} links, got {len(links)}'

 @then('Verify header is shown')
         def verify_header(context):
             context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_utilityHeaderContainer']")


 @then('Verify header has links')
 def verify_header_links(context):
     context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
     assert len(links) > 0