import services.utilities.blaze_driver as bu
import services.constructors.homepage_blaze_locators as bl1
import services.pages.blaze_homepage as bp1
import validators


class TestBlazeHome(bu.Drivers, bp1.HomePage):

    def test_Home_button(self):
        bp1.HomePage.home_button_click(self)
        assert validators.url('https://demoblaze.com/index.html')

    def test_button_change_picture(self):
        bp1.HomePage.home_button_click(self)
        bp1.HomePage.click_button_next_picture(self)
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.MainPageLocators.second_pic,)))
        assert self.my_driver.find_element(*bl1.MainPageLocators.second_pic,)

    def test_button_next(self):
        bp1.HomePage.click_button_next(self)
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.MainPageLocators.mc_img,)))
        assert self.my_driver.find_element(*bl1.MainPageLocators.mc_img,)

    def test_button_previous(self):
        bp1.HomePage.click_button_next(self)
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.MainPageLocators.mc_img,)))
        bp1.HomePage.click_button_previous(self)
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.MainPageLocators.first_page_image,)))
        assert self.my_driver.find_element(*bl1.MainPageLocators.first_page_image, )

    def test_first_button_header_picture(self):
        bp1.HomePage.click_button_for_second_pic_header(self)
        bp1.HomePage.click_button_for_first_pic_header(self)
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HeaderLocators.first_image,)))
        assert self.my_driver.find_element(*bl1.HeaderLocators.first_image,)

    def test_second_button_header_picture(self):
        bp1.HomePage.click_button_for_second_pic_header(self)
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HeaderLocators.second_image,)))
        assert self.my_driver.find_element(*bl1.HeaderLocators.second_image,)

    def test_third_button_header_picture(self):
        bp1.HomePage.click_button_for_third_pic_header(self)
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HeaderLocators.third_image,)))
        assert self.my_driver.find_element(*bl1.HeaderLocators.third_image,)

    def test_valid_LoggedIn(self):
        bp1.HomePage.log_in_site(self)
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl1.LogInLocators.user_exists,)))
        self.assertTrue(self.my_driver.find_element(*bl1.LogInLocators.user_exists, ))
