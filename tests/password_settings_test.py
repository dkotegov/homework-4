import os
import abc
import unittest
from time import sleep

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

from tests.dashboard_page import DashboardPage

from tests.general import Page, Component, AuthPage


class PasswordSettingsPage(Page):
    PATH = '/settings?tab=password'

    @property
    def form(self):
        return PasswordSettingsForm(self.driver)


class PasswordSettingsForm(Component):
    PASSWORD = '//input[@type="password"]'
    NEW_PASSWORD = '//input[@name="newPassword"]'
    NEW_PASSWORD_CONF = '//input[@name="newPasswordConfirmation"]'
    SUBMIT = '//form[@id="passwordChangeForm"]/div[@class="password-settings__submit"]/div[' \
             '@class="field-group"]//button[@type="submit"]'

    EDIT_SUCCESS = '//div[@class="response-text response-text-success"]'

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).clear()
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def set_new_password(self, password):
        self.driver.find_element_by_xpath(self.NEW_PASSWORD).clear()
        self.driver.find_element_by_xpath(self.NEW_PASSWORD).send_keys(password)

    def set_new_password_conf(self, password):
        self.driver.find_element_by_xpath(self.NEW_PASSWORD_CONF).clear()
        self.driver.find_element_by_xpath(self.NEW_PASSWORD_CONF).send_keys(password)

    def get_success_info(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.EDIT_SUCCESS).text
        )

    def click_on_button(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class PasswordSettingsTest(abc.ABC, unittest.TestCase):
    PASSWORD = None
    NEW_PASSWORD1 = None
    NEW_PASSWORD2 = None
    FREELANCER = None

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        if self.FREELANCER:
            auth_page.login_as_freelancer()
        else:
            auth_page.login_as_client()

    def tearDown(self):
        self.driver.quit()

    def test(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.dashboard.get_title()

        password_settings_page = PasswordSettingsPage(self.driver)
        password_settings_page.open()
        password_settings_form = password_settings_page.form
        sleep(3)
        #self.driver.implicitly_wait(10)

        self.change_settings(password_settings_form)
        self.check(password_settings_form)

    @abc.abstractmethod
    def check(self, password_settings_form):
        return

    def change_settings(self, password_settings_form):
        password_settings_form.set_password(self.PASSWORD)
        password_settings_form.set_new_password(self.NEW_PASSWORD1)
        password_settings_form.set_new_password_conf(self.NEW_PASSWORD2)
        password_settings_form.click_on_button()


class FreelancerChangePasswordTestValid(PasswordSettingsTest):
    PASSWORD = os.getenv('F_PASS') if os.getenv('F_PASS') else '123456' #'123456'
    NEW_PASSWORD1 = '1234567'
    NEW_PASSWORD2 = '1234567'
    FREELANCER = True

    def check(self, password_settings_form):
        self.assertEqual(password_settings_form.get_success_info(), 'Изменения сохранены.')
        sleep(3)
        password_settings_form.set_password(self.NEW_PASSWORD1)
        password_settings_form.set_new_password(self.PASSWORD)
        password_settings_form.set_new_password_conf(self.PASSWORD)
        password_settings_form.click_on_button()
        self.assertEqual(password_settings_form.get_success_info(), 'Изменения сохранены.')


class FreelancerChangePasswordTestInvalidWrongPassword(PasswordSettingsTest):
    PASSWORD = 'ddffdf'
    NEW_PASSWORD1 = '654321'
    NEW_PASSWORD2 = '654321'
    FREELANCER = True

    def check(self, password_settings_form):
        return


class FreelancerChangePasswordTestInvalidDiffPasswords(PasswordSettingsTest):
    PASSWORD = os.getenv('F_PASS') if os.getenv('F_PASS') else '123456' #'123456'
    NEW_PASSWORD1 = '1234567'
    NEW_PASSWORD2 = '123456789'
    FREELANCER = True

    def check(self, password_settings_form):
        return


class ClientChangePasswordTestValid(PasswordSettingsTest):
    PASSWORD = os.getenv('C_PASS') if os.getenv('C_PASS') else '123456' #'123456'
    NEW_PASSWORD1 = '1234567'
    NEW_PASSWORD2 = '1234567'
    FREELANCER = False

    def check(self, password_settings_form):
        self.assertEqual(password_settings_form.get_success_info(), 'Изменения сохранены.')
        sleep(3)
        password_settings_form.set_password(self.NEW_PASSWORD1)
        password_settings_form.set_new_password(self.PASSWORD)
        password_settings_form.set_new_password_conf(self.PASSWORD)
        password_settings_form.click_on_button()
        self.assertEqual(password_settings_form.get_success_info(), 'Изменения сохранены.')


class ClientChangePasswordTestInvalidWrongPassword(PasswordSettingsTest):
    PASSWORD = 'ddffdf'
    NEW_PASSWORD1 = '654321'
    NEW_PASSWORD2 = '654321'
    FREELANCER = False

    def check(self, password_settings_form):
        return


class ClientChangePasswordTestInvalidDiffPasswords(PasswordSettingsTest):
    PASSWORD = os.getenv('C_PASS') if os.getenv('C_PASS') else '123456' #'123456'
    NEW_PASSWORD1 = '1234567'
    NEW_PASSWORD2 = '123456789'
    FREELANCER = False

    def check(self, password_settings_form):
        return
