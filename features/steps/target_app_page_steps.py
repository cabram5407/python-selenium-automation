from behave import given, when, then

@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()


@given ('Open Sign-in Page')
def open_sign_in(context):
    context.app.target_app_page.open_sign_in_page()


@given('Store original window')
def store_window(context):
    context.original_window = context.app.target_app_page.get_current_window()
    print('Original window: ', context.original_window)


@when('Click Target Terms and Conditions link')
def click_terms_link(context):
    context.app.target_app_page.click_terms_link()


@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()


@when('Switch to new window')
def switch_to_window(context):
    context.app.target_app_page.switch_to_new_window()


@then('Verify Terms and Conditions page opened')
def verify_terms_page_opened(context):
    context.app.target_app_page.verify_terms_page_opened()


@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.target_app_page.verify_pp_opened()


@then('Close current page')
def close_page(context):
    context.app.target_app_page.close()


@then('Return to original window')
def switch_to_original(context):
    context.app.target_app_page.switch_to_window_by_id(context.original_window)