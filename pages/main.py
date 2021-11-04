import time

import utils
from pages.default import Page


class MainPage(Page):
    PATH = ''

    CONTAINER = '.content'

    MOVIE_CARD = 'div.item__film-card'
    MOVIE_CARD_TITLE = 'div.item__film-card__title'
    MOVIE_CARD_WATCH_BUTTON = 'div.item__button-title'

    TOP_CARD_RIGHT_SLIDER = 'img.js-slider-right-FilmCard'
    TOP_CARD_LEFT_SLIDER = 'img.js-slider-left-FilmCard'

    def wait_for_container(self):
        utils.wait_for_element_by_selector(self.driver, self.CONTAINER)

    def click_on_first_card(self):
        utils.wait_click_for_element_by_selector(self.driver, self.MOVIE_CARD)

    def click_on_first_card_watch_button(self):
        utils.wait_click_for_element_by_selector(self.driver, self.MOVIE_CARD_WATCH_BUTTON)

    def get_first_card_id_and_type(self):
        first_card_href = utils.wait_for_element_by_selector(self.driver, self.MOVIE_CARD).get_attribute('href')
        first_card_split = list(filter(len, first_card_href.split('/')))
        first_card_type, first_card_id = first_card_split[-2:]
        return first_card_id, first_card_type

    def get_visible_card_titles(self):
        elements = filter(lambda x: x.isDisplayed(), self.driver.find_elements_by_css_selector(self.MOVIE_CARD_TITLE))
        return [element.text for element in elements]

    def click_right_scroll(self):
        utils.wait_click_for_element_by_selector(self.driver, self.TOP_CARD_RIGHT_SLIDER)

    def is_right_scroll_visible(self):
        utils.is_visible(self.driver, self.TOP_CARD_RIGHT_SLIDER)

    def click_right_scroll_until_visible(self):
        while self.is_right_scroll_visible():
            self.click_right_scroll()

    def click_left_scroll(self):
        utils.wait_click_for_element_by_selector(self.driver, self.TOP_CARD_LEFT_SLIDER)

    def is_left_scroll_visible(self):
        utils.is_visible(self.driver, self.TOP_CARD_LEFT_SLIDER)

    def click_left_scroll_until_visible(self):
        while self.is_left_scroll_visible():
            self.click_left_scroll()
