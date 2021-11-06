from helpers import Page, Component
from components import ReviewPopup, Login


class AwaitReviewBlock(Component):
    AWAIT_REVIEW_CARD = ".one-await-review"
    AWAIT_REVIEW_CARD_ID = "//div[@data-product-id={}]"

    # у нас у карточек нет своего id, но есть product_Id
    # Он уникальный для карточки на странице
    def get_card_id(self):
        element = self.helpers.get_element(self.AWAIT_REVIEW_CARD)
        return element.get_attribute("data-product-id")

    def is_contains_card(self, card_id):
        return self.helpers.is_contains(self.AWAIT_REVIEW_CARD_ID.format(card_id), self.helpers.SELECTOR.XPATH)

    def click_card(self, card_id):
        self.helpers.click_element(self.AWAIT_REVIEW_CARD_ID.format(card_id), self.helpers.SELECTOR.XPATH)


class UserAwaitReviewsPage(Page):
    PATH = "/user/review/await"

    @property
    def login(self):
        return Login(self.driver)

    @property
    def review_popup(self):
        return ReviewPopup(self.driver)

    @property
    def await_review_block(self):
        return AwaitReviewBlock(self.driver)
