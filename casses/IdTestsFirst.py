# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.common.exceptions import TimeoutException

from pages.AuthPage import AuthPage
from pages.IdPage import Main_page
from pages.PersonalDataPage import Data_page
from steps.PersonalDataSteps import InputAnnotationsErrors


class IdMainPageAndPersonalDataTests(unittest.TestCase):
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
        self.main_page = Main_page(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def go_to_main(self):
        self.main_page.open(self.main_page.BASE_URL)

    def go_to_popup(self):
        self.main_page.open_popup()

    def clear_email_after_tests(self):
        try:
            self.main_page.clear_reserve_email()
        except TimeoutException:
            pass

    def test_go_to_all_settings(self):
        self.go_to_main()
        ok = self.main_page.click_get_all_settings()
        self.assertTrue(ok)

    def test_change_personal_info(self):
        self.go_to_main()
        ok = self.main_page.click_change_personal_info()
        self.assertTrue(ok)

    # def test_avatar_change(self):
    #     self.data_page.open(self.data_page.BASE_URL)
    #     test_path = os.path.abspath("./avatar.jpg")
    #     self.assertTrue(self.data_page.change_avatar(test_path))

    def test_click_add_reserve_email(self):
        self.clear_email_after_tests()
        self.go_to_main()
        ok = self.main_page.click_add_reserve_email()
        self.assertTrue(ok)

    def test_check_empty_email(self):
        self.clear_email_after_tests()
        self.go_to_popup()
        res = self.main_page.add_email("")
        self.assertEqual(res, "Укажите почту")

    def test_check_incorrect_email(self):
        self.clear_email_after_tests()
        self.go_to_popup()
        res = self.main_page.add_email("asd")
        self.assertEqual(res, "Неправильная почта. Укажите другую.")

    def test_check_correct_email(self):
        self.clear_email_after_tests()
        self.go_to_popup()
        header = self.main_page.add_email("correct@yandex.ru")
        self.assertEqual(header, "Резервная почта добавлена")
        self.clear_email_after_tests()

    def test_empty_city(self):
        self.data_page.open(self.data_page.BASE_URL)
        errors = self.data_page.fill_form("Имя", "Фамилия", "Никнейм", "")
        self.assertEqual(errors.city_err, "Укажите город")
        self.assertEqual(errors.name_err, "")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "")

    def test_fill_form_with_empty_name(self):
        self.data_page.open(self.data_page.BASE_URL)
        errors = self.data_page.fill_form("", "Фамилия", "Никнейм", "Москва")
        self.assertEqual(errors.city_err, "")
        self.assertEqual(errors.name_err, "Укажите имя")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "")

    def test_city_wrong(self):
        self.data_page.open(self.data_page.BASE_URL)
        errors = self.data_page.fill_form("Имя", "Фамилия", "Никнейм", "123")
        self.assertEqual(errors.city_err, "Проверьте название города")
        self.assertEqual(errors.name_err, "")
        self.assertEqual(errors.last_name_err, "")
        self.assertEqual(errors.nickname_err, "")

    def test_fill_with_empty_nickanme(self):
        self.data_page.open(self.data_page.BASE_URL)
        errors = self.data_page.fill_form("Имя", "Фамилия", "", "Москва")
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

    def test_all_ok_data(self):
        self.data_page.open(self.data_page.BASE_URL)
        errors = self.data_page.fill_form("Имя2", "Фамилия2", "Никнейм2", "Москва")
        self.check_no_errors(errors)
        self.data_page.reload()
        newName, newSurname = self.main_page.get_name_surname_from_left_bar()
        self.assertEqual(newName, "Имя2")
        self.assertEqual(newSurname, "Фамилия2")

    def test_city_different_case(self):
        self.data_page.open(self.data_page.BASE_URL)
        errors = self.data_page.fill_form("Имя3", "Фамилия3", "Никнейм3", "МоСкВа")
        self.check_no_errors(errors)
        self.data_page.reload()
        newName, newSurname = self.main_page.get_name_surname_from_left_bar()
        self.assertEqual(newName, "Имя3")
        self.assertEqual(newSurname, "Фамилия3")

    def test_long_input(self):
        self.data_page.open(self.data_page.BASE_URL)
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
        self.data_page.open(self.data_page.BASE_URL)
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

    def test_close_popup(self):
        self.go_to_popup()
        ok = self.main_page.close_pop_up()
        self.assertTrue(ok)
