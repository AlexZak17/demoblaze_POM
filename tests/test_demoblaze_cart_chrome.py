import demoblaze_POM.services.utilities.blaze_driver as bu
import demoblaze_POM.services.pages.blaze_cart_page as cp
import demoblaze_POM.services.constructors.cart_blaze_locators as cl


class Cart(bu.Drivers, cp.Cart):

    def test_add_product_to_cart(self):
        self.my_driver.get('https://www.demoblaze.com/prod.html?idp_=1')
        cp.Cart.product1_add_to_cart_click(self)
        cp.Cart.accept_alert(self)
        cp.Cart.cart_header_button_click(self)
        cp.Cart.find_product_in_cart(self)
        self.assertIsNotNone(bu.EC.visibility_of_element_located((*cl.CartLocators.product1_added_to_cart,)))







