from selenium import webdriver
wd = webdriver.Chrome()

wd.get('http://localhost/litecart/admin')
wd.find_element_by_name("username").send_keys("admin")
wd.find_element_by_name("password").send_keys("admin")
wd.find_element_by_name("login").click()


menu = wd.find_elements_by_css_selector('span.name')
print (len(menu))


for elem in range(1, len(menu)+1):
    wd.find_element_by_css_selector('li#app-:nth-child({})'.format(elem)).click()
    assert wd.title is not None
    menu2 = wd.find_elements_by_css_selector("li[id*=doc]")
    for elem in range(1, len(menu2)+1):
        wd.find_element_by_css_selector('li[id*=doc]:nth-child({})'.format(elem)).click()
        assert wd.title is not None

wd.quit()