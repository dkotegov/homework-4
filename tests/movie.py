from pages.login import LoginPage
from pages.movie import MoviePage
from tests.base import BaseTest
from utils.helpers import wait_for_visible


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
