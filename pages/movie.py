from pages.default import DefaultPage, Component
from utils.helpers import wait_for_visible, if_element_exists
from selenium.webdriver.support.ui import Select


class MoviePage(DefaultPage):
    REVIEW_USER_LINK = '.write-review__user-link'
    USER_NAME_HEADER = '#user-full-name'
    MOVIE_RATING = '.movie-flex-right__rate-movie'
    RATING_STAR = 'label[data-rating="{}"]'
    DELETE_RATING = '#delete-rating'

    def __init__(self, driver, movie_id):
        super().__init__(driver, f'/movie/{movie_id}')
        self.review_box = ReviewBox(self.driver)

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

    @staticmethod
    def rating_to_int(movie_rating_text):
        return int(movie_rating_text.split()[2].split('/')[0])

    def rate_movie(self, rating):
        selector = self.RATING_STAR.format(rating)
        wait_for_visible(self.driver, selector)
        self.driver.find_element_by_css_selector(selector).click()
        wait_for_visible(self.driver, self.DELETE_RATING)

    def delete_rating(self):
        wait_for_visible(self.driver, self.DELETE_RATING)
        self.driver.find_element_by_css_selector(self.DELETE_RATING).click()


class ReviewBox(Component):
    REVIEW_CONTAINER = '#user-review-container'
    REVIEW_VALIDATION_HINT = '#validation-hint-review'
    REVIEW_HEADING_INPUT = '#review-heading-input'
    REVIEW_TEXT_INPUT = '#review-text-input'
    REVIEW_TYPE_SELECT = '#select-type'
    SUBMIT_REVIEW = '#review-button'
    EDIT_REVIEW = '#edit-button'
    DELETE_REVIEW = '#delete-button'
    YOUR_REVIEW_TITLE = '.your-review__review-body .review-body__title'
    YOUR_REVIEW_CONTENT = '.your-review__review-body .review-body__content'

    @property
    def validation_hint(self):
        wait_for_visible(self.driver, self.REVIEW_VALIDATION_HINT)
        return self.driver.find_element_by_css_selector(self.REVIEW_VALIDATION_HINT).text

    @property
    def your_review_title(self):
        wait_for_visible(self.driver, self.YOUR_REVIEW_TITLE)
        return self.driver.find_element_by_css_selector(self.YOUR_REVIEW_TITLE).text

    @property
    def your_review_content(self):
        wait_for_visible(self.driver, self.YOUR_REVIEW_CONTENT)
        return self.driver.find_element_by_css_selector(self.YOUR_REVIEW_CONTENT).text

    def if_review_container_exists(self):
        return if_element_exists(self.driver, self.REVIEW_CONTAINER)

    def fill_review(self, title, content, review_type):
        self.fill_review_title(title)
        self.fill_review_content(content)
        self.select_review_type(review_type)

    def edit_review(self, title, content, review_type):
        wait_for_visible(self.driver, self.EDIT_REVIEW)
        self.driver.find_element_by_css_selector(self.EDIT_REVIEW).click()
        self.fill_review_title(title)
        self.fill_review_content(content)
        self.select_review_type(review_type)

    def submit_review(self):
        wait_for_visible(self.driver, self.SUBMIT_REVIEW)
        self.driver.find_element_by_css_selector(self.SUBMIT_REVIEW).click()

    def fill_review_title(self, title):
        wait_for_visible(self.driver, self.REVIEW_HEADING_INPUT)
        self.driver.find_element_by_css_selector(self.REVIEW_HEADING_INPUT).send_keys(title)

    def fill_review_content(self, content):
        wait_for_visible(self.driver, self.REVIEW_TEXT_INPUT)
        self.driver.find_element_by_css_selector(self.REVIEW_TEXT_INPUT).send_keys(content)

    def select_review_type(self, review_type):
        wait_for_visible(self.driver, self.REVIEW_TYPE_SELECT)
        select = Select(self.driver.find_element_by_css_selector(self.REVIEW_TYPE_SELECT))
        if review_type:
            select.select_by_value(review_type)

    def delete_review(self):
        wait_for_visible(self.driver, self.DELETE_REVIEW)
        self.driver.find_element_by_css_selector(self.DELETE_REVIEW).click()
