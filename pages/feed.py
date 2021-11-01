from pages.default import DefaultPage
from utils.helpers import wait_for_visible


class FeedPage(DefaultPage):
    FEED_CARD_AVATAR = '.feed-card__avatar'
    FEED_CARD_USERNAME = '.feed-card__username'
    FEED_CARD_MOVIE_LINK = '.feed-card__movie-rating-link'
    MOVIE_TITLE = '.title-box__title'
    USER_NAME_HEADER = '#user-full-name'

    def __init__(self, driver):
        super().__init__(driver, '/feed')

    @property
    def first_card_avatar(self):
        wait_for_visible(self.driver, self.FEED_CARD_AVATAR)
        return self.driver.find_elements_by_css_selector(self.FEED_CARD_AVATAR)[0]

    @property
    def first_card_username(self):
        wait_for_visible(self.driver, self.FEED_CARD_USERNAME)
        return self.driver.find_elements_by_css_selector(self.FEED_CARD_USERNAME)[0]

    @property
    def first_card_movie_link(self):
        wait_for_visible(self.driver, self.FEED_CARD_MOVIE_LINK)
        return self.driver.find_elements_by_css_selector(self.FEED_CARD_MOVIE_LINK)[0]

    @property
    def first_card_movie_title(self):
        return self.first_card_movie_link.text[1:-1]

    @property
    def movie_title_from_page(self):
        wait_for_visible(self.driver, self.MOVIE_TITLE)
        return self.driver.find_elements_by_css_selector(self.MOVIE_TITLE)[0].text

    @property
    def username_from_profile(self):
        wait_for_visible(self.driver, self.USER_NAME_HEADER)
        return self.driver.find_element_by_css_selector(self.USER_NAME_HEADER).text

    def go_to_profile_via_avatar(self):
        self.first_card_avatar.click()

    def go_to_profile_via_username(self):
        self.first_card_username.click()

    def go_to_movie_page(self):
        self.first_card_movie_link.click()
