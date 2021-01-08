# -*- coding: utf-8 -*-
import os
import unittest

from selenium.common.exceptions import TimeoutException
from casses.base.BaseTest import BaseTest
from pages.IdPage import Main_page


class MainPageTests(BaseTest, unittest.TestCase):
    def setUp(self) -> None:
        super(MainPageTests, self).setUp()
        id_page = Main_page(self.driver)
        id_page.open(id_page.BASE_URL)
        self.main_page = Main_page(self.driver)

    def go_to_main(self):
        self.main_page.open(self.main_page.BASE_URL)

    def go_to_popup(self):
        self.main_page.open_popup()

    def clear_email_after_tests(self):
        try:
            self.main_page.clear_reserve_email()
        except TimeoutException:  # Значит Email уже очищен
            pass

    def test_go_to_all_settings(self):
        self.go_to_main()
        text = self.main_page.click_get_all_settings()
        self.assertEqual(text, "Контакты и адреса")

    def test_change_personal_info(self):
        self.go_to_main()
        text = self.main_page.click_change_personal_info()
        self.assertEqual(text, "Личные данные")

    def test_click_add_reserve_email(self):
        self.go_to_main()
        text = self.main_page.click_add_reserve_email()
        self.assertEqual(text, "Добавление резервной почты")

    def test_check_empty_email(self):
        self.go_to_popup()
        res = self.main_page.add_email("")
        self.assertEqual(res, "Укажите почту")

    def test_check_incorrect_email(self):
        self.go_to_popup()
        res = self.main_page.add_email("asd")
        self.assertEqual(res, "Неправильная почта. Укажите другую.")

    def test_check_correct_email(self):
        self.go_to_popup()
        header = self.main_page.add_email("correct@yandex.ru", has_error=False)
        self.assertEqual(header, "Резервная почта добавлена")
        self.clear_email_after_tests()

    def test_close_pop_up(self):
        self.go_to_popup()
        page_header_text = self.main_page.close_pop_up()
        self.assertEqual(page_header_text, "Контакты и адреса")
