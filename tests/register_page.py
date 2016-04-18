# -*- coding: utf-8 -*-
from page import Page
from component import Component
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage(Page):
    PATH = u'/signup/?lang=ru_RU'

    def get_form(self):
        return RegisterForm(self.driver)


class RegisterForm(Component):

    TAKEN_EMAIL_LEGIT = u'legit'

    TITLE = u"//div[contains(@class, 'qc-title-row')]"

    FIRST_NAME_INPUT = u"//*[contains(@class, 'qc-firstname-row')]/span[contains(@class, 'sig2')]/input"
    FIRST_NAME_NOTIF = u"//*[contains(@class, 'qc-firstname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'example')]"
    FIRST_NAME_ERROR = u"//*[contains(@class, 'qc-firstname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"
    LAST_NAME_INPUT = u"//*[contains(@class, 'qc-lastname-row')]/span[contains(@class, 'sig2')]/input"
    LAST_NAME_NOTIF = u"//*[contains(@class, 'qc-lastname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'example')]"
    LAST_NAME_ERROR = u"//*[contains(@class, 'qc-lastname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"

    BIRTHDATE_ERROR = u"//*[contains(@class, 'qc-birthday-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"
    BIRTHDATE_ERROR_TEXT = u"//*[contains(@class, 'qc-birthday-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]/span"
    BIRTHDATE_SUCCESS = u"//*[contains(@class, 'qc-birthday-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'success')]"

    CITY_INPUT = u"//*[contains(@class, 'qc-city-row')]/span[contains(@class, 'sig2')]/input"
    CITY_HELPER = u"//*[contains(@class, 'qc-city-row')]/span/*[contains(@class, 'geo_popup')]/span"
    CITY_ERROR = u"//*[contains(@class, 'qc-city-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"
    CITY_SUCCESS = u"//*[contains(@class, 'qc-city-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'success')]"

    SEX_SUCCESS = u"//*[contains(@class, 'qc-sex-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'success')]"
    SEX_BUTTONS = u"//input[@type='radio']"

    EMAIL_INPUT = u"//*[contains(@class, 'qc-login-row')]/span[contains(@class, 'sig2')]/input"
    EMAIL_SELECT = u"//*[contains(@class, 'qc-login-row')]/span[contains(@class, 'sig2')]/select"
    EMAIL_ERROR = u"//*[contains(@class, 'qc-login-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"
    EMAIL_SUCCESS = u"//*[contains(@class, 'qc-login-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'success')]"

    PASS_INPUT = u"//*[contains(@class, 'qc-pass-row')]/span[contains(@class, 'sig2')]/input"
    PASSVERIFY_INPUT = u"//*[contains(@class, 'qc-passverify-row')]/span[contains(@class, 'sig2')]/input"
    PASSVERIFY_SUCCESS = u"//*[contains(@class, 'qc-passverify-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'success')]"
    PASS_ERROR = u"//*[contains(@class, 'qc-pass-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"
    PASSVERIFY_ERROR = u"//*[contains(@class, 'qc-passverify-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"
    PASS_NOTIF = u"//*[contains(@class, 'qc-pass-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'example')]"
    PASS_STRENGTHS = u"//*[contains(@class, 'qc-pass-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'strength')]"

    PHONE_INPUT = u"//input[contains(@class, 'phone')]"
    PHONE_REGION_SELECT = u"//select[@id='country_ver']"
    PHONE_SUCCESS = u"//*[contains(@class, 'qc-phone-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'success')]"

    NO_PHONE_LINK = u"//a[@id='noPhoneLink']"
    EXTRA_EMAIL_INPUT = u"//div[contains(@class, 'qc-mail-row')]/span[contains(@class, 'sig2')]/input"
    EXTRA_EMAIL_SUCCESS = u"//div[contains(@class, 'qc-mail-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'success')]"
    EXTRA_EMAIL_ERROR = u"//div[contains(@class, 'qc-mail-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"

    DAY_SELECTOR = u"//*[contains(@class, 'qc-select-day')]"
    MONTH_SELECTOR = u"//*[contains(@class, 'qc-select-month')]"
    YEAR_SELECTOR = u"//*[contains(@class, 'qc-select-year')]"

    def get_first_name_notif(self):
        return self.driver.find_element_by_xpath(self.FIRST_NAME_NOTIF)

    def get_first_name_error(self):
        return self.driver.find_element_by_xpath(self.FIRST_NAME_ERROR)

    def set_first_name(self, name):
        self.driver.find_element_by_xpath(self.FIRST_NAME_INPUT).send_keys(name)

    def get_last_name_notif(self):
        return self.driver.find_element_by_xpath(self.LAST_NAME_NOTIF)

    def get_last_name_error(self):
        return self.driver.find_element_by_xpath(self.LAST_NAME_ERROR)

    def set_last_name(self, name):
        self.driver.find_element_by_xpath(self.LAST_NAME_INPUT).send_keys(name)

    def unfocus(self):
        self.driver.find_element_by_xpath(self.TITLE).click()

    def select_day(self, day):
        day = str(day)
        el = Select(self.driver.find_element_by_xpath(self.DAY_SELECTOR))
        el.select_by_visible_text(day)

    def select_month(self, month):
        el = Select(self.driver.find_element_by_xpath(self.MONTH_SELECTOR))
        el.select_by_visible_text(month)

    def select_year(self, year):
        year = str(year)
        el = Select(self.driver.find_element_by_xpath(self.YEAR_SELECTOR))
        el.select_by_visible_text(year)

    def get_birthdate_success_el(self):
        return self.driver.find_element_by_xpath(self.BIRTHDATE_SUCCESS)

    def get_birthdate_error_el(self):
        return self.driver.find_element_by_xpath(self.BIRTHDATE_ERROR)

    def get_birthdate_error_text(self):
        return self.driver.find_element_by_xpath(self.BIRTHDATE_ERROR_TEXT).text

    def get_city_input(self):
        return self.driver.find_element_by_xpath(self.CITY_INPUT)

    def set_city(self, city):
        self.driver.find_element_by_xpath(self.CITY_INPUT).send_keys(city)

    def get_city_error_el(self):
        return self.driver.find_element_by_xpath(self.CITY_ERROR)

    def get_city_auto_variant(self):
        helper = self.driver.find_element_by_xpath(self.CITY_HELPER)
        city = helper.find_element_by_tag_name('div')
        return city

    def get_city_success_el(self):
        return self.driver.find_element_by_xpath(self.CITY_SUCCESS)

    def get_sex_buttons(self):
        return self.driver.find_elements_by_xpath(self.SEX_BUTTONS)

    def get_sex_success_el(self):
        return self.driver.find_element_by_xpath(self.SEX_SUCCESS)

    def get_email_success_el(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of(self.driver.find_element_by_xpath(self.EMAIL_SUCCESS)))

    def get_email_error_el(self):
        return self.driver.find_element_by_xpath(self.EMAIL_ERROR)

    def get_email_input(self):
        return self.driver.find_element_by_xpath(self.EMAIL_INPUT)

    def set_email(self, email):
        username = email.split('@')[0]
        domain = '@{}'.format(email.split('@')[1])

        email_input = self.get_email_input()
        email_input.send_keys(username)

        select = Select(self.driver.find_element_by_xpath(self.EMAIL_SELECT))
        select.select_by_visible_text(domain)

    def get_pass_input(self):
        return self.driver.find_element_by_xpath(self.PASS_INPUT)

    def get_passverify_input(self):
        return self.driver.find_element_by_xpath(self.PASSVERIFY_INPUT)

    def get_passverify_success_el(self):
        return self.driver.find_element_by_xpath(self.PASSVERIFY_SUCCESS)

    def get_passverify_error_el(self):
        return self.driver.find_element_by_xpath(self.PASSVERIFY_ERROR)

    def get_pass_error_el(self):
        return self.driver.find_element_by_xpath(self.PASS_ERROR)

    def get_pass_notif_el(self):
        return self.driver.find_element_by_xpath(self.PASS_NOTIF)

    def set_pass(self, password):
        self.driver.find_element_by_xpath(self.PASS_INPUT).send_keys(password)

    def set_passverify(self, password):
        self.driver.find_element_by_xpath(self.PASSVERIFY_INPUT).send_keys(password)

    def get_pass_strength_list(self):
        return self.driver.find_elements_by_xpath(self.PASS_STRENGTHS)

    def get_phone_success_el(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of(self.driver.find_element_by_xpath(self.PHONE_SUCCESS)))

    def set_phone(self, phone):
        self.driver.find_element_by_xpath(self.PHONE_INPUT).send_keys(phone)

    def clear_phone_input(self):
        self.driver.find_element_by_xpath(self.PHONE_INPUT).clear()

    def get_no_phone_link(self):
        return self.driver.find_element_by_xpath(self.NO_PHONE_LINK)

    def get_extra_email_success_el(self):
        return self.driver.find_element_by_xpath(self.EXTRA_EMAIL_SUCCESS)

    def get_extra_email_error_el(self):
        return self.driver.find_element_by_xpath(self.EXTRA_EMAIL_ERROR)

    def set_extra_email(self, email):
        self.driver.find_element_by_xpath(self.EXTRA_EMAIL_INPUT).send_keys(email)

    def clear_extra_email(self):
        self.driver.find_element_by_xpath(self.EXTRA_EMAIL_INPUT).clear()

    def get_extra_email_input(self):
        return self.driver.find_element_by_xpath(self.EXTRA_EMAIL_INPUT)
