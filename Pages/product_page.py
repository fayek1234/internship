from selenium.webdriver.common.by import By
from Pages.base_page import Page
from selenium.webdriver import ActionChains
import time
class Product(Page):


    PRODUCT_IMAGE = (By. CSS_SELECTOR, "div.product-small img.attachment-woocommerce_thumbnail")
    QUICK_VIEW = (By.XPATH, "//a[@data-prod='180']")
    BUTTON_CLICK =(By.XPATH, "//button[@class='mfp-close']")
    ADD_CART = (By.XPATH,"//button[text()='Add to cart']")
    CLICK_PRODUCT_IMAGE = (By. XPATH, "//span[text()='Xiaomi Redmi Note 11 Pro']")
    HOVER_OVER_LEFT_ARROW = (By.CSS_SELECTOR,'i.icon-angle-left')
    CLICK_LEFT_ARROW = (By. CSS_SELECTOR, 'i.icon-angle-left')
    CLICK_RIGHT_ARROW = (By. CSS_SELECTOR, 'i.icon-angle-right')
    ARROWS = (By.XPATH, "//div[@id='product-sidebar']/div/ul/li/a/i")

    def hover_over_product(self):
        product_image = self.find_element(*self. PRODUCT_IMAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(product_image)
        actions.perform()


    def click_quickview(self,):
        self.click(*self.QUICK_VIEW)


    def close_quickview(self,):
        time.sleep(5)
        self.click(*self.BUTTON_CLICK)


    def add_product(self,):
        self.click(*self.ADD_CART)


    def click_product(self,):
        self.click(*self.CLICK_PRODUCT_IMAGE)


    def hover_over_left_arrow(self):
        time.sleep(5)
        hover_over_left_arrow = self.find_elements(*self.ARROWS)
        # [Webelement1, webelement2]
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_over_left_arrow[0]).click().perform()
        # actions.perform()

    # def click_left_arrow(self,):
    #     self.click(*self.CLICK_LEFT_ARROW)


    def click_right_arrow(self):
        click_right_arrow = self.find_elements(*self.ARROWS)
        actions = ActionChains(self.driver)
        actions.double_click(click_right_arrow[1])
        actions.perform()


