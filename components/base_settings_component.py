# -*- coding: utf-8 -*-

from components.base_component import BaseComponent
import time


class PersonalDataForm(BaseComponent):
    NAME = "//input[@name='fr.name']"
    SURNAME = "//input[@name='fr.surname']"
    SAVE_BUTTON = "//input[@id='hook_FormButton_button_savePopLayerEditUserProfileNew']"
    CLOSE_BUTTON = "//input[@id='buttonId_button_close']"

    def name_surname(self, my_name, my_surname):
        name = self.get_visibility_element(self.NAME)
        self.driver.execute_script("arguments[0].value='" + my_name + "'", name)
        surname = self.get_visibility_element(self.SURNAME)
        self.driver.execute_script("arguments[0].value='" + my_surname + "'", surname)

    def save(self):
        self.get_clickable_element(self.SAVE_BUTTON).click()

    def close_save(self):
        self.get_clickable_element(self.CLOSE_BUTTON).click()

    ERROR = "//span[@class='input-e']"

    def name_surname_error(self):
        self.get_visibility_element(self.ERROR)  # Ждем пока станет видимый
        e1 = self.get_visibility_elements(self.ERROR)[0].text
        e2 = self.get_visibility_elements(self.ERROR)[1].text
        return e1, e2

    DAYS = "//select[@id='field_bday']"
    DAY = "//select[@id='field_bday']/option[@value='5']"
    DAY_ERROR = "//select[@id='field_bday']/option[@value='29']"

    MONTHS = "//select[@id='field_bmonth']"
    MONTH = "//select[@id='field_bmonth']/option[@value='3']"
    MONTH_ERROR = "//select[@id='field_bmonth']/option[@value='2']"

    YEARS = "//select[@id='field_byear']"
    YEAR = "//select[@id='field_byear']/option[@value='1996']"
    YEAR_ERROR = "//select[@id='field_byear']/option[@value='2001']"

    DATE = "//div[@value='user-profile_i_value ellip']"

    def birthday(self):
        self.get_visibility_element(self.DAYS).click()
        self.get_visibility_element(self.DAY).click()

        self.get_visibility_element(self.MONTHS).click()
        self.get_visibility_element(self.MONTH).click()

        self.get_visibility_element(self.YEARS).click()
        self.get_visibility_element(self.YEAR).click()

    def birthday_error(self):
        self.get_visibility_element(self.DAYS).click()
        self.get_visibility_element(self.DAY_ERROR).click()

        self.get_visibility_element(self.MONTHS).click()
        self.get_visibility_element(self.MONTH_ERROR).click()

        self.get_visibility_element(self.YEARS).click()
        self.get_visibility_element(self.YEAR_ERROR).click()

    def get_birthday_error(self):
        return self.get_visibility_elements(self.ERROR)[2].text

    GENDER_MALE = "//input[@id='field_gender_1']"
    GENDER_FEMALE = "//input[@id='field_gender_2']"

    def check_male(self):
        self.get_clickable_element(self.GENDER_MALE).click()

    def check_female(self):
        self.get_clickable_element(self.GENDER_FEMALE).click()

    def is_male(self):
        return self.get_clickable_element(self.GENDER_MALE).is_selected()

    def is_female(self):
        return self.get_clickable_element(self.GENDER_FEMALE).is_selected()

    CURRENT_CITY = "//input[@id='field_citySugg_SearchInput']"

    BIRTH_CITY = "//input[@id='field_cityBSugg_SearchInput']"

    CITY_LIST = "//li[@class='suggest_li']"


    def put_current_city_country(self, str):
        city = self.get_visibility_element(self.CURRENT_CITY)
        city.clear()
        city.send_keys(str)

    def select_current_city_country(self):
        self.get_visibility_elements(self.CITY_LIST)[0].click()

    CITY_ERROR = "//span[@class='input-e']"

    def current_city_error(self):
        return self.get_visibility_element(self.CITY_ERROR).text



class ProneNumberForm(BaseComponent):
    NUMBER = "//input[@name='st.layer.phone']"
    OK_BUTTON = "//input[@class='button-pro form-actions_yes']"

    OK_BUTTON2 = "//input[@value='Подтвердить код']"

    def set_number(self, my_number):
        number = self.get_visibility_element(self.NUMBER)
        self.driver.execute_script("arguments[0].value='" + my_number + "'", number)

    def ok_button_click(self):
        self.get_clickable_element(self.OK_BUTTON).click()

    def ok_button2(self):
        return self.get_visibility_element(self.OK_BUTTON2)

    NUMBER_ERROR = "//div[@id='formErrorsContainer']"

    def number_error(self):
        return self.get_visibility_element(self.NUMBER_ERROR).text


class EmailForm(BaseComponent):
    EMAIL = "//input[@name='fr.email']"
    PASSWORD = "//input[@name='fr.password']"
    SAVE_BUTTON = "//input[@class='button-pro form-actions_yes']"

    def set_email(self, my_email):
        email = self.get_visibility_element(self.EMAIL)
        self.driver.execute_script("arguments[0].value='" + my_email + "'", email)

    def set_password(self, my_password):
        password = self.get_visibility_element(self.PASSWORD)
        self.driver.execute_script("arguments[0].value='" + my_password + "'", password)

    def save_button_click(self):
        self.get_clickable_element(self.SAVE_BUTTON).click()

    ERROR = "//span[@class='input-e']"

    def get_error_password(self):
        return self.get_visibility_element(self.ERROR).text


class BaseSettingsForm(BaseComponent):
    DATA = "//div[@class='user-settings_i_lk lstp-t al']"

    PROFILE1 = "//a[@class='compact-profile_a ellip-i']"

    def personal_data(self):
        personal_data = self.driver.find_elements_by_xpath(self.DATA)[0]
        self.driver.execute_script("arguments[0].click();", personal_data)
        return PersonalDataForm(self.driver)

    def phone_number(self):
        phone_number = self.driver.find_elements_by_xpath(self.DATA)[2]
        self.driver.execute_script("arguments[0].click();", phone_number)
        return ProneNumberForm(self.driver)

    def email(self):
        email = self.driver.find_elements_by_xpath(self.DATA)[4]
        self.driver.execute_script("arguments[0].click();", email)
        return EmailForm(self.driver)

    def profile_get(self):
        return self.get_visibility_element(self.PROFILE1).text

    def profile_click(self):
        self.get_clickable_element(self.PROFILE1).click()
