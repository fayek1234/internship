from selenium.webdriver.common.by import By
from behave import given, when, then


@given("open GetTop page")
def open_page(context):
    context.app.main_page.open_GetTop_page()



@when("click the logo sign")
def click_logo(context):
    context.app.header.click_logo()


@then("verify logo is clickable")
def verify_logo_clickable(context):
    context.app.header.verify_logo()