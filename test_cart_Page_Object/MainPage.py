from selenium.webdriver.support.wait import WebDriverWait
from test_cart_Page_Object.ProductPage import ProductPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/")
        return self

    @property
    def checkout_link(self):
        return self.driver.find_element_by_xpath("//div[@id='cart']//a[.='Checkout »']")

    def click_to_product_number(self, x):
        self.driver.find_element_by_xpath("//li[%x]//a[@class='link']" % x).click()
        return ProductPage(self.driver)

    def go_to_checkout(self):
        self.checkout_link.click()
        from test_cart_Page_Object.CartPage import CartPage
        return CartPage(self.driver)
