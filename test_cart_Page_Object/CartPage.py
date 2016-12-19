from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/admin")
        return self

    @property
    def quantity(self):
        return self.driver.find_element_by_xpath("//span[@class='quantity']")

    @property
    def table_order_summary_exists(self):
        return is_element_present(self.driver, By.XPATH, "//div[@id='box-checkout-summary']")

    @property
    def removing_duck_element(self):
        return self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//button[@name='remove_cart_item']//preceding::p//strong")))

    @property
    def remove_button(self):
        return self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button[@name='remove_cart_item']")))

    def remove_all_items_from_cart(self):
        while self.table_order_summary_exists:
            removing_duck_name = self.removing_duck_element.text
            xpath = "//div[@id='box-checkout-summary']//td[.='" + removing_duck_name + "']"
            duck_in_table = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.remove_button.click()
            self.wait.until(EC.staleness_of(duck_in_table))


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False
