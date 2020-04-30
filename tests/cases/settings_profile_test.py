from tests.pages.settings_profile import SettingsPage
from tests.pages.authorization import AuthForm
from tests.cases.base import TestAuthorizedWithFillFields
import os


class SettingsTest(TestAuthorizedWithFillFields):
    def setUp(self):
        super().setUp()
        self.page = SettingsPage(self.driver)

    # Изменение одного из полей
    # Изменение аватарки TODO
    # def test_change_avatar(self):
    #     self.page.form.change_photo()

    # Изменение Имени
    def test_change_valid_name(self):
        name = 'Nell'
        self.page.form.change_field('name', name)

    # Изменение Фамилии
    def test_change_valid_surname(self):
        surname = 'Lin'
        self.page.form.change_field('surname', surname)

    # Изменение статуса
    def test_change_valid_status(self):
        status = 'Великолепность'
        self.page.form.change_field('status', status)

    # Изменение никнейма на несуществующий
    def test_change_valid_nickname(self):
        nickname = os.environ['NEW_NICKNAME']
        self.page.form.change_field('nickname', nickname)

    # # Изменение всех полей с условием, что никнейм не существует
    def test_change_all_fields_with_valid_nickname(self):
        name = 'Nelli'
        surname = 'Louse'
        nickname = os.environ['NEW_TWO_NICKNAME']
        status = "Классный день!"
        self.page.form.change_all_fields(name, surname, nickname, status)

    # Изменение никнейма на существующий
    def test_change_nickname_on_existing(self):
        nickname = 'ADshishovaaaa'
        self.page.form.change_nickname_on_existing(nickname)

    # Изменение одного из заполненных полей на пустое
    # Имя
    def test_change_empty_name(self):
        self.page.form.change_empty_field('name', '')

    # Фамилия
    def test_change_empty_surname(self):
        self.page.form.change_empty_field('surname', '')

    # Статус
    def test_change_empty_status(self):
        self.page.form.change_empty_field('status', '')

    def test_exit_go_to_profile(self):
        self.page.form.go_to_profile()