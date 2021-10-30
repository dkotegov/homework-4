from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helpers import Page
from components import Login


class AwaitReviewsPage(Page):
    PATH = "user/review/await"
    POPUP = ".review-user-content"
    REVIEW_CARD = ".one-await-review-inner"
    CLOSE_BUTTON = ".review-user-content-inner__close"
    SKIP_BUTTON = ".review-user-content-inner-body-button__skip"
    RATE_BUTTON = ".review-user-content-inner-body-button__review"
    ERROR = ".review-user-content-inner-body__error"

    @property
    def login(self):
        return Login(self.driver)

    def is_popup_opened(self):
        return self.helpers.is_contains(self.POPUP)

    def is_error(self):
        return self.helpers.get_element(self.ERROR) is not None

    def click_card(self):
        self.helpers.get_elements(self.REVIEW_CARD)[0].click()

    def click_close(self):
        self.helpers.click_button(self.CLOSE_BUTTON)

    def click_skip(self):
        self.helpers.click_button(self.SKIP_BUTTON)

    def click_rate(self):
        self.helpers.click_button(self.RATE_BUTTON)

    def count_cards(self):
        return len(self.helpers.get_elements(self.REVIEW_CARD))