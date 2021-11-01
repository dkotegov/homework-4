from pages.feed import FeedPage
from pages.login import LoginPage
from pages.profile import ProfilePage
from tests.base import BaseTest


class FeedTestSuite(BaseTest):
    def test_transition_to_profile_via_avatar(self):
        login = LoginPage(self.driver)
        profile = ProfilePage(self.driver, 'testuser')
        feed = FeedPage(self.driver)

        login.open()
        login.sign_in()
        profile.open()
        profile.toggle_follow()

        feed.open()
        username = feed.first_card_username.text
        feed.go_to_profile_via_avatar()

        try:
            self.assertEqual(username, feed.username_from_profile)
        finally:
            profile.open()
            profile.toggle_follow()

    def test_transition_to_profile_via_username(self):
        login = LoginPage(self.driver)
        profile = ProfilePage(self.driver, 'testuser')
        feed = FeedPage(self.driver)

        login.open()
        login.sign_in()
        profile.open()
        profile.toggle_follow()

        feed.open()
        username = feed.first_card_username.text
        feed.go_to_profile_via_username()

        try:
            self.assertEqual(username, feed.username_from_profile)
        finally:
            profile.open()
            profile.toggle_follow()

    def test_transition_to_movie(self):
        login = LoginPage(self.driver)
        profile = ProfilePage(self.driver, 'testuser')
        feed = FeedPage(self.driver)

        login.open()
        login.sign_in()
        profile.open()
        profile.toggle_follow()

        feed.open()
        movie_title = feed.first_card_movie_title
        feed.go_to_movie_page()

        try:
            self.assertEqual(movie_title, feed.movie_title_from_page)
        finally:
            profile.open()
            profile.toggle_follow()
