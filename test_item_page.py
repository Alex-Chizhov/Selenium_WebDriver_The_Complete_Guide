import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    wd.get("http://localhost/litecart/")
    request.addfinalizer(wd.quit)
    return wd

def test_item_on_hp_and_productp(driver):
    name_on_hp_page_text = driver.find_element_by_xpath("//div[@id='box-campaigns']//div[@class='name']").text
    old_price_hp_text = driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price']").text
    discount_price_hp_text = driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price']").text
    main_old_price_class_attribute = driver.find_element_by_xpath("//div[@id='box-campaigns']//s[@class='regular-price']").get_attribute("class")
    main_discount_price_class_attribute = driver.find_element_by_xpath("//div[@id='box-campaigns']//strong[@class='campaign-price']").get_attribute("class")

    driver.find_element_by_xpath("//div[@id='box-campaigns']//a").click()

    name_product_page_text = driver.find_element_by_xpath("//h1[@class='title']").text
    old_price_product_page_text = driver.find_element_by_xpath("//div[@id='box-product']//s[@class='regular-price']").text
    discount_price_product_page_text = driver.find_element_by_xpath("//div[@id='box-product']//strong[@class='campaign-price']").text
    product_old_price_class_attribute = driver.find_element_by_xpath("//div[@id='box-product']//s[@class='regular-price']").get_attribute("class")
    product_discount_price_class_attribute = driver.find_element_by_xpath("//div[@id='box-product']//strong[@class='campaign-price']").get_attribute("class")

    assert name_on_hp_page_text == name_product_page_text
    assert old_price_hp_text == old_price_product_page_text
    assert discount_price_hp_text == discount_price_product_page_text
    assert main_old_price_class_attribute == product_old_price_class_attribute
    assert main_discount_price_class_attribute == product_discount_price_class_attribute

