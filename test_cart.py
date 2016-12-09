import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='session')
def driver(request):
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/")
    request.addfinalizer(wd.quit)
    return wd

def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


def test_cart(driver):
    wait = WebDriverWait(driver, 10)

    for i in range(1,4):
        driver.find_element_by_xpath("//li[@class='product column shadow hover-light']").click()
        if is_element_present(driver, By.XPATH, "//option[@value='Small']"):
            driver.find_element_by_xpath("//option[@value='Small']").click()
        number_items_in_cart = int(driver.find_element_by_xpath("//span[@class='quantity']").text)
        driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"), str(number_items_in_cart + 1)))
        driver.find_element_by_xpath("//a[.='Home']").click()

    #time.sleep(5)
    driver.find_element_by_xpath("//a[.='Checkout »']").click()
    while is_element_present(driver, By.XPATH, "//div[@id='box-checkout-summary']"):
        removing_item = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@name='remove_cart_item']//preceding::p//strong")))
        removing_item_name = removing_item.text
        xpath = "//div[@id='box-checkout-summary']//td[.= '" + removing_item_name + "']"
        item_in_table = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        remove_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@name='remove_cart_item']")))
        remove_button.click()
        wait.until(EC.staleness_of(item_in_table))





