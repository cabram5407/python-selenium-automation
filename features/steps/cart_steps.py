from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()

@then('Verify cart is empty')
def verify_cart_empty(context):
    actual_result=context.driver.find_element(By.XPATH,"//h1[text()='Your cart is empty']").text
    expected_result = 'Your cart is empty'
    assert expected_result in actual_result, f'Expected {expected_result}, got {actual_result}'