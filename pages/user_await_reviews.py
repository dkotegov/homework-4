from random import randrange

from helpers import Page, Component
from components import ReviewPopup, Login


class AwaitReviewBlock(Component):
    AWAIT_REVIEW_CARD = ".one-await-review"
    AWAIT_REVIEW_CARD_ID = "//div[@data-product-id={}]"

    # у нас у карточек нет своего id, но есть product_Id
    # Он уникальный для карточки на странице
    def get_card_id(self):
        elements = self.helpers.get_elements(self.AWAIT_REVIEW_CARD)
        index = randrange(len(elements)) - 1
        return elements[index].get_attribute("data-product-id")

    def is_contains_card(self, card_id):
        return self.helpers.is_contains(self.AWAIT_REVIEW_CARD_ID.format(card_id), self.helpers.SELECTOR.XPATH)

    def click_card(self, card_id):
        self.helpers.click_element(self.AWAIT_REVIEW_CARD_ID.format(card_id), self.helpers.SELECTOR.XPATH)


class UserAwaitReviewsPage(Page):
    PATH = "/user/review/await"

    PAGE = ".await-review-list"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    @property
    def login(self):
        return Login(self.driver)

    @property
    def review_popup(self):
        return ReviewPopup(self.driver)

    @property
    def await_review_block(self):
        return AwaitReviewBlock(self.driver)
