import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver(request):
    wd = webdriver.Chrome()
    wd.get("http://localhost/litecart/admin/")
    wd.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    wd.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    wd.find_element_by_xpath("//button[@name='login']").click()
    request.addfinalizer(wd.quit)
    return wd

def test_logs_browser(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=2")
    list_item = driver.find_elements_by_xpath("//table//td[3]/a")
    for item in range(len(list_item)):
        item = driver.find_elements_by_xpath("//table//td[3]/a")[item]
        item.click()
        for l in driver.get_log("browser"):
            print(l)
        print(len(driver.get_log('browser')))
        driver.back()
