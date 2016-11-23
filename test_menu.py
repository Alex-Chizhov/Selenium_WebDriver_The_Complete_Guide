from selenium import webdriver
wd = webdriver.Chrome()



wd.get('http://localhost/litecart/admin')
wd.find_element_by_name("username").send_keys("admin")
wd.find_element_by_name("password").send_keys("admin")
wd.find_element_by_name("login").click()


lst = ["Appearence","Logotype", "Catalog", "Product Groups", "Option Groups","Manufacturers","Suppliers",
       "Delivery Statuses","Sold Out Statuses", "Quantity Units", "CSV Import/Export", "Countries","Currencies","Customers",
       "CSV Import/Export","Newsletter", "Geo Zones", "Languages", "Storage Encoding","Modules","Customer",
       "Shipping","Payment", "Order Total", "Order Success", "Order Action","Orders",
       "Order Statuses","Pages", "Reports", "Most Sold Products", "Most Shopping Customers","Settings","Defaults",
       "General","Listings", "Images", "Checkout", "Advanced","Security","Slides","Tax","Tax Rates","Translations",
       "Scan Files","CSV Import/Export", "Users", "vQmods"]

for item in lst:
    wd.find_element_by_link_text(item).click()
    assert wd.title != None


wd.quit()