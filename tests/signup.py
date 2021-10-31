from .base import BaseTest
from pages.signup import SignupPage


class SignupTestSuite(BaseTest):
    def test_short_login(self):
        page = SignupPage(self.driver)

        page.open()
        page.sign_up(login='short')

        self.assertEqual('Логин должен быть длиной от 6 до 20 символов!', page.validation_hint_login)

    def test_invalid_email(self):
        page = SignupPage(self.driver)

        page.open()
        page.sign_up(email='1')

        self.assertEqual('Некорректный формат Email', page.validation_hint_email)

    def test_password_only_digits(self):
        page = SignupPage(self.driver)

        page.open()
        page.sign_up(password='1234567890')

        self.assertEqual('Пароль должен содержать хотя бы одну букву!', page.validation_hint_password)

    def test_password_only_letters(self):
        page = SignupPage(self.driver)

        page.open()
        page.sign_up(password='abcdefghij')

        self.assertEqual('Пароль должен содержать хотя бы одну цифру!', page.validation_hint_password)

    def test_transition_to_login_from_form(self):
        page = SignupPage(self.driver)

        page.open()
        page.go_to_login_from_form()

        self.assertEqual(f'{page.ROOT_URL}/login', self.driver.current_url)

    def test_transition_to_login_from_header(self):
        page = SignupPage(self.driver)

        page.open()
        page.go_to_login_from_header()

        self.assertEqual(f'{page.ROOT_URL}/login', self.driver.current_url)
