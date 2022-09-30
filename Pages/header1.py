from selenium.webdriver.common.by import By

from Pages.base_page import Page
import time

class HeaderProduct(Page):

    PRODUCT_TEXT = (By.CSS_SELECTOR, 'div.message-container')

    def added_product_cart(self):
        time.sleep(4)
        self.find_element(*self.PRODUCT_TEXT)

