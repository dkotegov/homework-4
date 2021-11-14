from tests.pages.base import Page
from components.navbar import NavbarComponent


class ProfilePage(Page):
    """
    Стриница профиля
    """

    PHONE = '//input[@name="number"]'
    EMAIL = '//input[@name="email"]'
    CUR_PASSWORD = '//input[@name="password_current"]'
    NEW_PASSWORD = '//input[@name="password"]'
    REPEAT_PASSWORD = '//input[@name="password_repeat"]'
    SAVE = '//input[@type="submit"]'
    AVATAR = '//button[@id="input-avatar-button"]'

    ERROR_PHONE = '//p[@id="numberError"]'
    ERROR_EMAIL = '//p[@id="emailError"]'
    ERROR_CUR_PASSWORD = '//p[@id="password_currentError"]'
    ERROR_NEW_PASSWORD = '//p[@id="passwordError"]'
    ERROR_REPEAT_PASSWORD = '//p[@id="password_repeatError"]'

    def __init__(self, driver):
        self.PATH = 'profile/edits'
        super(ProfilePage, self).__init__(driver)

    @property
    def navbar(self):
        return NavbarComponent(self.driver)

    def set_phone(self, phone):
        elem = self.driver.find_element_by_xpath(self.PHONE)
        elem.clear()
        elem.send_keys(phone)

    def set_email(self, email):
        elem = self.driver.find_element_by_xpath(self.EMAIL)
        elem.clear()
        elem.send_keys(email)

    def set_current_password(self, password):
        elem = self.driver.find_element_by_xpath(self.CUR_PASSWORD)
        elem.clear()
        elem.send_keys(password)

    def set_new_password(self, password):
        elem = self.driver.find_element_by_xpath(self.NEW_PASSWORD)
        elem.clear()
        elem.send_keys(password)

    def set_repeat_password(self, password):
        elem = self.driver.find_element_by_xpath(self.REPEAT_PASSWORD)
        elem.clear()
        elem.send_keys(password)

    def add_avatar(self):
        self.driver.find_element_by_xpath(self.AVATAR).click()

    def click_save(self):
        self.driver.find_element_by_xpath(self.SAVE).click()

    def get_phone_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_PHONE).text

    def get_email_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_EMAIL).text

    def get_cur_pass_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_CUR_PASSWORD).text

    def get_new_pass_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_NEW_PASSWORD).text

    def get_repeat_pass_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_REPEAT_PASSWORD).text
