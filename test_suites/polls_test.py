import os
import unittest
from selenium import webdriver

from pages.auth_page import AuthPage
from pages.ask_page import AskPage


class PollsTest(unittest.TestCase):
    USER = (os.environ['LOGIN_1'], os.environ['PASSWORD_1'])

    TOPIC = 'Кто ты сегодня?'
    FIRST_OPTION = 'Хорошая уточка'
    SECOND_OPTION = 'Недовольный опоссум'

    def setUp(self) -> None:
        self.driver = webdriver.Chrome('./chromedriver')

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login(*self.USER)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_one_option(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.open_poll_tab()
        ask_page.set_topic(self.TOPIC)
        ask_page.set_first_option(self.FIRST_OPTION)
        ask_page.set_category()
        ask_page.set_subcategory()
        self.assertEqual(ask_page.is_button_disabled(), True)

    def test_delete_option(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.open_poll_tab()
        ask_page.set_first_option(self.FIRST_OPTION)
        ask_page.delete_first_option()
        self.assertEqual(ask_page.get_first_option(), '')

    def test_new_option_appearance(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.open_poll_tab()
        ask_page.click_on_third_option()
        self.assertEqual(ask_page.is_forth_option_present(), True)
