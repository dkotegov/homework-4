import time
import unittest

from selenium import webdriver
from Pages.auth_page import AuthPage
from Pages.profile_page import ProfilePage
from Pages.film_page import FilmPage


class CommentTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_write_comment(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        film_page = FilmPage(self.driver)
        film_page.PATH = '/film/19'
        film_page.open()
        count = film_page.get_count_comments()
        body = 'надеюсь это последний комментарий5.9'
        film_page.create_comment(body)
        check = film_page.check_new_comment(count, auth_page.USERNAME_INPUT, body)
        self.assertEqual(check, True)

    def test_empty_comment(self):
        auth_page = AuthPage(self.driver)
        auth_page.auth()
        film_page = FilmPage(self.driver)
        film_page.PATH = '/film/19'
        film_page.open()
        film_page.create_comment("")
        film_page.check_empty_comment()
