import pytest
import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope='session')
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    wd.get("http://localhost/litecart/admin/")
    wd.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    wd.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    wd.find_element_by_xpath("//button[@name='login']").click()
    request.addfinalizer(wd.quit)
    return wd

def test_add_item(driver):
    driver.find_element_by_xpath("//span[.='Catalog']").click()
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product']").click()
    driver.find_element_by_css_selector("input[type='radio'][value='1']").click()
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys("name item")
    driver.find_element_by_xpath("//input[@name='code']").send_keys("1414")
    driver.find_element_by_xpath("//input[@type='checkbox'][@value='1']").click()
    driver.find_element_by_xpath("//input[@name='product_groups[]'][@value='1-3']").click()
    driver.find_element_by_xpath("//input[@name='quantity']").send_keys("1000")
    photo = "F:\\GitHub\\photo.jpg"
    driver.find_element_by_xpath("//input[@name='new_images[]']").send_keys(photo)
    driver.find_element_by_xpath("//input[@name='date_valid_from']").send_keys('08 12 2016')
    driver.find_element_by_xpath("//input[@name='date_valid_to']").send_keys('08 12 2017')

    driver.find_element_by_xpath("//a[.='Information']").click()
    select1 = Select(driver.find_element_by_name('manufacturer_id'))
    select1.select_by_visible_text("ACME Corp.")
    driver.find_element_by_xpath("//input[@name='keywords']").send_keys('keywords')
    driver.find_element_by_xpath("//input[@name='short_description[en]']").send_keys('Short Description')
    driver.find_element_by_xpath("//div[@class='trumbowyg-editor']").send_keys('text')
    driver.find_element_by_xpath("//input[@name='head_title[en]']").send_keys('text')
    driver.find_element_by_xpath("//input[@name='meta_description[en]']").send_keys('text')

    driver.find_element_by_xpath("//a[.='Prices']").click()
    driver.find_element_by_xpath("//input[@name='purchase_price']").send_keys('10')
    select2 = Select(driver.find_element_by_name('purchase_price_currency_code'))
    select2.select_by_visible_text("US Dollars")
    driver.find_element_by_xpath("//input[@name='gross_prices[USD]']").send_keys('1')
    driver.find_element_by_xpath("//input[@name='gross_prices[EUR]']").send_keys('0.5')


    driver.find_element_by_xpath("//button[@name='save']").click()
    driver.find_element_by_xpath("//span[.='Catalog']").click()
    list_items = driver.find_elements_by_xpath("//form//td[3]/a")
    list_names = []
    for name in list_items:
        list_names.append(name.text)
    assert "name item" in list_names
