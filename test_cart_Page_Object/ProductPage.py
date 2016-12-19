from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def choose_size(self, size):
        self.driver.find_element_by_xpath("//option[@value='%s']" % size).click()

    @property
    def quantity(self):
        return self.driver.find_element_by_xpath("//span[@class='quantity']")

    @property
    def size_dropdown_exists(self):
        return is_element_present(self.driver, By.XPATH, "//select[@name='options[Size]']")

    @property
    def home_link(self):
        return self.driver.find_element_by_xpath("//div[@class='content']//a[.='Home']")

    @property
    def add_button(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@name='add_cart_product']")))

    def put_product_into_cart(self):
        if self.size_dropdown_exists:
            self.choose_size('Small')
        items_in_cart = int(self.quantity.text)
        self.add_button.click()
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"), str(items_in_cart + 1)))

    def go_to_home_page(self):
        self.home_link.click()
        from test_cart_Page_Object.MainPage import MainPage
        return MainPage(self.driver)

