from selenium import webdriver
import unittest

from pages.auth_page import AuthPage


class QuestionsTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.assertEqual(1, 1)
