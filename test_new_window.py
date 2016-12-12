import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from contextlib import contextmanager

@pytest.fixture(scope='session')
def driver(request):
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/admin/")
    wd.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    wd.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    wd.find_element_by_xpath("//button[@name='login']").click()
    request.addfinalizer(wd.quit)
    return wd


@contextmanager
def wait_for_new_window(driver, timeout=10):
    handles_before = driver.window_handles
    yield
    WebDriverWait(driver, timeout).until(
        lambda driver: len(handles_before) != len(driver.window_handles))



def test_link_in_new_window(driver):
    driver.find_element_by_xpath("//span[.='Countries']").click()
    list_countries = driver.find_elements_by_xpath("//table//td[5]/a")
    random.choice(list_countries).click()
    list_links = driver.find_elements_by_xpath("//i[@class='fa fa-external-link']")
    for link in list_links:
        with wait_for_new_window(driver):
            link.click()
        new_window = driver.window_handles[1]
        driver.switch_to_window(new_window)
        assert driver.title is not None
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

