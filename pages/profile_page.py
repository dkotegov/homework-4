from pages.base_page import BasePage

from selenium.webdriver.common.action_chains import ActionChains


class ProfilePage(BasePage):
    PATH = '/user'

    EMAIL_INPUT = 'input[name="reserveEmail"]'
    NAME_INPUT = 'input[name="fullname"]'
    SAVE_BTN = 'input[type="submit"]'

    LOGOUT_BTN = '#logoutButton'
    CHANGE_PASSWORD_BTN = '#changePasswordButton'
    BACK_BTN = '.back-btn'

    AVATAR_COVER = '#avatarChange'
    AVATAR_IMAGE = '#avatarImage'

    EMAIL_ERROR = '#reserveEmailErrorText'

    def __init__(self, driver):
        super().__init__(driver, 'div.profile')

    def logout(self):
        self.open()
        self.click_logout_btn()

    def get_avatar_url(self):
        return self.locate_el(self.AVATAR_IMAGE).get_attribute('src')

    def set_email(self, email):
        self.set_field(self.EMAIL_INPUT, email)

    def set_name(self, name):
        self.set_field(self.NAME_INPUT, name)

    def click_avatar(self):
        el = self.locate_hidden_el(self.AVATAR_COVER)
        ActionChains(self.driver).move_to_element(el).perform()
        el.click()

    def click_save_btn(self):
        self.locate_el(self.SAVE_BTN).click()

    def click_logout_btn(self):
        self.locate_el(self.LOGOUT_BTN).click()

    def click_change_password_btn(self):
        self.locate_el(self.CHANGE_PASSWORD_BTN).click()

    def click_back_btn(self):
        self.locate_el(self.BACK_BTN).click()

    def get_email(self):
        return self.locate_el(self.EMAIL_INPUT).get_attribute('value')

    def get_name(self):
        return self.locate_el(self.NAME_INPUT).get_attribute('value')

    def get_email_error(self):
        return self.locate_el(self.EMAIL_ERROR).text
