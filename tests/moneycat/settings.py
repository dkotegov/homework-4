import os

from .utils import TestCase
from .pages.settings import Settings


VALID_AVATAR = "/assets/normal.png"
BIG_AVATAR = "/assets/big.jpeg"


class MoneyCatSettingsTest(TestCase):
    def setUp(self):
        super().setUp()

        self.settings = Settings(self.driver)
        self.settings.open()

    def test_new_pass_len_less_than_6(self):
        self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass=os.environ.get("PASS"),
            new_pass="12345",
            repeat_pass="12345",
        )
        self.assertTrue(self.settings.password_form.errors)

    def test_valid_pass(self):
        self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass=os.environ.get("PASS"),
            new_pass="keklol",
            repeat_pass="keklol",
        )
        success_msg = self.settings.password_form.success_msg.text
        self.settings.password_form.clear_input()
        self.driver.refresh()

        self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass="keklol",
            new_pass=os.environ.get("PASS"),
            repeat_pass=os.environ.get("PASS"),
        )

        self.assertEqual(
            self.settings.password_form.success_msg.text,
            "Пароль успешно обновлен!",
        )

    def test_new_pass_len_more_than_30(self):
        self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass=os.environ.get("PASS"),
            new_pass="BSiaIwOqsSGNKCu9JGcZWFUEGGq5CID",
            repeat_pass="BSiaIwOqsSGNKCu9JGcZWFUEGGq5CID",
        )
        self.assertTrue(self.settings.password_form.errors)

    def test_invalid_symbols(self):
        self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass=os.environ.get("PASS"),
            new_pass="невалидный",
            repeat_pass="невалидный",
        )
        self.assertTrue(self.settings.password_form.errors)

    def test_pass_not_cmp(self):
        self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass=os.environ.get("PASS"),
            new_pass="kekkek",
            repeat_pass="kekkkk",
        )
        self.assertTrue(self.settings.password_form.errors)

    def test_change_avatar(self):
        self.settings.update_avatar(
            menu_form=self.settings.menu_form,
            avatar_form=self.settings.avatar_form,
            file_path=os.getcwd() + VALID_AVATAR,
        )
        self.assertEqual(
            self.settings.avatar_form.success_msg.text,
            "Фотография успешно обновлена!",
        )

    def test_avatar_invalid_size(self):
        self.settings.update_avatar(
            menu_form=self.settings.menu_form,
            avatar_form=self.settings.avatar_form,
            file_path=os.getcwd() + BIG_AVATAR,
        )
        self.assertEqual(
            self.settings.avatar_form.errors.text,
            "Упс, что-то пошло не так(",
        )

    def test_check_user_data(self):
        email = self.settings.open_avatar_form(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.avatar_form,
        ).text
        self.assertEqual(email, os.environ.get("LOGIN"))

    def test_open_pass_form(self):
        self.assertTrue(self.settings.open_pass_form(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
        ))

    def test_open_avatar_form(self):
        self.assertTrue(self.settings.open_avatar_form(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.avatar_form,
        ))
