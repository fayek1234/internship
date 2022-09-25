from selenium.webdriver.common.by import By

from Pages.base_page import Page

class Header(Page):

    PRODUCT_TEXT = (By.CSS_SELECTOR, 'div.message-container')

    def added_product_cart(self):
        self.verify_element_text(*self.PRODUCT_TEXT)