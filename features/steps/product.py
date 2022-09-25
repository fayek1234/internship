from selenium.webdriver.common.by import By
from behave import given, when, then


@when("hover over a product")
def hover_over_product(context):
    context.app.product_page.hover_over_product()


@then("click quick view")
def click_quickview(context):
    context.app.product_page.click_quickview()



@then("close quick view by clicking on X")
def close_quickview(context):
    context.app.product_page.close_quickview()



@then("add product to cart")
def add_product(context):
    context.app.product_page.add_product()


@then("added product text showen")
def added_product_cart(context):
    context.app.header1.added_product_cart()


