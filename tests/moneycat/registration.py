import os

import time
import unittest
from .pages.signup import SignUpPage
from testutils import SeleniumTest


class MoneyCatRegistrationTest(SeleniumTest):
    def setUp(self):
        super().setUp()
        self.account = SignUpPage(self.driver)
        self.account.open()
        self.signup_form = self.account.form

    def tearDown(self) -> None:
        self.driver.quit()

    def test_signup_success(self):
        self.account.Actions.sign_up(
            self.signup_form,
            str(time.time()) + "@mail.ru",
            os.environ.get("PASS"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.signup_form.get_account_header(),
            "Личный кабинет"
        )

    def test_signup_user_exists(self):
        self.account.Actions.sign_up(
            self.signup_form,
            os.environ.get("LOGIN"),
            os.environ.get("PASS"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Пользователь с таким email'ом уже существует"
        )

    def test_signup_empty_form(self):
        self.account.Actions.sign_up(
            self.signup_form,
            "",
            "",
            ""
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Вы ввели некорректный email-адрес"
        )
        self.assertEqual(
            self.signup_form.get_error_message(1),
            "Длина пароля должна быть в пределах от 6 до 30 символов"
        )
        self.assertEqual(
            self.signup_form.get_error_message(2),
            "Длина пароля должна быть в пределах от 6 до 30 символов"
        )

    def test_signup_unexceptable_symbols_in_email_cyrillic(self):
        self.account.Actions.sign_up(
            self.signup_form,
            "юзер@mail.ru",
            os.environ.get("PASS"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Вы ввели некорректный email-адрес"
        )

    def test_signup_unexceptable_symbols_in_email_special_characters(self):
        self.account.Actions.sign_up(
            self.signup_form,
            ":*&^%$user@mail.ru",
            os.environ.get("PASS"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Вы ввели некорректный email-адрес"
        )

    def test_signup_email_with_allowed_special_characters(self):
        self.account.Actions.sign_up(
            self.signup_form,
            "new-user." + str(time.time()) + "@mail.ru",
            os.environ.get("PASS"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.signup_form.get_account_header(),
            "Личный кабинет"
        )

    def test_signup_unexceptable_symbols_in_pass_cyrillic(self):
        self.account.Actions.sign_up(
            self.signup_form,
            os.environ.get("LOGIN"),
            "парольqwe123",
            "парольqwe123"
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Пароль может включать только буквы английского алфавита и цифры"
        )

    def test_signup_unexceptable_symbols_in_pass_special_characters(self):
        self.account.Actions.sign_up(
            self.signup_form,
            os.environ.get("LOGIN"),
            "_!@#$%^&*()-+=qwerty",
            "_!@#$%^&*()-+=qwerty"
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Пароль может включать только буквы английского алфавита и цифры"
        )

    def test_signup_invalid_email_no_separators(self):
        self.account.Actions.sign_up(
            self.signup_form,
            "usermailru",
            os.environ.get("PASS"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Вы ввели некорректный email-адрес"
        )

    def test_signup_invalid_email_no_dog(self):
        self.account.Actions.sign_up(
            self.signup_form,
            "usermail.ru",
            os.environ.get("PASS"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Вы ввели некорректный email-адрес"
        )

    def test_signup_invalid_email_no_point(self):
        self.account.Actions.sign_up(
            self.signup_form,
            "user@mailru",
            os.environ.get("PASS"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Вы ввели некорректный email-адрес"
        )

    def test_signup_pass_shorter_6(self):
        self.account.Actions.sign_up(
            self.signup_form,
            os.environ.get("LOGIN"),
            "qwert",
            "qwert"
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Длина пароля должна быть в пределах от 6 до 30 символов"
        )
        self.assertEqual(
            self.signup_form.get_error_message(1),
            "Длина пароля должна быть в пределах от 6 до 30 символов"
        )

    def test_signup_pass_longer_30(self):
        self.account.Actions.sign_up(
            self.signup_form,
            os.environ.get("LOGIN"),
            "qwertyasdfghzxcvbnqwertyasdfghz",
            "qwertyasdfghzxcvbnqwertyasdfghz"
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Длина пароля должна быть в пределах от 6 до 30 символов"
        )
        self.assertEqual(
            self.signup_form.get_error_message(1),
            "Длина пароля должна быть в пределах от 6 до 30 символов"
        )

    def test_signup_passwords_do_not_match(self):
        self.account.Actions.sign_up(
            self.signup_form,
            os.environ.get("LOGIN"),
            os.environ.get("PASS"),
            os.environ.get("PASS") + "A",
        )

        self.assertEqual(
            self.signup_form.get_error_message(0),
            "Пароли не совпадают"
        )

    def test_signup_button_to_signin(self):
        self.signup_form.click_signin_href()
        self.assertEqual(
            self.signup_form.get_auth_title(),
            "Здравствуйте!"
        )
