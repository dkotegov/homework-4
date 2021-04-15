import os

from .pages.auth import AuthPage
from testutils import SeleniumTest


class MoneyCatAuthTest(SeleniumTest):
    def setUp(self):
        super(MoneyCatAuthTest, self).setUp()
        self.account = AuthPage(self.driver)
        self.account.open()
        self.login_form = self.account.form

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_success(self):
        self.account.Actions.sign_in(
            self.login_form,
            os.environ.get("LOGIN"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.login_form.get_account_header(),
            "Личный кабинет"
        )

    def test_login_nonexist(self):
        self.account.Actions.sign_in(
            self.login_form,
            "mkoijnbhu@ygv.mhr",
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.login_form.get_error_message(),
            "Пароль или Email не подходит"
        )

    def test_login_existing_account_wrong_pass(self):
        self.account.Actions.sign_in(
            self.login_form,
            os.environ.get("LOGIN"),
            os.environ.get("PASS") + "1"
        )

        self.assertEqual(
            self.login_form.get_error_message(),
            "Пароль или Email не подходит"
        )

    def test_login_send_empty_form(self):
        self.account.Actions.sign_in(
            self.login_form,
            "",
            ""
        )

        self.assertEqual(
            self.login_form.get_error_message(),
            "Вы ввели некорректный email-адрес"
        )

    def test_login_send_empty_email(self):
        self.account.Actions.sign_in(
            self.login_form,
            "",
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.login_form.get_error_message(),
            "Вы ввели некорректный email-адрес"
        )

    def test_login_send_empty_pass(self):
        self.account.Actions.sign_in(
            self.login_form,
            os.environ.get("LOGIN"),
            ""
        )

        self.assertEqual(
            self.login_form.get_error_message(),
            "Пароль или Email не подходит"
        )

    def test_login_button_to_signup(self):
        self.login_form.go_to_signin()
        self.login_form.click_signup_href()
        self.assertEqual(
            self.login_form.get_registration_title(),
            "Добро пожаловать!"
        )
