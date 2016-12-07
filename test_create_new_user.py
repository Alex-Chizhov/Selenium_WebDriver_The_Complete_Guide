import pytest
import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope='session')
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    wd.get("http://localhost/litecart/")
    request.addfinalizer(wd.quit)
    return wd


def random_list():
    psw = ''
    for x in range(8):
        psw = psw + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    return psw


def test_create_new_user(driver):
    driver.find_element_by_xpath("//form//a").click()
    driver.find_element_by_xpath("//input[@name='tax_id']").send_keys(random_list())
    driver.find_element_by_xpath("//input[@name='company']").send_keys(random_list())
    driver.find_element_by_xpath("//input[@name='firstname']").send_keys(random_list())
    driver.find_element_by_xpath("//input[@name='lastname']").send_keys(random_list())
    driver.find_element_by_xpath("//input[@name='address1']").send_keys(random_list())
    driver.find_element_by_xpath("//input[@name='address2']").send_keys(random_list())
    driver.find_element_by_xpath("//input[@name='postcode']").send_keys("87875")
    driver.find_element_by_xpath("//input[@name='city']").send_keys(random_list())

    select1 = Select(driver.find_element_by_name('country_code'))
    select1.select_by_visible_text("United States")
    select2 = Select(driver.find_element_by_xpath("//select[@name='zone_code']"))
    select2.select_by_index(3)

    email = (random_list()+"@gmail.com")
    password = ("56564tFe466eR")
    #print(email)
    driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
    driver.find_element_by_xpath("//input[@name='phone']").send_keys("89163756780")
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//input[@name='confirmed_password']").send_keys(password)
    driver.find_element_by_xpath("//button[@name='create_account']").click()
    #time.sleep(5)

    driver.find_element_by_xpath("//aside//li[4]/a").click()
    driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@name='login']").click()
    driver.find_element_by_xpath("//aside//li[4]/a").click()
