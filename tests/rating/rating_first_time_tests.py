import unittest
import os

from Pages.film_page import FilmPage
from tests.default_setup import default_setup
from steps.signup import signup
from steps.delete_user import delete_user


class RatingTestsFirst(unittest.TestCase):

    signup_login_success = "abrikos-soska"
    signup_password = "12345678"
    signup_mail = "qwer@mail.ru"
    expected_notification_success = "Вы успешно проголосвали!"
    expected_notification_empty = "Вы не выбрали голос!"

    def setUp(self):
        default_setup(self)
        signup(self, self.signup_login_success, self.signup_password, self.signup_mail)
        self.film_page = FilmPage(self.driver)
        self.film_page.open()

    def tearDown(self):
        delete_user(self)
        self.driver.quit()

    def test_rate_new(self):
        self.film_page.select_star()
        self.film_page.submit_star()
        notification_text = self.film_page.get_notification_text()
        self.assertEqual(notification_text, self.expected_notification_success)

    def test_rate_empty(self):
        self.film_page.submit_star()
        notification_text = self.film_page.get_notification_text()
        self.assertEqual(notification_text, self.expected_notification_empty)
