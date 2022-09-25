from selenium.webdriver.common.by import By
from behave import given, when, then



@when("click on product image")
def click_product(context):
    context.app.product_page.click_product()


@then("hover over left arrow")
def hover_over_arrow(context):
    context.app.product_page.hover_over_left_arrow()


@then("click on left arrow")
def click_left_arrow(context):
    context.app.product_page.click_left_arrow()


@then("click on right arrow 2 times")
def click_right_arrow(context):
    context.app.product_page.click_right_arrow()