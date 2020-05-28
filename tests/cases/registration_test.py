from tests.cases.base import Test
from tests.pages.registration import RegPage
import os


class RegTest(Test):
    def setUp(self):
        super().setUp()
        self.page = RegPage(self.driver)

    # Регистрация с корректными неиспользованными ранее почтой, никнеймом, паролем
    def test_correct_reg(self):
        mail = os.environ["REG_MAIL"]
        login = os.environ["REG_LOGIN"]
        password = "q1w2e3r4"
        self.page.form.registration(mail, login, password)

    # Ошибка регистрации с существующими данными, при условии, что пароль валидный
    # Cуществует почта, но не существует логин
    def test_existing_email_and_nonexistent_login(self):
        mail = "Nelltest@mail.ru"
        login = "nonexistingLogin"
        password = "q1w2e3r4"
        self.page.form.incorrect_registration(mail, login, password)

    # Cуществует логин, не существует почта
    def test_nonexistent_email_and_existing_login(self):
        mail = "Nelltesttest6@mail.ru"
        login = "ADshishovaaa"
        password = "q1w2e3r4"
        self.page.form.incorrect_registration(mail, login, password)

    # Ошибка регистрации с пустой почтой и новым логином, и валидным паролем
    def test_empty_email_and_new_login_and_valid_password(self):
        mail = ""
        login = "Nelltesttest"
        password = "q1w2e3r4"
        self.page.form.incorrect_registration(mail, login, password)

    # Ошибка регистрации с новой почтой, валидным паролем и невалидным логином
    # Логин пустой
    def test_new_email_valid_password_empty_login(self):
        mail = "Nelltesttest6@mail.ru"
        login = ""
        password = "q1w2e3r4"
        self.page.form.incorrect_registration(mail, login, password)

    # Логин = 2 символа, состоит из латинских букв и цифр
    def test_new_email_valid_password_and_login_equal_to_2_ch(self):
        mail = "Nelltesttest6@mail.ru"
        login = "ll"
        password = "q1w2e3r4"
        self.page.form.incorrect_registration(mail, login, password)

    # Логин = 31 символ, состоит из латинских букв и цифр
    def test_new_email_valid_password_and_login_equal_to_31_ch(self):
        mail = "Nelltesttest6@mail.ru"
        login = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
        password = "q1w2e3r4"
        self.page.form.incorrect_registration(mail, login, password)

    # Логин [3, 30] символов, состоит из кириллицы
    def test_new_email_valid_password_and_cyrillic_login(self):
        mail = "Nelltesttest6@mail.ru"
        login = "ррррр"
        password = "q1w2e3r4"
        self.page.form.incorrect_registration(mail, login, password)

    # Ошибка регистрации с  новой почтой, новым логином и невалидным паролем
    # Пароль пустой
    def test_new_email_new_login_empty_password(self):
        mail = "Nelltesttest6@mail.ru"
        login = "Nelltestnew"
        password = ""
        self.page.form.incorrect_registration(mail, login, password)

    # Пароль = 5 символов
    def test_new_email_new_login_and_password_equal_5_ch(self):
        mail = "Nelltesttest6@mail.ru"
        login = "Nelltestnew"
        password = "hhhhh"
        self.page.form.incorrect_registration(mail, login, password)

    # Пароль = 31 символ
    def test_new_email_new_login_and_password_equal_31_ch(self):
        mail = "Nelltesttest6@mail.ru"
        login = "Nelltestnew"
        password = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
        self.page.form.incorrect_registration(mail, login, password)

    # Переход на страницу авторизации
    def test_go_to_signin(self):
        self.page.form.to_login_page()
