import services.utilities.blaze_driver as bu
import services.constructors.homepage_blaze_locators as bl1


class HomePage:
    def __init__(self, my_driver):
        self.my_driver = my_driver

    def log_in_site(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.LogInLocators.logIn_header_button,)))
        self.my_driver.find_element(*bl1.LogInLocators.logIn_header_button, ).click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.LogInLocators.username_field,)))
        username_field = self.my_driver.find_element(*bl1.LogInLocators.username_field, )
        username_field.send_keys('alex12345')
        password_field = self.my_driver.find_element(*bl1.LogInLocators.password_field, )
        password_field.send_keys('12345')
        self.my_driver.find_element(*bl1.LogInLocators.login_button, ).click()

    def home_button_click(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HeaderLocators.home_button,))).click()

    def click_button_next_picture(self):
        self.my_driver.find_element(*bl1.MainPageLocators.button_change_picture,).click()

    def click_button_next(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HeaderLocators.home_button,)))
        self.my_driver.find_element(*bl1.MainPageLocators.next_button, ).click()

    def click_button_previous(self):
        self.my_driver.find_element(*bl1.MainPageLocators.previous_button, ).click()

    def click_button_for_first_pic_header(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HeaderLocators.home_button,)))
        self.my_driver.find_element(*bl1.HeaderLocators.first_button_header_picture, ).click()

    def click_button_for_second_pic_header(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HeaderLocators.home_button,)))
        self.my_driver.find_element(*bl1.HeaderLocators.second_button_header_picture,).click()

    def click_button_for_third_pic_header(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HeaderLocators.home_button,)))
        self.my_driver.find_element(*bl1.HeaderLocators.third_button_header_picture,).click()