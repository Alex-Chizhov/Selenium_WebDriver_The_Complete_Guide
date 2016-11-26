from selenium import webdriver
wd = webdriver.Chrome()

wd.get("http://localhost/litecart/")

goods = wd.find_elements_by_css_selector("li[class*=product]")
for item in goods:
    stickers = len(item.find_elements_by_css_selector("div[class*=sticker]"))
    assert stickers == 1

wd.quit()