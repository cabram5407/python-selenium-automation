from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#Target product search test case
@then('Verify item in cart')
def verify_cart_item(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-qty']").text
    assert expected_result == actual_result, f'Expected {expected_result}, got {actual_result}'


@then('Verify Cart Empty message shown')
def verify_empty_cart(context):
    context.app.cart_page.verify_empty_cart()
