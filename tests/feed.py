from pages.feed import FeedPage
from pages.login import LoginPage
from pages.profile import ProfilePage
from tests.base import BaseTest
from utils.helpers import wait_for_visible


class FeedTestSuite(BaseTest):
    def test_transition_to_profile_via_avatar(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        profile = ProfilePage(self.driver, 'testuser')
        profile.open()
        profile.toggle_follow()

        feed = FeedPage(self.driver)
        feed.open()
        feed.reload()

        try:
            username = feed.first_card_username.text
            feed.go_to_profile_via_avatar()
            self.assertEqual(username, feed.username_from_profile)
        finally:
            profile.open()
            profile.toggle_follow()

    def test_transition_to_profile_via_username(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)

        profile = ProfilePage(self.driver, 'testuser')
        profile.open()
        profile.toggle_follow()

        feed = FeedPage(self.driver)
        feed.open()
        feed.reload()

        try:
            username = feed.first_card_username.text
            feed.go_to_profile_via_username()
            self.assertEqual(username, feed.username_from_profile)
        finally:
            profile.open()
            profile.toggle_follow()

    def test_transition_to_movie(self):
        login = LoginPage(self.driver)
        login.open()
        login.sign_in()
        wait_for_visible(self.driver, login.USER_NAME_HEADER)
        profile = ProfilePage(self.driver, 'testuser')
        profile.open()
        profile.toggle_follow()

        feed = FeedPage(self.driver)
        feed.open()
        feed.reload()

        try:
            movie_title = feed.first_card_movie_title
            feed.go_to_movie_page()
            self.assertEqual(movie_title, feed.movie_title_from_page)
        finally:
            profile.open()
            profile.toggle_follow()
