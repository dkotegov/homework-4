from tests.cases.base import Test
from tests.pages.authorization import AuthPage


class AuthTest(Test):
    def setUp(self):
        super().setUp()
        self.page = AuthPage(self.driver)

    # Авторизация с корректными почтой и паролем
    def test_correct_auth(self):
        mail = "Nelltest@mail.ru"
        password = "Nelltest"
        self.page.form.authorise(mail, password)

    # Ошибка авторизации с наверными почтой/паролем: почта не существует, пароль корректный
    def test_no_exist_mail_and_correct_password(self):
        mail = "Nelltesttest@mail.ru"
        password = "Nelltest"
        self.page.form.incorrect_authorise(mail, password)

    # Ошибка авторизации с наверными почтой/паролем: почта корректная, пароль некорректный
    def test_correct_mail_and_incorrect_password(self):
        mail = "Nelltest@mail.ru"
        password = "Nelltesttest"
        self.page.form.incorrect_authorise(mail, password)

    # Ошибка авторизации с пустыми полями: пустая почта, пароль заполнен
    def test_empty_mail_and_filled_password(self):
        mail = ""
        password = "Nelltest"
        self.page.form.incorrect_authorise(mail, password)

    # Ошибка авторизации с пустыми полями: пустой пароль, почта заполнена
    def test_filled_mail_and_empty_password(self):
        mail = "Nelltest@mail.ru"
        password = ""
        self.page.form.incorrect_authorise(mail, password)

    # Ошибка авторизации с пустыми полями: пустая почта, пустой пароль
    def test_empty_mail_and_filled_password(self):
        self.page.form.incorrect_authorise("", "")

    # Переход на страницу регистрации
    def test_to_reg_page(self):
        self.page.form.to_registration_page()
