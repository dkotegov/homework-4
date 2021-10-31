from helpers import Page, Component
from components import Login


class ReviewPopup(Component):
    POPUP = ".review-user-content"
    CLOSE_BUTTON = ".review-user-content-inner__close"
    SKIP_BUTTON = ".review-user-content-inner-body-button__skip"
    RATE_BUTTON = ".review-user-content-inner-body-button__review"
    ERROR = ".review-user-content-inner-body__error"

    def is_popup_opened(self):
        return self.helpers.is_contains(self.POPUP)

    def is_error(self):
        return self.helpers.get_element(self.ERROR) is not None

    def click_close(self):
        self.helpers.click_button(self.CLOSE_BUTTON)

    def click_skip(self):
        self.helpers.click_button(self.SKIP_BUTTON)

    def click_rate(self):
        self.helpers.click_button(self.RATE_BUTTON)


class AwaitReviewBlock(Component):
    REVIEW_CARD = ".one-await-review-inner"

    def click_card(self):
        self.helpers.get_elements(self.REVIEW_CARD)[0].click()

    def count_cards(self):
        return len(self.helpers.get_elements(self.REVIEW_CARD))


class UserAwaitReviewsPage(Page):
    PATH = "user/review/await"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def review_popup(self):
        return ReviewPopup(self.driver)

    @property
    def await_review_block(self):
        return AwaitReviewBlock(self.driver)
