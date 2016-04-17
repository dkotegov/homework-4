# -*- coding: utf-8 -*-
from page import Page
from component import Component
from selenium.webdriver.support.ui import Select


class RegisterPage(Page):
    PATH = u'/signup/?lang=ru_RU'

    def get_form(self):
        return RegisterForm(self.driver)


class RegisterForm(Component):

    TITLE = u"//div[contains(@class, 'qc-title-row')]"

    FIRST_NAME_INPUT = u"//*[contains(@class, 'qc-firstname-row')]/span[contains(@class, 'sig2')]/input"
    FIRST_NAME_NOTIF = u"//*[contains(@class, 'qc-firstname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'example')]"
    FIRST_NAME_ERROR = u"//*[contains(@class, 'qc-firstname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"
    LAST_NAME_INPUT = u"//*[contains(@class, 'qc-lastname-row')]/span[contains(@class, 'sig2')]/input"
    LAST_NAME_NOTIF = u"//*[contains(@class, 'qc-lastname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'example')]"
    LAST_NAME_ERROR = u"//*[contains(@class, 'qc-lastname-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"

    BIRTHDATE_ERROR = u"//*[contains(@class, 'qc-birthday-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"
    BIRTHDATE_SUCCESS = u"//*[contains(@class, 'qc-birthday-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'success')]"

    CITY_INPUT = u"//*[contains(@class, 'qc-city-row')]/span[contains(@class, 'sig2')]/input"
    CITY_HELPER = u"//*[contains(@class, 'qc-city-row')]/span/*[contains(@class, 'geo_popup')]/span"
    CITY_ERROR = u"//*[contains(@class, 'qc-city-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'error')]"
    CITY_SUCCESS = u"//*[contains(@class, 'qc-city-row')]/span[contains(@class, 'sig3')]/span[contains(@class, 'success')]"

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

    def get_city_input(self):
        return self.driver.find_element_by_xpath(self.CITY_INPUT)

    def set_city(self, city):
        self.driver.find_element_by_xpath(self.CITY_INPUT).send_keys(city)

    def get_city_error_el(self):
        return self.driver.find_element_by_xpath(self.CITY_ERROR)

    def get_city_helper_el(self):
        return self.driver.find_element_by_xpath(self.CITY_HELPER)

    def get_city_success_el(self):
        return self.driver.find_element_by_xpath(self.CITY_SUCCESS)
