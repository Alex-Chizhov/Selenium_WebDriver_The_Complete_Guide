import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    wd.get("http://localhost/litecart/admin/")
    wd.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    wd.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    wd.find_element_by_xpath("//button[@name='login']").click()
    request.addfinalizer(wd.quit)
    return wd

def test_country(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    list_countries_elements = driver.find_elements_by_xpath("//td[@id='content']//td[5]/a")
    list_countries_names = []
    for country in list_countries_elements:
        list_countries_names.append(country.text)
    list_sorted = sorted(list_countries_names)
    assert list_countries_names == list_sorted

    list_countries_elements_with_zones = driver.find_elements_by_xpath("//td[@id='content']//td[6][string(text())>0]/preceding-sibling::td[1]/a")
    for elem in range(len(list_countries_elements_with_zones)):
        link = list_countries_elements_with_zones[elem]
        link.click()
        list_of_zones_elements = driver.find_elements_by_xpath("//table[@id='table-zones']//td[3]")
        list_of_zone_names = []
        for zone_link in list_of_zones_elements:
            list_of_zone_names.append(zone_link.text)
        list_of_zone_names.pop()
        list_sorted2 = sorted(list_of_zone_names)
        assert list_of_zone_names == list_sorted2
        driver.find_element_by_xpath("//button[@name='cancel']").click()
        list_countries_elements_with_zones = driver.find_elements_by_xpath("//td[@id='content']//td[6][string(text())>0]/preceding-sibling::td[1]/a")


def test_geo_zones(driver):
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    list_countries_elements = driver.find_elements_by_xpath("//td[@id='content']//td[3]/a")
    for elem in range(len(list_countries_elements)):
        link = list_countries_elements[elem]
        link.click()
        list_of_zones_elements = driver.find_elements_by_xpath("//table[@id='table-zones']//td[3]//option[@selected='selected']")
        list_of_zone_names = []
        for zone_link in list_of_zones_elements:
            list_of_zone_names.append(zone_link.text)
        list_geo_zone_sorted = sorted(list_of_zone_names)
        assert list_of_zone_names == list_geo_zone_sorted
        driver.find_element_by_xpath("//button[@name='cancel']").click()
        list_countries_elements = driver.find_elements_by_xpath("//td[@id='content']//td[3]/a")


