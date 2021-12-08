from pages.login import LoginPage
from pages.movie import MoviePage
from tests.base import BaseTest
from utils.helpers import wait_for_visible, if_element_exists


class MovieTestSuite(BaseTest):
    def test_profile_transition_from_review(self):
        movie = MoviePage(self.driver, 26)
        movie.open()
        review_username = movie.get_first_reviewer_username()
        movie.go_to_first_reviewer_page()
        profile_username = movie.get_username_from_profile()
        self.assertEqual(review_username, profile_username)

    def test_rate_movie(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        rating = 10
        movie.rate_movie(rating)
        movie_rating_text = movie.get_movie_rating()
        try:
            self.assertNotEqual(movie_rating_text, 'Оцените фильм')
            movie_rating = movie.rating_to_int(movie_rating_text)
            self.assertEqual(movie_rating, rating)
        finally:
            movie.delete_rating()

    def test_change_movie_rating(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        rating = 10
        movie.rate_movie(rating)
        new_rating = 7
        movie.rate_movie(new_rating)
        movie.reload()
        movie_rating_text = movie.get_movie_rating()
        try:
            self.assertNotEqual(movie_rating_text, 'Оцените фильм')
            movie_rating = movie.rating_to_int(movie_rating_text)
            self.assertEqual(movie_rating, new_rating)
        finally:
            movie.delete_rating()

    def test_delete_rating(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        rating = 10
        movie.rate_movie(rating)
        movie.delete_rating()
        self.assertEqual(movie.get_movie_rating(), 'Оцените фильм')

    def test_no_review_box_for_unauthorized(self):
        movie = MoviePage(self.driver, 26)
        movie.open()
        self.assertFalse(movie.review_box.if_review_container_exists())

    def test_review_long_title(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        long_title = 'Long' * 51
        movie.review_box.fill_review_title(long_title)
        self.assertEqual(movie.review_box.validation_hint, 'Введите заголовок до 200 символов!')

    def test_review_long_content(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        long_content = 'Long' * 1251
        movie.review_box.fill_review_content(long_content)
        self.assertEqual(movie.review_box.validation_hint, 'Введите текст рецензии до 5000 символов!')

    def test_review_empty_title(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        movie.review_box.fill_review('', 'content', 'positive')
        movie.review_box.submit_review()
        self.assertEqual(movie.review_box.validation_hint, 'Заполните все поля!')

    def test_review_empty_content(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        movie.review_box.fill_review('title', '', 'positive')
        movie.review_box.submit_review()
        self.assertEqual(movie.review_box.validation_hint, 'Заполните все поля!')

    def test_review_empty_type(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        movie.review_box.fill_review('title', 'content', '')
        movie.review_box.submit_review()
        self.assertEqual(movie.review_box.validation_hint, 'Заполните все поля!')

    def test_create_review(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        movie.review_box.fill_review('title', 'content', 'positive')
        movie.review_box.submit_review()
        wait_for_visible(self.driver, movie.review_box.EDIT_REVIEW)

        try:
            self.assertTrue(if_element_exists(self.driver, movie.review_box.EDIT_REVIEW))
            self.assertTrue(if_element_exists(self.driver, movie.review_box.DELETE_REVIEW))
            self.assertEqual(movie.review_box.your_review_title, 'title')
            self.assertEqual(movie.review_box.your_review_content, 'content')
        finally:
            movie.review_box.delete_review()

    def test_edit_review(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        movie = MoviePage(self.driver, 26)
        movie.open()
        movie.review_box.fill_review('title', 'content', 'positive')
        movie.review_box.submit_review()
        wait_for_visible(self.driver, movie.review_box.EDIT_REVIEW)

        try:
            self.assertTrue(if_element_exists(self.driver, movie.review_box.EDIT_REVIEW))
            self.assertTrue(if_element_exists(self.driver, movie.review_box.DELETE_REVIEW))
            self.assertEqual(movie.review_box.your_review_title, 'title')
            self.assertEqual(movie.review_box.your_review_content, 'content')
        except:
            movie.review_box.delete_review()

        movie.review_box.edit_review(' 1', ' new', 'negative')
        movie.review_box.submit_review()
        wait_for_visible(self.driver, movie.review_box.EDIT_REVIEW)

        try:
            self.assertTrue(if_element_exists(self.driver, movie.review_box.EDIT_REVIEW))
            self.assertTrue(if_element_exists(self.driver, movie.review_box.DELETE_REVIEW))
            self.assertEqual(movie.review_box.your_review_title, 'title 1')
            self.assertEqual(movie.review_box.your_review_content, 'content new')
        finally:
            movie.review_box.delete_review()
