from Pages.page import Page
import os


class SettingPage(Page):
    AVATAR_PATH = os.getcwd() + '/media/vorobey.jpg'
    AVATAR_INPUT = '//input[@name="file"]'
    USERNAME_INPUT = os.environ['LOGIN']
    PASSWORD_INPUT = os.environ['PASSWORD']
    PATH = '/profileChange'
    USERNAME = '//input[@name="login"]'
    OLD = '//input[@placeholder="Старый пароль"]'
    NEW = '//input[@placeholder="Новый пароль"]'
    REPEAT = '//input[@placeholder="Повторите новый пароль"]'
    SUBMIT = '//button[text()="Сохранить"]'
    ERROR_MSG_MAIN = '//div[@id="badMain"]'
    ERROR_MSG_LOGIN = '//div[@id="badLogin"]'
    ERROR_MSG_PASSWORD = '//div[@id="badNewPassword"]'
    ERROR_MSG_DIFFERENT_NEW = '//div[@id="differentPassword"]'
    NOTIFICATION = '//span[@id="notification"]'

    def set_old_pass(self, old):
        self.driver.find_element_by_xpath(self.OLD).send_keys(old)

    def set_new_pass(self, new):
        self.driver.find_element_by_xpath(self.NEW).send_keys(new)

    def set_new_pass_confirm(self, new):
        self.driver.find_element_by_xpath(self.REPEAT).send_keys(new)

    def set_username(self, username):
        self.driver.find_element_by_xpath(self.USERNAME).send_keys(username + '\t')

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def get_main_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_MSG_MAIN).text

    def get_login_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_MSG_LOGIN).text

    def get_password_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_MSG_PASSWORD).text

    def get_password_diff_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_MSG_DIFFERENT_NEW).text

    def get_notification_text(self):
        return self.driver.find_element_by_xpath(self.NOTIFICATION).text

    def change_password(self, old, new, new_conf):
        self.set_old_pass(old)
        self.set_new_pass(new)
        self.set_new_pass_confirm(new_conf)
        self.submit()

    def change_username(self, username):
        self.set_username(username)
        self.submit()

    def setup_avatar(self):
        self.driver.find_element_by_xpath(self.AVATAR_INPUT).send_keys(self.AVATAR_PATH)

    def get_avatar_text(self):
        return self.driver.find_element_by_xpath(self.AVATAR_INPUT).get_attribute("value")
