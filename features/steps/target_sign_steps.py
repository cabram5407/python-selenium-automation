from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on sign-in button')
def sign_in_main(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()

@when('From side navigation, click sign-in')
def sign_in_side(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()


@then('Verify ign-in form opened')
def verify_sign_in_form(context):
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    expected_result ='Sign into your Target account'
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'