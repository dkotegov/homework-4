# coding=utf-8
import os
import unittest
from pages.auth_page import AuthPage
from selenium.webdriver import DesiredCapabilities, Remote

from pages.letter_formatting_page import LetterFormattingPage


class LetterFormattingTests(unittest.TestCase):
    USEREMAIL = 'park.test.testovich@mail.ru'
    PASSWORD = 'rha_the_best_team'
    # PASSWORD = os.environ['PASSWORD']

    BOLD_TEXT = '<strong>​​​​​​​hello</strong><br>'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        # форматирование письма
        letter_formatting_page = LetterFormattingPage(self.driver)
        letter_formatting_form = letter_formatting_page.form
        letter_formatting_form.open_writing_letter()
        letter_formatting_form.click_on_bold_icon()
        letter_formatting_form.write_some_text("hello")
        # letter_formatting_form.text_selection()
        bold_text = letter_formatting_form.get_text()
        self.assertEqual(self.BOLD_TEXT.decode('utf-8'), bold_text)
