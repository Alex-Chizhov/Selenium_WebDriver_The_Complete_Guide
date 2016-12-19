from test_cart_Page_Object.MainPage import MainPage


def test_cart(driver):
    main_page = MainPage(driver)
    main_page.open()
    for i in range(1, 4):
        product_page = main_page.click_to_product_number(i)
        product_page.put_product_into_cart()
        main_page = product_page.go_to_home_page()
    cart_page = main_page.go_to_checkout()
    cart_page.remove_all_items_from_cart()


