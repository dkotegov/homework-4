import os
import abc
import unittest
from time import sleep

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

from tests.dashboard_page import DashboardPage
from tests.general import Page, Component, AuthPage


class ClientSettingPage(Page):
    PATH = '/settings?tab=company'

    @property
    def form(self):
        return ClientSettingForm(self.driver)


class ClientSettingForm(Component):
    NAME = '//input[@name="companyName"]'
    SITE = '//input[@name="site"]'
    TITLE = '//input[@name="tagline"]'
    DESCRIPTION = '//textarea[@name="description"]'

    ADDRESS = '//input[@name="address"]'
    PHONE = '//input[@name="phone"]'

    DESC_BUTTON = '//form[@id="companySettingsForm"]/div[5]//button[@type="submit"]'
    CONTACT_BUTTON = '//form[@id="companyContactsForm"]/div[4]//button[@type="submit"]'

    EDIT_SUCCESS = '//div[@class="response-text response-text-success"]'
    INPUT_ERROR = '//span[@class="text-field__error"][@style="display: block; visibility: visible;"]'

    def set_name(self, name):
        self.driver.find_element_by_xpath(self.NAME).clear()
        self.driver.find_element_by_xpath(self.NAME).send_keys(name)

    def set_site(self, site):
        self.driver.find_element_by_xpath(self.SITE).clear()
        self.driver.find_element_by_xpath(self.SITE).send_keys(site)

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE).clear()
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_description(self, desc):
        self.driver.find_element_by_xpath(self.DESCRIPTION).clear()
        self.driver.find_element_by_xpath(self.DESCRIPTION).send_keys(desc)

    def set_address(self, address):
        self.driver.find_element_by_xpath(self.ADDRESS).clear()
        self.driver.find_element_by_xpath(self.ADDRESS).send_keys(address)

    def set_phone(self, phone):
        self.driver.find_element_by_xpath(self.PHONE).clear()
        self.driver.find_element_by_xpath(self.PHONE).send_keys(phone)

    def get_success_info(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.EDIT_SUCCESS).text
        )

    def get_input_error(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.INPUT_ERROR).text
        )

    def get_name(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.NAME).get_attribute('value')
        )

    def get_site(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.SITE).get_attribute('value')
        )

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.TITLE).get_attribute('value')
        )

    def get_address(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.ADDRESS).get_attribute('value')
        )

    def click_on_desc_button(self):
        self.driver.find_element_by_xpath(self.DESC_BUTTON).click()

    def click_on_contact_button(self):
        self.driver.find_element_by_xpath(self.CONTACT_BUTTON).click()


class ClientSettingsTest(abc.ABC, unittest.TestCase):
    MAX_NAME_LEN = 20
    MAX_SITE_LEN = 30
    MAX_TITLE_LEN = 60
    MAX_ADDRESS_LEN = 40

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login_as_client()

    def tearDown(self):
        self.driver.quit()

    def test(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.dashboard.get_title()

        client_settings_page = ClientSettingPage(self.driver)
        client_settings_page.open()
        client_settings_form = client_settings_page.form
        # self.driver.implicitly_wait(10)
        sleep(3)

        self.change_settings(client_settings_form)
        self.check(client_settings_form)

    @abc.abstractmethod
    def check(self, client_settings_form):
        return

    @abc.abstractmethod
    def change_settings(self, client_settings_form):
        return


class ClientSettingsChangeCompanyTestValid(ClientSettingsTest):
    NAME = 'ОАО "МАРС"'
    SITE = 'oaomars.ru'
    TITLE = 'КОПАНИЯ "МАРС"'
    DESCRIPTION = 'Мы занимаемся разработкой сайтов. В нашей компании уже 500 человек.'

    def check(self, client_settings_form):
        client_settings_form.get_success_info()

    def change_settings(self, client_settings_form):
        client_settings_form.set_name(self.NAME)
        client_settings_form.set_site(self.SITE)
        client_settings_form.set_title(self.TITLE)
        client_settings_form.set_description(self.DESCRIPTION)
        client_settings_form.click_on_desc_button()


class ClientSettingsChangeCompanyTestInvalidTooShortName(ClientSettingsTest):
    NAME = 'ОА'
    SITE = 'oaomars.ru'
    TITLE = 'КОПАНИЯ "МАРС"'
    DESCRIPTION = 'Мы занимаемся разработкой сайтов. В нашей компании уже 500 человек.'

    def check(self, client_settings_form):
        error = 'Просим написать 3 и более символов. Сейчас у Вас 2 символов.'
        self.assertEqual(client_settings_form.get_input_error(), error)

    def change_settings(self, client_settings_form):
        client_settings_form.set_name(self.NAME)
        client_settings_form.set_site(self.SITE)
        client_settings_form.set_title(self.TITLE)
        client_settings_form.set_description(self.DESCRIPTION)
        client_settings_form.click_on_desc_button()


class ClientSettingsChangeCompanyTestInvalidTooLongName(ClientSettingsTest):
    NAME = 'О' * 100
    SITE = 'oaomars.ru'
    TITLE = 'КОПАНИЯ "МАРС"'
    DESCRIPTION = 'Мы занимаемся разработкой сайтов. В нашей компании уже 500 человек.'

    def check(self, client_settings_form):
        self.assertEqual(len(client_settings_form.get_name()), self.MAX_NAME_LEN)
        client_settings_form.get_success_info()

    def change_settings(self, client_settings_form):
        client_settings_form.set_name(self.NAME)
        client_settings_form.set_site(self.SITE)
        client_settings_form.set_title(self.TITLE)
        client_settings_form.set_description(self.DESCRIPTION)
        client_settings_form.click_on_desc_button()


class ClientSettingsChangeCompanyTestInvalidTooShortSite(ClientSettingsTest):
    NAME = 'ОАО МАРС'
    SITE = 'oa'
    TITLE = 'КОПАНИЯ "МАРС"'
    DESCRIPTION = 'Мы занимаемся разработкой сайтов. В нашей компании уже 500 человек.'

    def check(self, client_settings_form):
        error = 'Просим написать 5 и более символов. Сейчас у Вас 2 символов.'
        self.assertEqual(client_settings_form.get_input_error(), error)

    def change_settings(self, client_settings_form):
        client_settings_form.set_name(self.NAME)
        client_settings_form.set_site(self.SITE)
        client_settings_form.set_title(self.TITLE)
        client_settings_form.set_description(self.DESCRIPTION)
        client_settings_form.click_on_desc_button()


class ClientSettingsChangeCompanyTestInvalidTooLongSite(ClientSettingsTest):
    NAME = 'ОАО МАРС'
    SITE = 'o' * 200
    TITLE = 'КОПАНИЯ "МАРС"'
    DESCRIPTION = 'Мы занимаемся разработкой сайтов. В нашей компании уже 500 человек.'

    def check(self, client_settings_form):
        self.assertEqual(len(client_settings_form.get_site()), self.MAX_SITE_LEN)
        client_settings_form.get_success_info()

    def change_settings(self, client_settings_form):
        client_settings_form.set_name(self.NAME)
        client_settings_form.set_site(self.SITE)
        client_settings_form.set_title(self.TITLE)
        client_settings_form.set_description(self.DESCRIPTION)
        client_settings_form.click_on_desc_button()


class ClientSettingsChangeCompanyTestInvalidTooShortTitle(ClientSettingsTest):
    NAME = 'ОАО МАРС'
    SITE = 'oaomars.ru'
    TITLE = 'КО'
    DESCRIPTION = 'Мы занимаемся разработкой сайтов. В нашей компании уже 500 человек.'

    def check(self, client_settings_form):
        error = 'Просим написать 5 и более символов. Сейчас у Вас 2 символов.'
        self.assertEqual(client_settings_form.get_input_error(), error)

    def change_settings(self, client_settings_form):
        client_settings_form.set_name(self.NAME)
        client_settings_form.set_site(self.SITE)
        client_settings_form.set_title(self.TITLE)
        client_settings_form.set_description(self.DESCRIPTION)
        client_settings_form.click_on_desc_button()


class ClientSettingsChangeCompanyTestInvalidTooLongTitle(ClientSettingsTest):
    NAME = 'ОАО МАРС'
    SITE = 'oaomars.ru'
    TITLE = 'К' * 200
    DESCRIPTION = 'Мы занимаемся разработкой сайтов. В нашей компании уже 500 человек.'

    def check(self, client_settings_form):
        self.assertEqual(len(client_settings_form.get_title()), self.MAX_TITLE_LEN)
        client_settings_form.get_success_info()

    def change_settings(self, client_settings_form):
        client_settings_form.set_name(self.NAME)
        client_settings_form.set_site(self.SITE)
        client_settings_form.set_title(self.TITLE)
        client_settings_form.set_description(self.DESCRIPTION)
        client_settings_form.click_on_desc_button()


class ClientChangeContactsValid(ClientSettingsTest):
    ADDRESS = 'бауманская 32'
    PHONE = '+78889995050'
    COUNTRY = 'Россия'
    CITY = 'Москва'

    def check(self, client_settings_form):
        #client_settings_form.get_success_info()
        return

    def change_settings(self, client_settings_form):
        client_settings_form.set_address(self.ADDRESS)
        client_settings_form.set_phone(self.PHONE)
        client_settings_form.click_on_contact_button()


class ClientChangeContactsInvalidWrongPhone(ClientSettingsTest):
    ADDRESS = 'бауманская 32'
    PHONE = 'sgdfdhfjdsh'
    COUNTRY = 'Россия'
    CITY = 'Москва'

    def check(self, client_settings_form):
        input_error = 'Неправильный формат номера телефона. Пример: +7 900 90 90 900'
        self.assertEqual(client_settings_form.get_input_error(), input_error)
        return

    def change_settings(self, client_settings_form):
        client_settings_form.set_address(self.ADDRESS)
        client_settings_form.set_phone(self.PHONE)
        client_settings_form.click_on_contact_button()


class ClientChangeContactsInvalidTooShortAddress(ClientSettingsTest):
    ADDRESS = 'ба'
    PHONE = '+78889995050'
    COUNTRY = 'Россия'
    CITY = 'Москва'

    def check(self, client_settings_form):
        input_error = 'Просим написать 5 и более символов. Сейчас у Вас 2 символов.'
        self.assertEqual(client_settings_form.get_input_error(), input_error)
        return

    def change_settings(self, client_settings_form):
        client_settings_form.set_address(self.ADDRESS)
        client_settings_form.set_phone(self.PHONE)
        client_settings_form.click_on_contact_button()


class ClientChangeContactsInvalidTooLongAddress(ClientSettingsTest):
    ADDRESS = 'б' * 200
    PHONE = '+78889995050'
    COUNTRY = 'Россия'
    CITY = 'Москва'

    def check(self, client_settings_form):
        self.assertEqual(len(client_settings_form.get_address()), self.MAX_ADDRESS_LEN)
        #client_settings_form.get_success_info()

    def change_settings(self, client_settings_form):
        client_settings_form.set_address(self.ADDRESS)
        client_settings_form.set_phone(self.PHONE)
        client_settings_form.click_on_contact_button()

        # freelancer_settings_form.click_on_dropdown_list(1)
        # freelancer_settings_form.search_dropdown(self.COUNTRY)
        # freelancer_settings_form.pick_dropdown()
        # freelancer_settings_form.click_on_dropdown_list2()