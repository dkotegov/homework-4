import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote
from tests.personal_data.src.personal_data_page import PersonalDataPage
from tests.personal_data.src.auth_page import AuthPage


class PersonalDataTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']
    SUCCESS_NAME = 'Ультрабобер'
    SUCCESS_DATE = [27, 6, 2001]
    FAIL_NAME = 'Ультрабобер<>'
    FAIL_DATE = [27, 8, 2021]
    AVATAR_SUCCESS = './tests/personal_data/test/img/success.jpg'
    AVATAR_FAIL = './tests/personal_data/test/img/fail.jpg'
    CITY_SUCCESS = 'Москва, Россия'
    CITY_FAIL = 'Казахстан'


    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        # browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def authorize(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorize(self.LOGIN, self.PASSWORD)
        auth_page.top_menu.get_username()

    def test_edit_firstname_success(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_firstname(self.SUCCESS_NAME)
        personal_data_page.form.submit()

    def test_edit_lastname_success(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_lastname(self.SUCCESS_NAME)
        personal_data_page.form.submit()

    def test_edit_nickname_success(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_nickname(self.SUCCESS_NAME)
        personal_data_page.form.submit()

    def test_edit_date_success(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_date(self.SUCCESS_DATE[0], self.SUCCESS_DATE[1], self.SUCCESS_DATE[2])
        personal_data_page.form.submit()

    def test_load_avatar_success(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.load_avatar(self.AVATAR_SUCCESS)
        personal_data_page.form.save_avatar()

    def test_edit_city_success(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_city(self.CITY_SUCCESS)
        personal_data_page.form.submit()

    def test_edit_firstname_fail(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_firstname(self.FAIL_NAME)
        personal_data_page.form.submit()
        personal_data_page.form.check_error()

    def test_edit_lastname_fail(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_lastname(self.FAIL_NAME)
        personal_data_page.form.submit()
        personal_data_page.form.check_error()

    def test_edit_nickname_fail(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_nickname(self.FAIL_NAME)
        personal_data_page.form.submit()
        personal_data_page.form.check_error()

    def test_edit_date_fail(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_date(self.FAIL_DATE[0], self.FAIL_DATE[1], self.FAIL_DATE[2])
        personal_data_page.form.submit()

    def test_load_avatar_fail(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.load_avatar(self.AVATAR_FAIL)
        personal_data_page.form.save_avatar()

    def test_edit_city_fail(self):
        self.authorize()

        personal_data_page = PersonalDataPage(self.driver)
        personal_data_page.open()

        personal_data_page.form.edit_city(self.CITY_FAIL)
        personal_data_page.form.submit()
        personal_data_page.form.check_error()
