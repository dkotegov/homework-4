import os
import abc
import unittest
from time import sleep

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

from tests.dashboard_page import DashboardPage
from tests.general import Page, Component, AuthPage


class AccSettingsPage(Page):
    PATH = '/settings'

    @property
    def form(self):
        return AccSettingsForm(self.driver)


class AccSettingsForm(Component):
    FIRST_NAME = '//input[@name="firstName"]'
    SECOND_NAME = '//input[@name="secondName"]'
    EMAIL = '//input[@name="email"]'

    CHANGE_AVATAR = '//button[@type="button"]'
    SUBMIT = '//div[@class="field-group__fields "]/button[@type="submit"]'

    EDIT_SUCCESS = '//div[@class="response-text response-text-success"]'
    INPUT_ERROR = '//span[@class="text-field__error"][@style="display: block; visibility: visible;"]'

    def set_first_name(self, first_name):
        self.driver.find_element_by_xpath(self.FIRST_NAME).clear()
        self.driver.find_element_by_xpath(self.FIRST_NAME).send_keys(first_name)

    def set_second_name(self, second_name):
        self.driver.find_element_by_xpath(self.SECOND_NAME).clear()
        self.driver.find_element_by_xpath(self.SECOND_NAME).send_keys(second_name)

    def get_first_name(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.FIRST_NAME).get_attribute('value')
        )

    def get_second_name(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.SECOND_NAME).get_attribute('value')
        )

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def get_success_info(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.EDIT_SUCCESS).text
        )

    def get_input_error(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.INPUT_ERROR).text
        )


class AccSettingsTest(abc.ABC, unittest.TestCase):
    FIRST_NAME = None
    SECOND_NAME = None

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

        acc_settings_page = AccSettingsPage(self.driver)
        acc_settings_page.open()
        acc_settings_form = acc_settings_page.form
        acc_settings_form.get_first_name()

        self.change_settings(acc_settings_form)
        self.check(acc_settings_form)

    @abc.abstractmethod
    def check(self, acc_settings_form):
        return

    @abc.abstractmethod
    def change_settings(self, acc_settings_form):
        return


class FreelancerChangeSurnameTestValid(AccSettingsTest):
    SECOND_NAME = 'ROMANOV'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_second_name(self.SECOND_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        info = 'Изменения сохранены.'
        self.assertEqual(acc_settings_form.get_success_info(), info)


class FreelancerChangeSurnameTestInvalidTooShort(AccSettingsTest):
    SECOND_NAME = 'R'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_second_name(self.SECOND_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        error = 'Обычно фамилия так не выглядит. Это Ваша настоящая фамилия?'
        self.assertEqual(acc_settings_form.get_input_error(), error)


class FreelancerChangeSurnameTestInvalidTooLong(AccSettingsTest):
    SECOND_NAME = 'ROMANOVROMANOVROMANOVROMANOVROMANOVROMANOVROMANOVROMANOV'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_second_name(self.SECOND_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        info = 'Изменения сохранены.'
        self.assertEqual(acc_settings_form.get_success_info(), info)
        edited_surname = acc_settings_form.get_second_name()
        self.assertEqual(len(edited_surname), 20)
        self.assertEqual(edited_surname, self.SECOND_NAME[0:20])


class FreelancerChangeSurnameTestInvalidSpecialSymbols(AccSettingsTest):
    SECOND_NAME = 'Romanov--====+.'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_second_name(self.SECOND_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        error = 'Обычно фамилия так не выглядит. Это Ваша настоящая фамилия?'
        self.assertEqual(acc_settings_form.get_input_error(), error)


class FreelancerChangeSurnameTestInvalidNumbers(AccSettingsTest):
    SECOND_NAME = 'Romanov12344'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_second_name(self.SECOND_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        error = 'Обычно фамилия так не выглядит. Это Ваша настоящая фамилия?'
        self.assertEqual(acc_settings_form.get_input_error(), error)


class FreelancerChangeNameTestValid(AccSettingsTest):
    FIRST_NAME = 'ROMAN'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_first_name(self.FIRST_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        info = 'Изменения сохранены.'
        self.assertEqual(acc_settings_form.get_success_info(), info)


class FreelancerChangeNameTestInvalidTooShort(AccSettingsTest):
    FIRST_NAME = 'R'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_first_name(self.FIRST_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        error = 'Обычно имя так не выглядит. Это Ваше настоящая имя?'
        self.assertEqual(acc_settings_form.get_input_error(), error)


class FreelancerChangeNameTestInvalidTooLong(AccSettingsTest):
    FIRST_NAME = 'SERGEYSERGEYSERGEYSERGEYSERGEYSERGEYSERGEYSERGEYSERGEYSERGEYSERGEY'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_first_name(self.FIRST_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        info = 'Изменения сохранены.'
        self.assertEqual(acc_settings_form.get_success_info(), info)
        edited_name = acc_settings_form.get_first_name()
        self.assertEqual(len(edited_name), 20)
        self.assertEqual(edited_name, self.FIRST_NAME[0:20])


class FreelancerChangeNameTestInvalidSpecialSymbols(AccSettingsTest):
    FIRST_NAME = 'IVAN--====+.'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_first_name(self.FIRST_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        error = 'Обычно имя так не выглядит. Это Ваше настоящая имя?'
        self.assertEqual(acc_settings_form.get_input_error(), error)


class FreelancerChangeNameTestInvalidNumbers(AccSettingsTest):
    FIRST_NAME = 'IVAN12344'
    FREELANCER = True

    def change_settings(self, acc_settings_form):
        acc_settings_form.set_first_name(self.FIRST_NAME)
        acc_settings_form.submit()

    def check(self, acc_settings_form):
        error = 'Обычно имя так не выглядит. Это Ваше настоящая имя?'
        self.assertEqual(acc_settings_form.get_input_error(), error)



