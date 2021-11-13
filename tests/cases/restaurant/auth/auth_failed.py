import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.auth_customer import CustomerAuthPage


class RestaurantAuthFailedTest(unittest.TestCase):
    EMPTY_EMAIL_ERR_MESSAGE = "Email: Поле должно быть заполнено" # todo для ресторана и пользователя объединить, вынести
    EMPTY_PASSWORD_ERR_MESSAGE = "Пароль: Поле должно быть заполнено"
    NOT_VALID_EMAIL_ERR_MESSAGE = "Email: Введите настоящий адрес электронной почты"
    NOT_VALID_PASSWORD_ERR_MESSAGE = "Пароль: Ваш пароль должен быть от 6 до 30 символов"

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.auth_page = CustomerAuthPage(self.driver)
        self.auth_page.open()
        self.EXISTING_LOGIN = os.environ['LOGIN_RESTAURANT']
        self.PASSWORD = os.environ['PASSWORD']
        self.NOT_EXISTING_LOGIN = "qwerty098@mail.ru"  # todo для ресторана и пользователя объединить, вынести
        self.WRONG_PASSWORD = "QWE231"
        self.PASSWORD_UNDER_6_SYMBOLS = "231"
        self.EMAIL_WITH_NO_AT = "zxcmail.ru"
        self.EMAIL_WITH_NO_SYMBOLS_B4_AT = "@mail.ru"
        self.EMAIL_WITHOUT_DOMAIN = "zxc@"
        self.EMAIL_WITHOUT_NOT_LATIN_SYMBOLS = "даша@mail.ru"

    def tearDown(self):
        self.driver.quit()

    def test_empty_inputs(self):
        self.auth_page.submit()
        login_error = self.auth_page.get_login_error()
        password_error = self.auth_page.get_password_error()
        self.assertEqual(login_error, self.EMPTY_EMAIL_ERR_MESSAGE)
        self.assertEqual(password_error, self.EMPTY_PASSWORD_ERR_MESSAGE)

    def test_empty_password_input(self):
        self.auth_page.set_login(self.EXISTING_LOGIN)
        self.auth_page.submit()
        password_error = self.auth_page.get_password_error()
        self.assertEqual(password_error, self.EMPTY_PASSWORD_ERR_MESSAGE)

    def test_empty_login_input(self):
        self.auth_page.set_password(self.PASSWORD)
        self.auth_page.submit()
        login_error = self.auth_page.get_login_error()
        self.assertEqual(login_error, self.EMPTY_EMAIL_ERR_MESSAGE)

    def test_not_existing_login(self):
        self.auth_page.set_login(self.NOT_EXISTING_LOGIN)
        self.auth_page.set_password(self.PASSWORD)
        self.auth_page.submit()
        error_occurred = self.auth_page.check_if_error_occurred()
        self.assertEqual(error_occurred, True)

    def test_wrong_password(self):
        self.auth_page.set_login(self.EXISTING_LOGIN)
        self.auth_page.set_password(self.WRONG_PASSWORD)
        self.auth_page.submit()
        error_occurred = self.auth_page.check_if_error_occurred()
        self.assertEqual(error_occurred, True)

    def test_email_without_at_symbol(self):
        self.auth_page.set_login(self.EMAIL_WITH_NO_AT)
        self.auth_page.set_password(self.WRONG_PASSWORD)
        self.auth_page.submit()
        login_error = self.auth_page.get_login_error()
        self.assertEqual(login_error, self.NOT_VALID_EMAIL_ERR_MESSAGE)

    def test_email_with_no_symbols_b4_at(self):
        self.auth_page.set_login(self.EMAIL_WITH_NO_SYMBOLS_B4_AT)
        self.auth_page.set_password(self.WRONG_PASSWORD)
        self.auth_page.submit()
        login_error = self.auth_page.get_login_error()
        self.assertEqual(login_error, self.NOT_VALID_EMAIL_ERR_MESSAGE)

    def test_email_without_domain(self):
        self.auth_page.set_login(self.EMAIL_WITHOUT_DOMAIN)
        self.auth_page.set_password(self.WRONG_PASSWORD)
        self.auth_page.submit()
        login_error = self.auth_page.get_login_error()
        self.assertEqual(login_error, self.NOT_VALID_EMAIL_ERR_MESSAGE)

    def test_password_under_6_symbols(self):
        self.auth_page.set_login(self.NOT_EXISTING_LOGIN)
        self.auth_page.set_password(self.PASSWORD_UNDER_6_SYMBOLS)
        self.auth_page.submit()
        password_error = self.auth_page.get_password_error()
        self.assertEqual(password_error, self.NOT_VALID_PASSWORD_ERR_MESSAGE)

    def test_email_not_in_Latin_letters(self):
        self.auth_page.set_login(self.EMAIL_WITHOUT_NOT_LATIN_SYMBOLS)
        self.auth_page.set_password(self.WRONG_PASSWORD)
        self.auth_page.submit()
        login_error = self.auth_page.get_login_error()
        self.assertEqual(login_error, self.NOT_VALID_EMAIL_ERR_MESSAGE)

    # def test_password_quotes_arent_cut(self):
