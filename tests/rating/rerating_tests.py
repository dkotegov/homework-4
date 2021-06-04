import unittest

from Pages.film_page import FilmPage
from tests.default_setup import default_setup
from steps.auth import setup_auth


class ReratingTests(unittest.TestCase):
    expected_notification_success = "Вы успешно проголосвали!"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.film_page = FilmPage(self.driver)
        self.film_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_rate_success(self):
        self.film_page.select_star()
        self.film_page.submit_star()
        notification_text = self.film_page.get_notification_text()
        self.assertEqual(notification_text, self.expected_notification_success)
