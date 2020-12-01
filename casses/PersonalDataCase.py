# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.AuthPage import AuthPage
from pages.IdPage import Main_page
from pages.PersonalDataPage import Data_page
from steps.PersonalDataSteps import InputAnnotationsErrors


class PersonalDataTests(unittest.TestCase):
    def setUp(self) -> None:
        browser = os.environ.get("BROWSER", "CHROME")
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )

        LOGIN = os.environ["LOGIN"]
        PASSWORD = os.environ["PASSWORD"]

        auth_page = AuthPage(self.driver)
        auth_page.auth(LOGIN, PASSWORD)
        id_page = Main_page(self.driver)
        id_page.open(id_page.BASE_URL)
        self.data_page = Data_page(self.driver)
        self.data_page.open(self.data_page.BASE_URL)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_empty_city(self):
        errors = self.data_page.fill_form("Имя", "Фамилия", "Никнейм", "", collect_err_about="city")
        self.assertEqual(errors.city_err, "Укажите город")
        self.assertEqual(errors.name_err, "")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "")

    def test_fill_form_with_empty_name(self):
        errors = self.data_page.fill_form("", "Фамилия", "Никнейм", "Москва", collect_err_about="name")
        self.assertEqual(errors.city_err, "")
        self.assertEqual(errors.name_err, "Укажите имя")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "")

    def test_city_wrong(self):
        errors = self.data_page.fill_form("Имя", "Фамилия", "Никнейм", "123", collect_err_about="city",
                                          is_city_correct=False)
        self.assertEqual(errors.city_err, "Проверьте название города")
        self.assertEqual(errors.name_err, "")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "")

    def test_fill_with_empty_nickanme(self):
        errors = self.data_page.fill_form("Имя", "Фамилия", "", "Москва", collect_err_about="nickname")
        self.assertEqual(errors.city_err, "")
        self.assertEqual(errors.name_err, "")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "Укажите никнейм")

    def check_no_errors(self, errors: InputAnnotationsErrors):
        if (
                errors.name_err == ""
                and errors.city_err == ""
                and errors.last_name_err == ""
                and errors.nickname_err == ""
        ):
            return True
        return False

    def test_long_input(self):
        errors = self.data_page.fill_form(
            "ashgdjhasgdhasjkdhaskjhdkjashdkjashkjdhaskjhdkjashkdjhaskjdhkjashdkj",
            "ashgdjhasgdhasjkdhaskjhdkjashdkjashkjdhaskjhdkjashkdjhaskjdhkjashdkj",
            "ashgdjhasgdhasjkdhaskjhdkjashdkjashkjdhaskjhdkjashkdjhaskjdhkjashdkj",
            "Москва",
        )
        self.assertEqual(errors.city_err, "")
        self.assertEqual(
            errors.name_err,
            "Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов",
        )
        self.assertEqual(
            errors.last_name_err,
            "Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов",
        )
        self.assertEqual(
            errors.nickname_err,
            "Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов",
        )

    def test_inputs_special_char(self):
        errors = self.data_page.fill_form(
            "%$^&!@$^!@*!@*", "%$^&!@$^!@*!@*", "%$^&!@$^!@*!@*", "Москва"
        )
        self.assertEqual(errors.city_err, "")
        self.assertEqual(
            errors.name_err,
            "Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов",
        )
        self.assertEqual(
            errors.last_name_err,
            "Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов",
        )
        self.assertEqual(
            errors.nickname_err,
            "Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов",
        )

    def test_change_avatar(self):
        self.data_page.open(self.data_page.BASE_URL)
        test_path = os.path.abspath("./avatar.jpg")
        self.assertTrue(self.data_page.change_avatar(test_path))

    def test_all_ok_data(self):
        errors = self.data_page.fill_form("Имя2", "Фамилия2", "Никнейм2", "Москва")
        self.check_no_errors(errors)
        self.data_page.reload()
        newName, newSurname = self.data_page.get_name_surname_from_left_bar()
        self.assertEqual(newName, "Имя2")
        self.assertEqual(newSurname, "Фамилия2")

    def test_different_case(self):
        errors = self.data_page.fill_form("Имя3", "Фамилия3", "Никнейм3", "МоСкВа")
        self.check_no_errors(errors)
        self.data_page.reload()
        newName, newSurname = self.data_page.get_name_surname_from_left_bar()
        self.assertEqual(newName, "Имя3")
        self.assertEqual(newSurname, "Фамилия3")
