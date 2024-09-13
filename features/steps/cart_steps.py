from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty')
def verify_cart_empty(context):
    actual_result=context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg'] h1").text
    expected_result = 'Your cart is empty'
    assert expected_result == actual_result, f'Expected {expected_result}, got {actual_result}'