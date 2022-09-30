from selenium.webdriver.common.by import By
from behave import given, when, then


@given("open GetTop page")
def open_page(context):
    context.app.main_page.open_url()


@when("click the logo sign")
def click_logo(context):
    context.app.header.click_gettop_logo()


@then("verify logo is clickable")
def logo_clickable(context):
    context.app.header.logo_clickable()
