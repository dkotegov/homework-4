from Pages.film_page import FilmPage
from steps.auth import setup_auth
from tests.default_setup import default_setup
import unittest


class CommentsTests(unittest.TestCase):
    comment = "Привет мир!"
    expected_notification_success = "Вы успешно оставили комментарий!"
    expected_notification_empty_comment = "Пустой отзыв!"

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.film_page = FilmPage(self.driver)
        self.film_page.PATH = "film/4"
        self.film_page.open()

    def tearDown(self):
        self.driver.quit()


    def test_write_comment_succes_notification(self):
        self.film_page.set_comment(self.comment)
        self.film_page.submit_comment()
        notification = self.film_page.get_notification_text()
        self.assertEqual(notification, self.expected_notification_success)

    def test_write_comment_check_count(self):
        count_before = self.film_page.get_count_comments()
        self.film_page.set_comment(self.comment)
        self.film_page.submit_comment()
        self.film_page.get_notification_text()
        count_after = self.film_page.get_count_comments()
        self.assertEqual(count_after - count_before, 1)

    def test_write_comment_check_body(self):
        self.film_page.set_comment(self.comment)
        self.film_page.submit_comment()
        self.film_page.get_notification_text()
        last_comment = self.film_page.get_last_comment()
        self.assertEqual(last_comment, self.comment)

    def test_write_comment_check_author(self):
        self.film_page.set_comment(self.comment)
        self.film_page.submit_comment()
        self.film_page.get_notification_text()
        author = self.film_page.get_last_comment_author()
        self.assertEqual(author, self.LOGIN)


    def test_write_comment_empty(self):
        self.film_page.submit_comment()
        notification = self.film_page.get_notification_text()
        self.assertEqual(notification, self.expected_notification_empty_comment)
