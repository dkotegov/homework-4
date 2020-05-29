import os
from tests.cases.base import Test
from tests.pages.authorization import AuthPage
from tests.pages.solarsunrise_urls import ProfilePage


class AuthTest(Test):
    def setUp(self):
        super().setUp()
        self.page = AuthPage(self.driver)

    # Авторизация с корректными почтой и паролем
    def test_correct_auth(self):
        mail = os.environ.get('LOGIN')
        password = os.environ.get('PASSWORD')

        self.page.form.set_mail(mail)
        self.page.form.set_password(password)
        self.page.form.submit()
        ProfilePage(self.driver, open=False).wait_for_load()

        nick_text = self.page.form.check_nickname()
        self.assertNotEqual(nick_text, '', 'No nickname')

    # Ошибка авторизации с наверными почтой/паролем: почта не существует, пароль корректный
    def test_no_exist_mail_and_correct_password(self):
        mail = 'Nelltesttest@mail.ru'
        password = 'Nelltest'

        self.page.form.set_mail(mail)
        self.page.form.set_password(password)
        self.page.form.submit()

        err_text = self.page.form.check_error_field()
        self.assertNotEqual(err_text, '', 'No error field')

    # Ошибка авторизации с наверными почтой/паролем: почта корректная, пароль некорректный
    def test_correct_mail_and_incorrect_password(self):
        mail = 'Nelltest@mail.ru'
        password = 'Nelltesttest'

        self.page.form.set_mail(mail)
        self.page.form.set_password(password)
        self.page.form.submit()

        err_text = self.page.form.check_error_field()
        self.assertNotEqual(err_text, '', 'No error field')

    # Ошибка авторизации с пустыми полями: пустая почта, пароль заполнен
    def test_empty_mail_and_filled_password(self):
        mail = ''
        password = 'Nelltest'

        self.page.form.set_mail(mail)
        self.page.form.set_password(password)
        self.page.form.submit()

        err_text = self.page.form.check_error_field()
        self.assertNotEqual(err_text, '', 'No error field')

    # Ошибка авторизации с пустыми полями: пустой пароль, почта заполнена
    def test_filled_mail_and_empty_password(self):
        mail = 'Nelltest@mail.ru'
        password = ''

        self.page.form.set_mail(mail)
        self.page.form.set_password(password)
        self.page.form.submit()

        err_text = self.page.form.check_error_field()
        self.assertNotEqual(err_text, '', 'No error field')

    # Ошибка авторизации с пустыми полями: пустая почта, пустой пароль
    def test_empty_mail_and_empty_password(self):
        self.page.form.set_mail('')
        self.page.form.set_password('')
        self.page.form.submit()

        err_text = self.page.form.check_error_field()
        self.assertNotEqual(err_text, '', 'No error field')
