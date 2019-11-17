import os
from pages.default_page import DefaultPage

from selenium.webdriver.support import expected_conditions as EC

class UserInfoPage(DefaultPage):

    FIRST_NAME = '#FirstName'
    LAST_NAME = '#LastName'
    NICK_NAME = '#NickName'

    DAY_INPUT = 'select[name="BirthDay"]'
    DAY_INPUT_CHILD = 'select[name="BirthDay"] option[value="20"]'
    MONTH_INPUT = 'select[name="BirthMonth"]'
    MONTH_INPUT_CHILD = 'select[name="BirthMonth"] option[value="12"]'
    YEAR_INPUT = 'select[name="BirthYear"]'
    YEAR_INPUT_CHILD = 'select[name="BirthYear"] option[value="1997"]'

    IMAGE_INPUT = 'input[name="avatar"]'
    SAVE_IMAGE_BUTTON = 'div[data-fire="save"]'

    LOGOUT_BUTTON = '#PH_logoutLink'
    HELP_BUTTON = '#settigns_toolbar__right  a.b-toolbar__btn'

    SUBMIT_BUTTON = 'div.form__actions__inner button[type="submit"]'

    OK_AFTER_SUBMIT_URI = 'https://e.mail.ru/settings?result=ok&afterReload=1'
    AFTER_LOGOUT_URI = 'https://mail.ru/?from=logout'
    LOGIN_URI = 'https://e.mail.ru/login\?.*'
    HELP_URI = 'https://help.mail.ru/mail-help/settings/userinfo'

    def get_image(self):
        return os.getenv("TESTIMAGE")

    def click_submit_button(self):
        self.click_element(self.SUBMIT_BUTTON, False)

    def input_firstname(self, firstName = 'test1'):
        self.clear_and_send_keys_to_input(self.FIRST_NAME, firstName, False)

    def input_lastname(self, lastName = 'test1'):
        self.clear_and_send_keys_to_input(self.LAST_NAME, lastName, False)

    def input_nickname(self, nickName = 'test1'):
        self.clear_and_send_keys_to_input(self.NICK_NAME, nickName, False)

    def wait_for_ok_after_submit(self):
        self.wait_redirect(self.OK_AFTER_SUBMIT_URI)

    def input_test_image(self):
        self.clear_and_send_keys_to_input(self.IMAGE_INPUT, self.get_image(), False, False)

    def click_save_image_button(self):
        self.click_element(self.SAVE_IMAGE_BUTTON, True)

    def open_settings_in_new_window(self):
        self.driver.execute_script('''window.open("https://e.mail.ru/settings?result=ok&afterReload=1","_blank");''')
        self.switch_to_window(1)

    def click_logout_button(self):
        self.click_element(self.LOGOUT_BUTTON, False)

    def wait_for_logout(self):
        self.wait_redirect(self.AFTER_LOGOUT_URI)

    def match_to_login_URI(self):
        self.wait(EC.url_matches(self.LOGIN_URI))

    def click_on_day_input(self):
        self.click_element(self.DAY_INPUT, False)

    def click_on_day_child_input(self):
        self.click_element(self.DAY_INPUT_CHILD, False)

    def click_on_month_input(self):
        self.click_element(self.MONTH_INPUT, False)

    def click_on_month_child_input(self):
        self.click_element(self.MONTH_INPUT_CHILD, False)

    def click_on_year_input(self):
        self.click_element(self.YEAR_INPUT, False)

    def click_on_year_child_input(self):
        self.click_element(self.YEAR_INPUT_CHILD, False)

    def click_on_help(self):
        self.click_element(self.HELP_BUTTON, False)

    def wait_for_help(self):
        self.wait_redirect(self.HELP_URI)