# -*- coding: utf-8 -*-

import os
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import ResumeData
import TestData
from Auth import AuthPage
from PageObject import Page


class CreateResumePage(Page):
    PATH = 'applicant/resumes/view?resume='


class ContactsPage(Page):
    PATH = 'https://rabota.mail.ru/applicant/resumes/edit/contacts?resume='
    OPEN_BUTTON = '//a[text()="Контакты "]'

    def open(self):
        self.driver.find_element_by_xpath(self.OPEN_BUTTON).click()

    @property
    def contacts_form(self):
        return ContactsForm(self.driver)


class PersonalPage(Page):
    PATH = 'applicant/resumes/edit/personal?resume='
    OPEN_BUTTON = '//a[text()="Имя, возраст, город "]'

    def open(self):
        self.driver.find_element_by_xpath(self.OPEN_BUTTON).click()

    @property
    def personal_form(self):
        return PersonalInfoForm(self.driver)


class SalaryPage(Page):
    PATH = 'applicant/resumes/edit/position?resume='
    OPEN_BUTTON = '//a[text()="Желаемая должность и зарплата "]'

    def open(self):
        self.driver.find_element_by_xpath(self.OPEN_BUTTON).click()

    @property
    def salary_form(self):
        return SalaryForm(self.driver)


class EducationPage(Page):
    PATH = 'applicant/resumes/edit/education?resume='
    OPEN_BUTTON = '//a[text()="Образование "]'

    def open(self):
        self.driver.find_element_by_xpath(self.OPEN_BUTTON).click()

    @property
    def education_form(self):
        return EducationForm(self.driver)


class PersonalInfoForm(object):
    LASTNAME = '//input[@name="lastName.string"]'
    FIRSTNAME = '//input[@name="firstName.string"]'
    DAY_SELECT = '//select[@data-qa="resume__birthday__day-select"]'
    MONTH_SELECT = '//select[@data-qa="resume__birthday__month-select"]'
    YEAR_SELECT = '//select[@data-qa="resume__birthday__year-select"]'
    OPTION = '//option[text()="{}"]'
    MALE = '//input[@value="male"]'
    FEMALE = '//input[@value="female"]'
    TOWN = '//input[@data-qa="suggestCity"]'
    UNDERGROUND = '//input[@data-qa="suggestMetro"]'
    VALIDATE_MESSAGE = '//span[text()="Длина превышена на 10 символов"]'
    SUBMIT = '//input[@value="Сохранить"]'

    def __init__(self, driver):
        self.driver = driver

    def clear_lastname(self):
        self.driver.find_element_by_xpath(self.LASTNAME).clear()

    def set_lastname(self, lastname):
        self.clear_lastname()
        self.driver.find_element_by_xpath(self.LASTNAME).send_keys(lastname)

    def clear_firstname(self):
        self.driver.find_element_by_xpath(self.FIRSTNAME).clear()

    def set_firstname(self, firstname):
        self.clear_firstname()
        self.driver.find_element_by_xpath(self.FIRSTNAME).send_keys(firstname)

    def day_select_open(self):
        self.driver.find_element_by_xpath(self.DAY_SELECT).click()

    def month_select_open(self):
        self.driver.find_element_by_xpath(self.MONTH_SELECT).click()

    def year_select_open(self):
        self.driver.find_element_by_xpath(self.YEAR_SELECT).click()

    def opened_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()

    def select_male(self):
        self.driver.find_element_by_xpath(self.MALE).click()

    def select_female(self):
        self.driver.find_element_by_xpath(self.FEMALE).click()

    def set_town(self, town_name):
        self.driver.find_element_by_xpath(self.TOWN).clear()
        self.driver.find_element_by_xpath(self.TOWN).send_keys(town_name)

    def set_metro(self, metro):
        self.driver.find_element_by_xpath(self.UNDERGROUND).send_keys(metro)

    def is_displayed_validate_message(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda driver: driver.find_element_by_xpath(self.VALIDATE_MESSAGE).is_displayed()
        )

    def submit_is_enabled(self):
        try:
            return WebDriverWait(self.driver, 1, 0.1).until(
                lambda driver: self.driver.find_element_by_xpath(self.SUBMIT).is_enabled()
            )
        except TimeoutException:
            return False

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class ContactsForm(object):
    PHONE_COUNTRY = '//input[@name="phone.country"]'
    PHONE_CITY = '//input[@name="phone.city"]'
    PHONE_NUMBER = '//input[@name="phone.number"]'
    VALIDATE_CODE_COUNTRY = '//span[text()="Неверный код страны"]'
    VALIDATE_PHONE = '//span[text()="Номер указан некорректно"]'
    SUBMIT = '//input[@value="Сохранить"]'

    def __init__(self, driver):
        self.driver = driver

    def clear_phone_country(self):
        self.driver.find_element_by_xpath(self.PHONE_COUNTRY).clear()

    def set_phone_country(self, code):
        self.clear_phone_country()
        self.driver.find_element_by_xpath(self.PHONE_COUNTRY).send_keys(code)

    def set_phone_city(self, code):
        self.driver.find_element_by_xpath(self.PHONE_CITY).clear()
        self.driver.find_element_by_xpath(self.PHONE_CITY).send_keys(code)

    def set_phone_number(self, number):
        self.driver.find_element_by_xpath(self.PHONE_NUMBER).clear()
        self.driver.find_element_by_xpath(self.PHONE_NUMBER).send_keys(number)

    def is_displayed_validate_phone_country(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda driver: driver.find_element_by_xpath(self.VALIDATE_CODE_COUNTRY).is_displayed()
        )

    def is_displayed_validate_phone(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda driver: driver.find_element_by_xpath(self.VALIDATE_PHONE).is_displayed()
        )

    def submit_is_enabled(self):
        try:
            return WebDriverWait(self.driver, 1, 0.1).until(
                lambda driver: self.driver.find_element_by_xpath(self.SUBMIT).is_enabled()
            )
        except TimeoutException:
            return False

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class SalaryForm(object):
    OBJECTIVE = '//input[@name="title.string"]'
    BEGIN_CARER = '//input[@data-gaformstatistic-name="profarea.string"]'
    VALIDATE_MESSAGE = '//span[text()="Длина превышена на 10 символов"]'
    PROF_REGION_FIRST = '//span[text()="Автомобильный бизнес"]'
    PROF_REGION_SECOND = '//span[text()="Административный персонал"]'
    PROF_REGION_THIRD = '//span[text()="Бухгалтерия"]'
    SUBMIT = '//input[@value="Сохранить"]'

    def __init__(self, driver):
        self.driver = driver

    def set_objective(self, work):
        self.driver.find_element_by_xpath(self.OBJECTIVE).clear()
        self.driver.find_element_by_xpath(self.OBJECTIVE).send_keys(work)

    def set_begin_carer(self):
        self.driver.find_element_by_xpath(self.BEGIN_CARER).click()

    def choose_prof_region(self):
        self.driver.find_element_by_xpath(self.PROF_REGION_FIRST).click()
        self.driver.find_element_by_xpath(self.PROF_REGION_SECOND).click()
        self.driver.find_element_by_xpath(self.PROF_REGION_THIRD).click()

    def is_displayed_validate_message(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda driver: driver.find_element_by_xpath(self.VALIDATE_MESSAGE).is_displayed()
        )

    def submit_is_enabled(self):
        try:
            return WebDriverWait(self.driver, 1, 0.1).until(
                lambda driver: self.driver.find_element_by_xpath(self.SUBMIT).is_enabled()
            )
        except TimeoutException:
            return False

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).send_keys(Keys.RETURN)


class EducationForm(object):
    INSTITUTION_NAME = '//input[@name="primaryEducation.name"]'
    FACULTY = '//input[@name="primaryEducation.organization"]'
    SPECIALITY = '//input[@name="primaryEducation.result"]'
    EDUCATION_YEAR_SELECTOR = '//select[@name="primaryEducation.year"]'
    OPTION = '//option[@value="{}"]'
    VALIDATE_MESSAGE = '//span[text()="Длина превышена на {} символов"]'
    COUNT_INVALID_SYMBOL = 0
    SUBMIT = '//input[@value="Сохранить"]'

    def __init__(self, driver):
        self.driver = driver

    def set_institut_name(self, name):
        self.driver.find_element_by_xpath(self.INSTITUTION_NAME).clear()
        self.driver.find_element_by_xpath(self.INSTITUTION_NAME).send_keys(name)

    def set_faculty_name(self, name):
        self.driver.find_element_by_xpath(self.FACULTY).clear()
        self.driver.find_element_by_xpath(self.FACULTY).send_keys(name)

    def set_speciality_name(self, name):
        self.driver.find_element_by_xpath(self.SPECIALITY).clear()
        self.driver.find_element_by_xpath(self.SPECIALITY).send_keys(name)

    def education_select_open(self):
        self.driver.find_element_by_xpath(self.EDUCATION_YEAR_SELECTOR).click()

    def opened_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()

    def set_count_invalid_symbol(self, count):
        self.COUNT_INVALID_SYMBOL = count

    def is_displayed_validate_message(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda driver: driver.find_element_by_xpath(self.VALIDATE_MESSAGE.format(self.COUNT_INVALID_SYMBOL)).is_displayed()
        )

    def submit_is_enabled(self):
        try:
            return WebDriverWait(self.driver, 1, 0.1).until(
                lambda driver: self.driver.find_element_by_xpath(self.SUBMIT).is_enabled()
            )
        except TimeoutException:
            return False

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class AuthForm(object):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//input[@value="Войти в личный кабинет"]'
    LOGIN_BUTTON = '//a[text()="Вход"]'

    def __init__(self, driver):
        self.driver = driver

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_email(self, mail):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(mail)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class CreateResumePageTest(unittest.TestCase):
    EMAIL = 'technopark.testemail@mail.ru'
    PASSWORD = 'Qwerty123'
    TITLE = u'Новое резюме'

    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.wrong_data = TestData.WrongData()
        self.wrong_data.set_up_wrong_data()

    def tearDown(self):
        self.driver.quit()

    def test_personal_form(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.auth_form
        auth_form.open_form()
        auth_form.set_email(self.EMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_resume = CreateResumePage(self.driver)
        create_resume.open()

        personal_page = PersonalPage(self.driver)
        personal_page.open()
        personal_form = personal_page.personal_form
        self.assertFalse(personal_form.submit_is_enabled())
        personal_form.select_male()
        personal_form.set_lastname(self.wrong_data.LONG_LASTNAME)
        personal_form.set_firstname(self.wrong_data.LONG_FIRSTNAME)
        self.assertTrue(personal_form.is_displayed_validate_message())
        personal_form.set_lastname(ResumeData.LASTNAME)
        self.assertTrue(personal_form.is_displayed_validate_message())
        personal_form.set_firstname(ResumeData.FIRSTNAME)
        self.assertTrue(personal_form.submit_is_enabled())

    def test_contacts_form(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.auth_form
        auth_form.open_form()
        auth_form.set_email(self.EMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_resume = CreateResumePage(self.driver)
        create_resume.open()

        contacts_page = ContactsPage(self.driver)
        contacts_page.open()
        contacts_form = contacts_page.contacts_form
        self.assertFalse(contacts_form.submit_is_enabled())
        contacts_form.set_phone_country(self.wrong_data.WRONG_CODE_COUNTRY)
        contacts_form.set_phone_city(self.wrong_data.WRONG_CODE_CITY)
        contacts_form.set_phone_number(self.wrong_data.WRONG_PHONE_NUMBER)
        self.assertTrue(contacts_form.is_displayed_validate_phone_country())
        contacts_form.set_phone_country(ResumeData.PHONE_COUNTRY)
        self.assertTrue(contacts_form.is_displayed_validate_phone())
        contacts_form.set_phone_city(ResumeData.PHONE_CITY)
        self.assertTrue(contacts_form.is_displayed_validate_phone())
        contacts_form.set_phone_number(ResumeData.PHONE_NUMBER)
        time.sleep(1)
        self.assertTrue(contacts_form.submit_is_enabled())

    def test_salary_form(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.auth_form
        auth_form.open_form()
        auth_form.set_email(self.EMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_resume = CreateResumePage(self.driver)
        create_resume.open()

        salary_page = SalaryPage(self.driver)
        salary_page.open()
        salary_form = salary_page.salary_form
        self.assertFalse(salary_form.submit_is_enabled())
        salary_form.set_objective(self.wrong_data.WRONG_OBJECTIVE)
        self.assertTrue(salary_form.is_displayed_validate_message())
        salary_form.set_objective(ResumeData.OBJECTIVE)
        salary_form.set_begin_carer()
        salary_form.choose_prof_region()
        self.assertTrue(salary_form.submit_is_enabled())

    def test_education_form(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.auth_form
        auth_form.open_form()
        auth_form.set_email(self.EMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_resume = CreateResumePage(self.driver)
        create_resume.open()

        education_page = EducationPage(self.driver)
        education_page.open()
        education_form = education_page.education_form
        education_form.set_count_invalid_symbol(10)
        self.assertFalse(education_form.submit_is_enabled())
        education_form.set_institut_name(self.wrong_data.WRONG_INSTITUTION_NAME)
        education_form.set_faculty_name(self.wrong_data.WRONG_FACULTY)
        self.assertTrue(education_form.is_displayed_validate_message())
        education_form.set_speciality_name(self.wrong_data.WRONG_FACULTY)
        self.assertTrue(education_form.is_displayed_validate_message())
        education_form.set_institut_name(ResumeData.INSTITUTION_NAME)
        self.assertTrue(education_form.is_displayed_validate_message())
        education_form.set_faculty_name(ResumeData.FACULTY)
        education_form.set_speciality_name(ResumeData.SPECIALITY)
        education_form.education_select_open()
        education_form.opened_select_set_option(ResumeData.EDUCATION_YEAR)
        self.assertTrue(education_form.submit_is_enabled())

    def test_valid_create_resume(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.auth_form
        auth_form.open_form()
        auth_form.set_email(self.EMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_resume = CreateResumePage(self.driver)
        create_resume.open()

        personal_page = PersonalPage(self.driver)
        personal_page.open()
        personal_form = personal_page.personal_form
        personal_form.set_firstname(ResumeData.FIRSTNAME)
        personal_form.set_lastname(ResumeData.LASTNAME)
        personal_form.day_select_open()
        personal_form.opened_select_set_option(ResumeData.DAY)
        personal_form.month_select_open()
        personal_form.opened_select_set_option(ResumeData.MONTH)
        personal_form.year_select_open()
        personal_form.opened_select_set_option(ResumeData.YEAR)
        personal_form.select_male()
        self.assertTrue(personal_form.submit_is_enabled())
        personal_form.submit()
        self.assertEqual(self.TITLE, self.driver.title)

        contacts_page = ContactsPage(self.driver)
        contacts_page.open()

        contacts_form = contacts_page.contacts_form
        contacts_form.set_phone_country(ResumeData.PHONE_COUNTRY)
        contacts_form.set_phone_city(ResumeData.PHONE_CITY)
        contacts_form.set_phone_number(ResumeData.PHONE_NUMBER)
        self.assertTrue(contacts_form.submit_is_enabled())
        contacts_form.submit()
        self.assertEqual(self.TITLE, self.driver.title)

        salary_page = SalaryPage(self.driver)
        salary_page.open()
        salary_form = salary_page.salary_form
        salary_form.set_objective(ResumeData.OBJECTIVE)
        salary_form.set_begin_carer()
        salary_form.choose_prof_region()
        self.assertTrue(salary_form.submit_is_enabled())
        salary_form.submit()
        self.assertEqual(ResumeData.OBJECTIVE, self.driver.title)

        education_page = EducationPage(self.driver)
        education_page.open()
        education_form = education_page.education_form
        education_form.set_institut_name(ResumeData.INSTITUTION_NAME)
        education_form.set_faculty_name(ResumeData.FACULTY)
        education_form.set_speciality_name(ResumeData.SPECIALITY)
        education_form.education_select_open()
        education_form.opened_select_set_option(ResumeData.EDUCATION_YEAR)
        self.assertTrue(education_form.submit_is_enabled())
        education_form.submit()
        self.assertEqual(ResumeData.OBJECTIVE, self.driver.title)
