import services.utilities.blaze_driver as bu
from services.constructors import cart_blaze_locators as cl


class Cart:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def product1_add_to_cart_click(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*cl.CartLocators.product1_add_to_cart_button,))).click()

    def accept_alert(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.alert_is_present())
        alert = bu.Alert(self.my_driver)
        alert.accept()

    def cart_header_button_click(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*cl.CartLocators.cart_header_button,))).click()

    def find_product_in_cart(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*cl.CartLocators.product1_added_to_cart,)))

