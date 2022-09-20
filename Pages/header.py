from selenium.webdriver.common.by import By

from Pages.base_page import Page

class Header(Page):
    CLICK_LOGO = (By.CSS_SELECTOR, 'img.header_logo')
    VERIFY_LOGO = (By.CSS_SELECTOR, "a[href='https://gettop.us/']")


    def click_logo(self,):
        self.click(*self.CLICK_LOGO).click()

    def verify_logo(self,):
        self.click(*self.VERIFY_LOGO).click()


