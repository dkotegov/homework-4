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
            movie_rating = int(movie_rating_text.split()[2].split('/')[0])
            self.assertEqual(movie_rating, rating)
        finally:
            movie.delete_rating()
