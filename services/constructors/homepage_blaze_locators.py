import services.utilities.blaze_driver as bu

# # # # # LOCATORS - We use these to tidy up our code and save time searching for elements # # # # # #


class HeaderLocators(object):
    home_button = (bu.By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a')
    first_button_header_picture = (bu.By.XPATH, '/html/body/nav/div[2]/div/ol/li[1]')
    first_image = (bu.By.XPATH, '/html/body/nav/div[2]/div/ol/li[1]')
    second_button_header_picture = (bu.By.XPATH, '/html/body/nav/div[2]/div/ol/li[2]')
    second_image = (bu.By.XPATH, '/html/body/nav/div[2]/div/div/div[2]/img')
    third_button_header_picture = (bu.By.XPATH, '/html/body/nav/div[2]/div/ol/li[3]')
    third_image = (bu.By.XPATH, '/html/body/nav/div[2]/div/div/div[3]/img')


class MainPageLocators(object):
    button_change_picture = (bu.By.XPATH, '/html/body/nav/div[2]/div/a[2]')
    second_pic = (bu.By.XPATH, '/html/body/nav/div[2]/div/div/div[2]/img')
    next_button = (bu.By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[2]/button')
    mc_img = (bu.By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')
    previous_button = (bu.By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[1]/button')
    first_page_image = (bu.By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')


class LogInLocators(object):
    logIn_header_button = (bu.By.XPATH, '/html/body/nav/div[1]/ul/li[5]/a')
    username_field = (bu.By.ID, 'loginusername')
    password_field = (bu.By.ID, 'loginpassword')
    login_button = (bu.By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    user_exists = (bu.By.ID, "nameofuser")
