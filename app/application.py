from Pages.main_page import MainPage
from Pages.header import Header
from Pages.header1 import HeaderProduct
from Pages.product_page import Product

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.header1 = HeaderProduct(self.driver)
        self.product_page = Product(self.driver)