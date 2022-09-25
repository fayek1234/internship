from selenium.webdriver.common.by import By
from Pages.base_page import Page
from selenium.webdriver import ActionChains
class Product(Page):


    PRODUCT_IMAGE = (By. CSS_SELECTOR, 'img.attachment-woocommerce_thumbnail ')
    QUICK_VIEW = (By.XPATH, "//a[@data-prod='180']")
    BUTTON_CLICK = (By.CSS_SELECTOR, 'button.mfp-close')
    ADD_CART = (By.CSS_SELECTOR, 'button.single_add_to_cart_button')
    CLICK_PRODUCT_IMAGE = (By. XPATH, "//span[text()='Xiaomi Redmi Note 11 Pro']")
    HOVER_OVER_LEFT_ARROW = (By.CSS_SELECTOR, 'i.icon-angle-left')
    CLICK_LEFT_ARROW = (By. CSS_SELECTOR, 'i.icon-angle-left')
    CLICK_RIGHT_ARROW = (By. CSS_SELECTOR, 'i.icon-angle-right')

    def hover_over_product(self):
        product_image = self.find_elements(*self. PRODUCT_IMAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(product_image)
        actions.perform()


    def click_quickview(self, ):
        self.click(*self.QUICK_VIEW).click()

    def close_quickview(self, ):
        self.click(*self.BUTTON_CLICK).click()

    def add_product(self, ):
            self.click(*self.ADD_CART).click()

    def click_product(self, ):
        self.click(*self.CLICK_PRODUCT_IMAGE).click()

    def hover_over_left_arrow(self):
        hover_over_left_arrow = self.find_elements(*self.  HOVER_OVER_LEFT_ARROW)
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_over_left_arrow)
        actions.perform()

    def click_left_arrow(self, ):
        self.click(*self.CLICK_LEFT_ARROW).click()

    def click_right_arrow(self):
        click_right_arrow = self.find_elements(*self.  CLICK_RIGHT_ARROW)
        actions = ActionChains(self.driver)
        actions.double_click(click_right_arrow)
        actions.perform()


