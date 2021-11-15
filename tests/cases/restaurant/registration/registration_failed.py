import os
import unittest

from faker import Faker
from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.registration_restaurant import RestaurantRegistrationPage


class RestaurantRegistrationFailedTest(unittest.TestCase):
    EMPTY_EMAIL_ERR_MESSAGE = "Email: Поле должно быть заполнено"
    EMPTY_NAME_ERR_MESSAGE = "Название ресторана: Поле должно быть заполнено"
    EMPTY_PASSWORD_ERR_MESSAGE = "Пароль: Поле должно быть заполнено"
    EMPTY_REPEAT_PASSWORD_ERR_MESSAGE = "Повторите пароль: Поле должно быть заполнено"
    EMPTY_RADIUS_ERR_MESSAGE = "Введите радиус покрытия (в метрах): Введите число"
    PASSWORDS_DONT_MATCH_ERR_MESSAGE = "Повторите пароль: Пароли не совпадают"
    NOT_VALID_PHONE_ERR_MESSAGE = "Телефон: Введите настоящий номер телефона"
    NOT_VALID_EMAIL_ERR_MESSAGE = "Email: Введите настоящий адрес электронной почты"
    NOT_VALID_PASSWORD_ERR_MESSAGE = "Пароль: Ваш пароль должен быть от 6 до 30 символов"
    # AUTH_ERR_MESSAGE = "Пароль: Поле должно быть заполнено"

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.faker = Faker()
        self.registration_page = RestaurantRegistrationPage(self.driver)
        self.registration_page.open()
        self.EXISTING_EMAIL = os.environ['LOGIN_RESTAURANT']
        self.EXISTING_PHONE = os.environ['PHONE']
        self.PASSWORD = os.environ['PASSWORD']
        self.NOT_EXISTING_EMAIL = "qwerty098@mail.ru"
        self.PHONE_UNDER_11_SYMBS = "811111111"
        self.PHONE_WITH_LETTERS = "8111sd18s4f"
        self.WRONG_PASSWORD = "QWE231"
        self.PASSWORD_UNDER_6_SYMBOLS = "231"
        self.EMAIL_WITH_NO_AT = "zxcmail.ru"
        self.EMAIL_WITH_NO_SYMBOLS_B4_AT = "@mail.ru"
        self.EMAIL_WITHOUT_DOMAIN = "zxc@"
        self.EMAIL_WITHOUT_NOT_LATIN_SYMBOLS = "даша@mail.ru"

    def tearDown(self):
        self.driver.quit()

    def test_empty_inputs(self):
        self.registration_page.submit()
        email_error = self.registration_page.get_email_error()
        phone_error = self.registration_page.get_phone_error()
        name_error = self.registration_page.get_title_error()
        password_error = self.registration_page.get_password_error()
        repeat_password_error = self.registration_page.get_repeat_password_error()
        radius_error = self.registration_page.get_radius_error()
        self.assertEqual(email_error, self.EMPTY_EMAIL_ERR_MESSAGE)
        self.assertEqual(phone_error, self.NOT_VALID_PHONE_ERR_MESSAGE)
        self.assertEqual(name_error, self.EMPTY_NAME_ERR_MESSAGE)
        self.assertEqual(password_error, self.EMPTY_PASSWORD_ERR_MESSAGE)
        self.assertEqual(repeat_password_error, self.EMPTY_REPEAT_PASSWORD_ERR_MESSAGE)
        self.assertEqual(radius_error, self.EMPTY_RADIUS_ERR_MESSAGE)

    def test_empty_email_input(self):
        self.registration_page.set_phone(self.faker.phone_number())
        self.registration_page.set_title(self.faker.name())
        self.registration_page.set_password(self.PASSWORD)
        self.registration_page.set_repeat_password(self.PASSWORD)
        self.registration_page.submit()
        email_error = self.registration_page.get_email_error()
        self.assertEqual(email_error, self.EMPTY_EMAIL_ERR_MESSAGE)

    def test_empty_name_input(self):
        self.registration_page.set_email(self.faker.email())
        self.registration_page.set_phone(self.faker.phone_number())
        self.registration_page.set_password(self.PASSWORD)
        self.registration_page.set_repeat_password(self.PASSWORD)
        self.registration_page.submit()
        name_error = self.registration_page.get_title_error()
        self.assertEqual(name_error, self.EMPTY_NAME_ERR_MESSAGE)

    def test_empty_phone_input(self):
        self.registration_page.set_email(self.faker.email())
        self.registration_page.set_title(self.faker.name())
        self.registration_page.set_password(self.PASSWORD)
        self.registration_page.set_repeat_password(self.PASSWORD)
        self.registration_page.submit()
        phone_error = self.registration_page.get_phone_error()
        self.assertEqual(phone_error, self.NOT_VALID_PHONE_ERR_MESSAGE)

    def test_empty_password_input(self):
        self.registration_page.set_email(self.faker.email())
        self.registration_page.set_phone(self.faker.phone_number())
        self.registration_page.set_title(self.faker.name())
        self.registration_page.set_repeat_password(self.PASSWORD)
        self.registration_page.submit()
        password_error = self.registration_page.get_password_error()
        self.assertEqual(password_error, self.EMPTY_PASSWORD_ERR_MESSAGE)

    def test_email_without_at_symbol(self):
        self.registration_page.set_email(self.EMAIL_WITH_NO_AT)
        self.registration_page.set_password(self.WRONG_PASSWORD)
        self.registration_page.submit()
        email_error = self.registration_page.get_email_error()
        self.assertEqual(email_error, self.NOT_VALID_EMAIL_ERR_MESSAGE)

    def test_email_with_no_symbols_b4_at(self):
        self.registration_page.set_email(self.EMAIL_WITH_NO_SYMBOLS_B4_AT)
        self.registration_page.set_password(self.WRONG_PASSWORD)
        self.registration_page.submit()
        email_error = self.registration_page.get_email_error()
        self.assertEqual(email_error, self.NOT_VALID_EMAIL_ERR_MESSAGE)

    def test_email_without_domain(self):
        self.registration_page.set_email(self.EMAIL_WITHOUT_DOMAIN)
        self.registration_page.set_password(self.WRONG_PASSWORD)
        self.registration_page.submit()
        email_error = self.registration_page.get_email_error()
        self.assertEqual(email_error, self.NOT_VALID_EMAIL_ERR_MESSAGE)

    def test_password_under_6_symbols(self):
        self.registration_page.set_password(self.PASSWORD_UNDER_6_SYMBOLS)
        self.registration_page.submit()
        password_error = self.registration_page.get_password_error()
        self.assertEqual(password_error, self.NOT_VALID_PASSWORD_ERR_MESSAGE)

    def test_phone_under_11_symbs(self):
        self.registration_page.set_phone(self.PHONE_UNDER_11_SYMBS)
        self.registration_page.submit()
        phone_error = self.registration_page.get_phone_error()
        self.assertEqual(phone_error, self.NOT_VALID_PHONE_ERR_MESSAGE)

    def test_phone_with_letters(self):
        self.registration_page.set_phone(self.PHONE_WITH_LETTERS)
        self.registration_page.submit()
        phone_error = self.registration_page.get_phone_error()
        self.assertEqual(phone_error, self.NOT_VALID_PHONE_ERR_MESSAGE)

    def test_email_not_in_Latin_letters(self):
        self.registration_page.set_email(self.EMAIL_WITHOUT_NOT_LATIN_SYMBOLS)
        self.registration_page.set_password(self.WRONG_PASSWORD)
        self.registration_page.submit()
        email_error = self.registration_page.get_email_error()
        self.assertEqual(email_error, self.NOT_VALID_EMAIL_ERR_MESSAGE)

    def test_register_existing_email(self):
        self.registration_page.set_email(self.EXISTING_EMAIL)
        self.registration_page.set_phone(self.faker.phone_number())
        self.registration_page.set_title(self.faker.name())
        self.registration_page.set_password(self.PASSWORD)
        self.registration_page.set_repeat_password(self.PASSWORD)
        self.registration_page.submit()
        error_occurred = self.registration_page.check_if_error_occurred()
        self.assertEqual(error_occurred, True)

    def test_register_existing_phone(self):
        self.registration_page.set_email(self.faker.email())
        self.registration_page.set_phone(self.EXISTING_PHONE)
        self.registration_page.set_title(self.faker.name())
        self.registration_page.set_password(self.PASSWORD)
        self.registration_page.set_repeat_password(self.PASSWORD)
        self.registration_page.submit()
        error_occurred = self.registration_page.check_if_error_occurred()
        self.assertEqual(error_occurred, True)

    def test_passwords_dont_match(self):
        self.registration_page.set_email(self.faker.email())
        self.registration_page.set_phone(self.faker.phone_number())
        self.registration_page.set_title(self.faker.name())
        self.registration_page.set_password(self.PASSWORD)
        self.registration_page.set_repeat_password(self.PASSWORD+'hello')
        self.registration_page.submit()
        password_error = self.registration_page.get_repeat_password_error()
        self.assertEqual(password_error, self.PASSWORDS_DONT_MATCH_ERR_MESSAGE)

    def test_zero_radius(self):
        self.registration_page.set_email(self.faker.email())
        self.registration_page.set_phone(self.faker.phone_number())
        self.registration_page.set_title(self.faker.name())
        self.registration_page.set_password(self.PASSWORD)
        self.registration_page.set_repeat_password(self.PASSWORD)
        self.registration_page.set_radius(0)
        self.registration_page.submit()
        radius_error = self.registration_page.get_radius_error()
        self.assertEqual(radius_error, self.EMPTY_RADIUS_ERR_MESSAGE)

