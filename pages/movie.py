from pages.default import DefaultPage
from utils.helpers import wait_for_visible


class MoviePage(DefaultPage):
    REVIEW_USER_LINK = '.write-review__user-link'
    USER_NAME_HEADER = '#user-full-name'
    MOVIE_RATING = '.movie-flex-right__rate-movie'
    RATING_STAR = 'label[data-rating="{}"]'
    DELETE_RATING = '#delete-rating'

    def __init__(self, driver, movie_id):
        super().__init__(driver, f'/movie/{movie_id}')

    def get_first_reviewer_username(self):
        wait_for_visible(self.driver, self.REVIEW_USER_LINK)
        return self.driver.find_element_by_css_selector(self.REVIEW_USER_LINK).text

    def get_username_from_profile(self):
        wait_for_visible(self.driver, self.USER_NAME_HEADER)
        return self.driver.find_element_by_css_selector(self.USER_NAME_HEADER).text

    def go_to_first_reviewer_page(self):
        wait_for_visible(self.driver, self.REVIEW_USER_LINK)
        self.driver.find_element_by_css_selector(self.REVIEW_USER_LINK).click()
        wait_for_visible(self.driver, self.USER_NAME_HEADER)

    def get_movie_rating(self):
        wait_for_visible(self.driver, self.MOVIE_RATING)
        return self.driver.find_element_by_css_selector(self.MOVIE_RATING).text

    def rate_movie(self, rating):
        selector = self.RATING_STAR.format(rating)
        wait_for_visible(self.driver, selector)
        self.driver.find_element_by_css_selector(selector).click()
        wait_for_visible(self.driver, self.DELETE_RATING)

    def delete_rating(self):
        wait_for_visible(self.driver, self.DELETE_RATING)
        self.driver.find_element_by_css_selector(self.DELETE_RATING).click()
