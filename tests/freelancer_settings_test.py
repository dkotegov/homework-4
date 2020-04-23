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
    TAGS = '//div[@class="input-tags__tags-wrapper"]/span'

    PHONE = '//input[@name="phone"]'
    ADDRESS = '//input[@name="address"]'

    LEVEL = '//span[@class="radio__label"]'

    DESC_BUTTON = '//div[@class="verview-settings card"]/div/form/div/div/div/button[@type="submit"]'
    CONTACT_BUTTON = '//div[@class="contacts-settings card"]/div/form/div/div/div/button[@type="submit"]'
    LEVEL_BUTTON = '//div[@class="experience-settings card"]/div/div/form/div/div/div/button[@type="submit"]'
    SPEC_BUTTON = '//div[@class="specialization-settings card"]/div/form/div/div/div/button[@type="submit"]'

    DROP_LIST = '//div[@class="select-custom__header"]'
    DROP_SEARCH = '//input[@class="select-dropdown__filter"]'
    DROP_RESULT = '//ul[@class="select-dropdown__items"]/li[1]/span[@class="select-items__item-label"]'

    DROP_CITY_LIST = '//div[@class="select-custom__header"]'

    EDIT_SUCCESS = '//div[@class="response-text response-text-success"]'
    INPUT_ERROR = '//span[@class="text-field__error"][@style="display: block; visibility: visible;"]'

    def set_description(self, desc):
        self.driver.find_element_by_xpath(self.DESCRIPTION).clear()
        self.driver.find_element_by_xpath(self.DESCRIPTION).send_keys(desc)

    def get_description(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.DESCRIPTION).get_attribute('value')
        )

    def set_skills(self, skills):
        self.driver.find_element_by_xpath(self.SKILLS).clear()
        self.driver.find_element_by_xpath(self.SKILLS).send_keys(skills)

    def set_address(self, address):
        self.driver.find_element_by_xpath(self.ADDRESS).clear()
        self.driver.find_element_by_xpath(self.ADDRESS).send_keys(address)

    def get_address(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.ADDRESS).get_attribute('value')
        )

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

    def click_on_desc_button(self):
        self.driver.find_element_by_xpath(self.DESC_BUTTON).click()

    def click_on_contact_button(self):
        self.driver.find_element_by_xpath(self.CONTACT_BUTTON).click()

    def click_on_level_button(self):
        self.driver.find_element_by_xpath(self.LEVEL_BUTTON).click()

    def click_on_spec_button(self):
        self.driver.find_element_by_xpath(self.SPEC_BUTTON).click()

    def click_on_dropdown_list(self, num):
        elements = self.driver.find_elements_by_xpath(self.DROP_LIST)
        print("DROPDOWNS:", len(elements))
        elements[num].click()

    def click_on_level(self, num):
        elements = self.driver.find_elements_by_xpath(self.LEVEL)
        print("LEVELS:", len(elements))
        elements[num].click()

    def search_dropdown(self, country):
        self.driver.find_element_by_xpath(self.DROP_SEARCH).send_keys(country)

    def pick_dropdown(self):
        self.driver.find_element_by_xpath(self.DROP_RESULT).click()

    def get_tags_num(self):
        return len(WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_xpath(self.TAGS)
        ))


class FreelancerSettingsTest(abc.ABC, unittest.TestCase):
    MAX_TAG_NUM = 5
    MAX_ADDRESS_LEN = 40
    MAX_DESCRIPTION_LEN = 500

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
        # self.driver.implicitly_wait(10)
        sleep(3)

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
        #freelancer_settings_form.get_success_info()
        return

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.set_description(self.DESCRIPTION)
        freelancer_settings_form.click_on_desc_button()


# class FreelancerChangeDescTestInvalidTooLong(FreelancerSettingsTest):
#     DESCRIPTION = "x" * 500
#
#     def check(self, freelancer_settings_form):
#         self.assertEqual(len(freelancer_settings_form.get_description()), self.MAX_ADDRESS_LEN)
#         # freelancer_settings_form.get_success_info()
#
#     def change_settings(self, freelancer_settings_form):
#         freelancer_settings_form.set_description(self.DESCRIPTION)
#         freelancer_settings_form.click_on_desc_button()


class FreelancerSetSkillsTestValid(FreelancerSettingsTest):
    DESCRIPTION = "hello"
    SKILLS = 'tag1 tag2 tag3 tag4 tag5 '

    def check(self, freelancer_settings_form):
        tag_num = len(self.SKILLS.split())
        self.assertEqual(freelancer_settings_form.get_tags_num(), tag_num)
        # freelancer_settings_form.get_success_info()

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.set_description(self.DESCRIPTION)
        freelancer_settings_form.set_skills(self.SKILLS)
        freelancer_settings_form.click_on_desc_button()


class FreelancerSetSkillsTestInvalidTooManyTags(FreelancerSettingsTest):
    DESCRIPTION = "hello"
    SKILLS = 'tag1 tag2 tag3 tag4 tag5 tag6 '

    def check(self, freelancer_settings_form):
        self.assertEqual(freelancer_settings_form.get_tags_num(), self.MAX_TAG_NUM)
        # freelancer_settings_form.get_success_info()

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.set_description(self.DESCRIPTION)
        freelancer_settings_form.set_skills(self.SKILLS)
        freelancer_settings_form.click_on_desc_button()


class FreelancerChangeContactsValid(FreelancerSettingsTest):
    ADDRESS = 'бауманская 32'
    PHONE = '+78889995050'
    COUNTRY = 'Россия'
    CITY = 'Москва'

    def check(self, freelancer_settings_form):
        # freelancer_settings_form.get_success_info()
        return

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.set_address(self.ADDRESS)
        freelancer_settings_form.set_phone(self.PHONE)
        freelancer_settings_form.click_on_contact_button()


class FreelancerChangeContactsInvalidWrongPhone(FreelancerSettingsTest):
    ADDRESS = 'бауманская 32'
    PHONE = 'sgdfdhfjdsh'
    COUNTRY = 'Россия'
    CITY = 'Москва'

    def check(self, freelancer_settings_form):
        input_error = 'Неправильный формат номера телефона. Пример: +7 900 90 90 900'
        self.assertEqual(freelancer_settings_form.get_input_error(), input_error)
        return

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.set_address(self.ADDRESS)
        freelancer_settings_form.set_phone(self.PHONE)
        freelancer_settings_form.click_on_contact_button()


class FreelancerChangeContactsInvalidTooShortAddress(FreelancerSettingsTest):
    ADDRESS = 'ба'
    PHONE = '+78889995050'
    COUNTRY = 'Россия'
    CITY = 'Москва'

    def check(self, freelancer_settings_form):
        input_error = 'Просим написать 5 и более символов. Сейчас у Вас 2 символов.'
        self.assertEqual(freelancer_settings_form.get_input_error(), input_error)
        return

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.set_address(self.ADDRESS)
        freelancer_settings_form.set_phone(self.PHONE)
        freelancer_settings_form.click_on_contact_button()


class FreelancerChangeContactsInvalidTooLongAddress(FreelancerSettingsTest):
    ADDRESS = 'б' * 200
    PHONE = '+78889995050'
    COUNTRY = 'Россия'
    CITY = 'Москва'

    def check(self, freelancer_settings_form):
        self.assertEqual(len(freelancer_settings_form.get_address()), self.MAX_ADDRESS_LEN)
        # freelancer_settings_form.get_success_info()

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.set_address(self.ADDRESS)
        freelancer_settings_form.set_phone(self.PHONE)
        freelancer_settings_form.click_on_contact_button()

        # freelancer_settings_form.click_on_dropdown_list(1)
        # freelancer_settings_form.search_dropdown(self.COUNTRY)
        # freelancer_settings_form.pick_dropdown()
        # freelancer_settings_form.click_on_dropdown_list2()


class FreelancerChangeExperienceJuniorTest(FreelancerSettingsTest):
    def check(self, freelancer_settings_form):
        return

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.click_on_level(0)
        freelancer_settings_form.click_on_level_button()


class FreelancerChangeExperienceMiddleTest(FreelancerSettingsTest):
    def check(self, freelancer_settings_form):
        return

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.click_on_level(1)
        freelancer_settings_form.click_on_level_button()


class FreelancerChangeExperienceSeniorTest(FreelancerSettingsTest):
    def check(self, freelancer_settings_form):
        return

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.click_on_level(2)
        freelancer_settings_form.click_on_level_button()


class FreelancerChangeSpecializationTest(FreelancerSettingsTest):
    def check(self, freelancer_settings_form):
        return

    def change_settings(self, freelancer_settings_form):
        freelancer_settings_form.click_on_spec_button()