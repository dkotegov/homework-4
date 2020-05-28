from tests.pages.settings_profile import SettingsPage
from tests.pages.solarsunrise_urls import ProfilePage
from tests.cases.base import TestAuthorized
import os


class SettingsTest(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = SettingsPage(self.driver)

    # Изменение одного из полей
    # Изменение аватарки
    def test_change_avatar(self):
        self.page.form.set_avatar()
        self.page.form.submit_ok_button()
        ProfilePage(self.driver, open=False).wait_for_load()
        self.page.form.submit_settings_button()

    # Изменение Имени
    def test_change_valid_name(self):
        name = "Nell"

        self.page.form.set_name(name)
        self.page.form.submit_ok_button()
        ProfilePage(self.driver, open=False).wait_for_load()
        self.page.form.submit_settings_button()
        SettingsPage(self.driver, open=False).wait_for_load()

        text = self.page.form.get_name(name)
        self.assertEqual(text, name, "Field was not changed")

    # Изменение Фамилии
    def test_change_valid_surname(self):
        surname = "Lin"

        self.page.form.set_surname(surname)
        self.page.form.submit_ok_button()
        ProfilePage(self.driver, open=False).wait_for_load()
        self.page.form.submit_settings_button()
        SettingsPage(self.driver, open=False).wait_for_load()

        text = self.page.form.get_surname(surname)
        self.assertEqual(text, surname, "Field was not changed")

    # Изменение статуса
    def test_change_valid_status(self):
        status = "Великолепность"

        self.page.form.set_status(status)
        self.page.form.submit_ok_button()
        ProfilePage(self.driver, open=False).wait_for_load()
        self.page.form.submit_settings_button()
        SettingsPage(self.driver, open=False).wait_for_load()

        text = self.page.form.get_status(status)
        self.assertEqual(text, status, "Field was not changed")

    # Изменение никнейма на несуществующий
    def test_change_valid_nickname(self):
        nickname = os.environ["NEW_NICKNAME"]

        self.page.form.set_nickname(nickname)
        self.page.form.submit_ok_button()
        ProfilePage(self.driver, open=False).wait_for_load()
        self.page.form.submit_settings_button()
        SettingsPage(self.driver, open=False).wait_for_load()

        text = self.page.form.get_nickname(nickname)
        self.assertEqual(text, nickname, "Field was not changed")

    # # Изменение всех полей с условием, что никнейм не существует
    def test_change_all_fields_with_valid_nickname(self):
        name = "Nelli"
        surname = "Louse"
        nickname = os.environ["NEW_TWO_NICKNAME"]
        status = "Классный день!"

        self.page.form.set_name(name)
        self.page.form.set_surname(surname)
        self.page.form.set_nickname(nickname)
        self.page.form.set_status(status)
        self.page.form.set_avatar()

        self.page.form.submit_ok_button()
        ProfilePage(self.driver, open=False).wait_for_load()
        self.page.form.submit_settings_button()
        SettingsPage(self.driver, open=False).wait_for_load()

        self.assertEqual(self.page.form.get_name(name), name, "Name was not changed")
        self.assertEqual(
            self.page.form.get_surname(surname), surname, "Surname was not changed"
        )
        self.assertEqual(
            self.page.form.get_nickname(nickname), nickname, "Nickname was not changed"
        )
        self.assertEqual(
            self.page.form.get_status(status), status, "Status was not changed"
        )

    # Изменение никнейма на существующий
    def test_change_nickname_on_existing(self):
        nickname = "ADshishovaaaa"

        self.page.form.set_nickname(nickname)
        self.page.form.submit_ok_button()
        self.assertNotEqual(
            self.page.form.wait_alert_settings(), "", "Alert not received"
        )

    # Изменение одного из заполненных полей на пустое
    # Имя
    def test_change_empty_name(self):
        text_one = self.page.form.get_value("name")
        self.page.form.set_name("")

        self.page.form.submit_ok_button()
        ProfilePage(self.driver, open=False).wait_for_load()
        self.page.form.submit_settings_button()
        SettingsPage(self.driver, open=False).wait_for_load()

        text = self.page.form.get_name(text_one)
        self.assertNotEqual(text, "", "Fields with equal values")

    # Фамилия
    def test_change_empty_surname(self):
        text_one = self.page.form.get_value("surname")
        self.page.form.set_surname("")

        self.page.form.submit_ok_button()
        ProfilePage(self.driver, open=False).wait_for_load()
        self.page.form.submit_settings_button()
        SettingsPage(self.driver, open=False).wait_for_load()

        text = self.page.form.get_surname(text_one)
        self.assertNotEqual(text, "", "Fields with equal values")

    # Статус
    def test_change_empty_status(self):
        text_one = self.page.form.get_value("status")
        self.page.form.set_status("")

        self.page.form.submit_ok_button()
        ProfilePage(self.driver, open=False).wait_for_load()
        self.page.form.submit_settings_button()
        SettingsPage(self.driver, open=False).wait_for_load()

        text = self.page.form.get_status(text_one)
        self.assertNotEqual(text, "", "Fields with equal values")

    def test_exit_go_to_profile(self):
        old_nickname = self.page.form.get_value("nickname")
        nickname = os.environ["NEW_THREE_NICKNAME"]

        self.page.form.set_nickname(nickname)
        self.page.form.submit_exit_button()
        ProfilePage(self.driver, open=False).wait_for_load()

        nick_text = self.page.form.check_nickname()
        self.assertEqual(nick_text, old_nickname, "No nickname")
