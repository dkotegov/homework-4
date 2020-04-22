# -*- coding: utf-8 -*-

import os
import abc
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker

from .general import Page, Component
from .dashboard_page import DashboardPage


class SignupPage(Page):
    PATH = '/signup'

    @property
    def form(self):
        return SignupForm(self.driver)


class SignupForm(Component):
    LOGIN = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    FIRST_NAME = '//input[@name="firstName"]'
    SECOND_NAME = '//input[@name="secondName"]'
    FREELANCER_TYPE = '//div[@class="radio-group"]/div/label[1]/span[@class="radio__label"]'
    CLIENT_TYPE = '//div[@class="radio-group"]/div/label[2]/span[@class="radio__label"]'
    SUBMIT = '//div[@class="field-group"]/div/button[@type="submit"]'

    INPUT_ERROR = '//span[@class="text-field__error"][@style="display: block; visibility: visible;"]'
    SERVER_ERROR = '//div[@class="response-text response-text-error"]'

    EMAIL_ERROR = '//form[@id="signupForm"]/div[4]//span[@class="text-field__error"]'

    def set_email(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def set_first_name(self, first_name):
        self.driver.find_element_by_xpath(self.FIRST_NAME).send_keys(first_name)

    def set_second_name(self, second_name):
        self.driver.find_element_by_xpath(self.SECOND_NAME).send_keys(second_name)

    def set_freelancer_type(self):
        self.driver.find_element_by_xpath(self.FREELANCER_TYPE).click()

    def set_client_type(self):
        self.driver.find_element_by_xpath(self.CLIENT_TYPE).click()

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def get_input_error(self):
        return WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.INPUT_ERROR).text
        )

    def get_server_error(self):
        return WebDriverWait(self.driver, 40, 0.5).until(
            lambda d: d.find_element_by_xpath(self.SERVER_ERROR).text
        )


class SignupTest(abc.ABC, unittest.TestCase):
    EMAIL = None
    PASSWORD = None
    FIRST_NAME = None
    SECOND_NAME = None
    IS_FREELANCER = None

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        signup_page = SignupPage(self.driver)
        signup_page.open()

        signup_form = signup_page.form

        if self.IS_FREELANCER:
            signup_form.set_freelancer_type()
        else:
            signup_form.set_client_type()

        signup_form.set_first_name(self.FIRST_NAME)
        signup_form.set_second_name(self.SECOND_NAME)
        signup_form.set_email(self.EMAIL)
        signup_form.set_password(self.PASSWORD)
        signup_form.submit()

        self.check(signup_form)

    @abc.abstractmethod
    def check(self, signup_form):
        return


class SignupTestValidFreelancer(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "123456"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = True

    TITLE = "Главная"

    def check(self, signup_form):
        dashboard_page = DashboardPage(self.driver)
        title = dashboard_page.dashboard.get_title()
        username = dashboard_page.dashboard.get_username()
        self.assertEqual(self.TITLE, title)
        self.assertEqual(self.FIRST_NAME + ' ' + self.SECOND_NAME, username)


class SignupTestInvalidFreelancerExistingEmail(SignupTest):
    EMAIL = "da@mail.ru"
    PASSWORD = "123456"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = True

    def check(self, signup_form):
        error = 'Пользователь с таким email уже существует'
        self.assertEqual(signup_form.get_server_error(), error)


class SignupTestInvalidFreelancerShortPassword(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "1"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = True

    def check(self, signup_form):
        error = 'Неправильная форма данных, пароль должен быть не менее 6 символов. Email должен быть в формате ' \
                'title@gmail.com'
        self.assertEqual(signup_form.get_server_error(), error)


class SignupTestInvalidFreelancerNameWithSymbols(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "1"
    FIRST_NAME = "IVAN---..."
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = True

    def check(self, signup_form):
        error = 'Обычно имя так не выглядит. Это Ваше действительное имя?'
        self.assertEqual(signup_form.get_input_error(), error)


class SignupTestInvalidFreelancerNameWithNumbers(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "123456"
    FIRST_NAME = "IVAN12322"
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = True

    def check(self, signup_form):
        error = 'Обычно имя так не выглядит. Это Ваше действительное имя?'
        self.assertEqual(signup_form.get_input_error(), error)


class SignupTestInvalidFreelancerSurnameWithSymbols(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "123456"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOVd---d-d"
    IS_FREELANCER = True

    def check(self, signup_form):
        error = 'Обычно фамилия так не выглядит. Это Ваша действительная фамилия?'
        self.assertEqual(signup_form.get_input_error(), error)


class SignupTestInvalidFreelancerSurnameWithNumbers(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "123456"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOVd12324"
    IS_FREELANCER = True

    def check(self, signup_form):
        error = 'Обычно фамилия так не выглядит. Это Ваша действительная фамилия?'
        self.assertEqual(signup_form.get_input_error(), error)


class SignupTestValidClient(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "123456"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = False

    def check(self, signup_form):
        dashboard_page = DashboardPage(self.driver)
        title = dashboard_page.dashboard.get_title()
        username = dashboard_page.dashboard.get_username()
        self.assertEqual(self.TITLE, title)
        self.assertEqual(self.FIRST_NAME + ' ' + self.SECOND_NAME, username)


class SignupTestInvalidClientExistingEmail(SignupTest):
    EMAIL = "da@mail.ru"
    PASSWORD = "123456"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = False

    def check(self, signup_form):
        error = 'Пользователь с таким email уже существует'
        self.assertEqual(signup_form.get_server_error(), error)


class SignupTestInvalidClientShortPassword(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "1"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = False

    def check(self, signup_form):
        error = 'Неправильная форма данных, пароль должен быть не менее 6 символов. Email должен быть в формате ' \
                'title@gmail.com'
        self.assertEqual(signup_form.get_server_error(), error)


class SignupTestInvalidClientNameWithSymbols(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "1"
    FIRST_NAME = "IVAN---..."
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = False

    def check(self, signup_form):
        error = 'Обычно имя так не выглядит. Это Ваше действительное имя?'
        self.assertEqual(signup_form.get_input_error(), error)


class SignupTestInvalidClientNameWithNumbers(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "123456"
    FIRST_NAME = "IVAN12322"
    SECOND_NAME = "IVANOV"
    IS_FREELANCER = False

    def check(self, signup_form):
        error = 'Обычно имя так не выглядит. Это Ваше действительное имя?'
        self.assertEqual(signup_form.get_input_error(), error)


class SignupTestInvalidClientSurnameWithSymbols(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "123456"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOVd---d-d"
    IS_FREELANCER = False

    def check(self, signup_form):
        error = 'Обычно фамилия так не выглядит. Это Ваша действительная фамилия?'
        self.assertEqual(signup_form.get_input_error(), error)


class SignupTestInvalidClientSurnameWithNumbers(SignupTest):
    fake = Faker()
    EMAIL = fake.email()
    PASSWORD = "123456"
    FIRST_NAME = "IVAN"
    SECOND_NAME = "IVANOVd12324"
    IS_FREELANCER = False

    def check(self, signup_form):
        error = 'Обычно фамилия так не выглядит. Это Ваша действительная фамилия?'
        self.assertEqual(signup_form.get_input_error(), error)
