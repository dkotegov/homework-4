# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import Remote, DesiredCapabilities

from pages.Question import *


class BaseTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')
        self.driver = Remote(command_executor='http://172.20.10.2:4444/wd/hub',
                             desired_capabilities=getattr(DesiredCapabilities, browser))

    def tearDown(self):
        self.driver.quit()


class AskQuestionTests(BaseTest):

    def setUp(self):
        super(AskQuestionTests, self).setUp()
        self.ask_page = OtvetPageAsk(self.driver)
        self.ask_page.open()
        self.ask_page.open_login_frame()
        t = self.ask_page.auth_form()
        t.set_login("zzz-zzzz-90")
        t.set_domain("list.ru")
        t.set_password("Qwerty12")
        t.login()
        self.ask_page.close_login_frame()

    def test_form_create_exceed_character_limit(self):
        ask = self.ask_page.ask_form()
        ask.set_text("ffffffff")
        ask.set_question_title("f" * 255)
        ask.is_symbol_extra_enabled()
        ask.set_category()
        ask.set_subcategory()
        ask.submit()
        self.driver.implicitly_wait(1)
        self.assertEqual(u"Невозможно опубликовать слишком длинный текст", self.ask_page.error_poput())

    def test_form_no_categories_selected(self):
        ask = self.ask_page.ask_form()
        ask.set_question_title("test")
        ask.submit()
        self.driver.implicitly_wait(1)
        self.assertEqual(u"Просьба более подробно и грамотно сформулировать тему вопроса.", self.ask_page.error_poput())

    def test_no_sub_ctegory(self):
        ask = self.ask_page.ask_form()
        ask.set_question_title("test")
        ask.set_category()
        ask.submit()
        self.driver.implicitly_wait(1)
        self.assertEqual(u"Просьба более подробно и грамотно сформулировать тему вопроса.", self.ask_page.error_poput())

    def test_title_empty(self):
        ask = self.ask_page.ask_form()
        ask.set_category()
        ask.set_subcategory()
        ask.submit()
        self.driver.implicitly_wait(1)
        self.assertEqual(u"Невозможно опубликовать пустой текст",
                         self.ask_page.error_poput())

    def test_form_add_picture(self):
        ask = self.ask_page.ask_form()
        ask.set_text(u"вопрос тест")
        ask.set_question_title(u"Что? Где? Когда? selenium test")
        ask.add_picture("/home/ivan/test/QA/selenium/homework-4/grumpy.png")
        ask.set_category()
        ask.set_subcategory()
        self.assertTrue(ask.is_picture_setted())


if __name__ == "__main__":
    unittest.main()