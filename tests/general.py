# -*- coding: utf-8 -*-
import os
from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    BASE_URL = 'https://fwork.live/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)

    def login_as_freelancer(self):
        auth_form = self.form
        #auth_form.set_login('da@mail.ru')
        auth_form.set_login(os.getenv('F_EMAIL') if os.getenv('F_EMAIL') else 'da@mail.ru')
        auth_form.set_password(os.getenv('F_PASS') if os.getenv('F_PASS') else '123456')
        auth_form.submit()

    def login_as_client(self):
        auth_form = self.form
        auth_form.set_login(os.getenv('C_EMAIL') if os.getenv('C_EMAIL') else 'client@ya.ru')
        auth_form.set_password(os.getenv('C_PASS') if os.getenv('C_PASS') else '123456')
        auth_form.submit()


class AuthForm(Component):
    LOGIN = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//div[@class="field-group__fields "]/button[@type="submit"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT)))
        self.driver.find_element_by_xpath(self.SUBMIT).click()


# class LoginTest(unittest.TestCase):
#     EMAIL = 'da@mail.ru'
#     PASSWORD = '123456'
#     BLOG = 'Флудилка'
#     TITLE = u'ЗаГоЛоВоК'
#     MAIN_TEXT = u'Текст под катом! Отображается внутри топика!'
#
#     def setUp(self):
#         browser = os.environ.get('BROWSER', 'CHROME')
#
#         self.driver = Remote(
#             command_executor='http://127.0.0.1:4444/wd/hub',
#             desired_capabilities=getattr(DesiredCapabilities, browser).copy()
#         )
#
#     def tearDown(self):
#         self.driver.quit()
#
#     def test(self):
#         auth_page = AuthPage(self.driver)
#         auth_page.open()
#
#         auth_form = auth_page.form
#         auth_form.set_login(self.EMAIL)
#         auth_form.set_password(self.PASSWORD)
#         auth_form.submit()




