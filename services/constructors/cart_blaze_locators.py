import services.utilities.blaze_driver as bu


class CartLocators(object):
    cart_header_button = (bu.By.XPATH, '//*[@id="cartur"]')
    product1_add_to_cart_button = (bu.By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
    product1_added_to_cart = (bu.By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
