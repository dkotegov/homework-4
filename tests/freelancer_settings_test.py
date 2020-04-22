import os
import abc
import unittest
from time import sleep

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

from tests.dashboard_page import DashboardPage

from tests.general import Page, Component, AuthPage


class FreelancerSettingPage(Page):
    PATH = '/settings?tab=freelancer'

    @property
    def form(self):
        return FreelancerSettingForm(self.driver)


class FreelancerSettingForm(Component):
    DESCRIPTION = '//textarea[@name="overview"]'
    SKILLS = '//div[@class="text-field"]/input[@name="text field"]'
    BUTTONS = '//button[@type="submit"]'

    EDIT_SUCCESS = '//div[@class="response-text response-text-success"]'

    def set_description(self, desc):
        self.driver.find_element_by_xpath(self.DESCRIPTION).clear()
        self.driver.find_element_by_xpath(self.DESCRIPTION).send_keys(desc)

    def get_description(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.DESCRIPTION).get_attribute('value')
        )

    def get_success_info(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.EDIT_SUCCESS).text
        )

    def click_on_button(self, num):
        self.driver.find_elements_by_xpath(self.BUTTONS)[num].click()


class FreelancerSettingsTest(abc.ABC, unittest.TestCase):
    DESCRIPTION = None

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login_as_freelancer()

    def tearDown(self):
        self.driver.quit()

    def test(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.dashboard.get_title()

        freelancer_settings_page = FreelancerSettingPage(self.driver)
        freelancer_settings_page.open()
        freelancer_settings_form = freelancer_settings_page.form
        #freelancer_settings_form.get_description()

        self.change_settings(freelancer_settings_form)
        self.check(freelancer_settings_form)

    @abc.abstractmethod
    def check(self, freelancer_settings_form):
        return

    @abc.abstractmethod
    def change_settings(self, freelancer_settings_form):
        return


class FreelancerChangeDescTestValid(FreelancerSettingsTest):
    DESCRIPTION = 'Привет, я руковожу UX-лабораторией. Хочу рассказать, ' \
                  'чем занимается моя команда, какие методы есть в её арсенале, ' \
                  'и как наша работа позволяет достигать ' \
                  'бизнес-целей. '

    def check(self, freelancer_settings_form):
        freelancer_settings_form.get_success_info()

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.set_description(self.DESCRIPTION)
        freelancer_settings_form.click_on_button(1)


class FreelancerChangeDescTestInvalidTooLong(FreelancerSettingsTest):
    DESCRIPTION = "x" * 500

    def check(self, freelancer_settings_form):
        freelancer_settings_form.get_success_info()

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.set_description(self.DESCRIPTION)
        freelancer_settings_form.click_on_button(1)
