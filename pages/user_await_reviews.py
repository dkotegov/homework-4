from helpers import Page, Component
from components import Login, ReviewPopup


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
