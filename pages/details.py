from pages.default import Page
from components.player import Player
from utils import wait_for_element_by_selector


class DetailsPage(Page):
    PATH = 'movie/'
    ID = "id"
    WRAPPER = '.detail-preview'
    TITLE = '.detail-preview__title'
    RATING = '.item__marks:last-child'
    TRANSITION_STUB = '.sub__href'
    LAST_ACTOR = '.actors__href:last-child'
    OPENED_PLAYER = '.video-player__show-animation'
    OPEN_PLAYER_BTN = '.js-play-detail'
    ADD_TO_FAVOURITE_BTN = '.js-add-favourite-detail'
    REMOVE_FROM_FAVOURITE_BTN = '.js-remove-favourite-detail'
    LIKE_BTN = '.js-like-detail'
    PRESSED_LIKE_BTN = '.js-pressed-like-detail'
    DISLIKE_BTN = '.js-dislike-detail'
    PRESSED_DISLIKE_BTN = '.js-pressed-dislike-detail'

    def __init__(self, driver, id):
        super().__init__(driver)
        self.PATH += id

    def get_title(self):
        return wait_for_element_by_selector(self.driver, self.TITLE).text

    def transit_by_stub(self):
        wait_for_element_by_selector(self.driver, self.TRANSITION_STUB).click()

    def click_on_last_actor(self):
        wait_for_element_by_selector(self.driver, self.LAST_ACTOR).click()

    def get_name_of_last_actor(self):
        return wait_for_element_by_selector(self.driver, self.LAST_ACTOR).text

    def open_player(self):
        wait_for_element_by_selector(self.driver, self.OPEN_PLAYER_BTN).click()

    def is_player_opened(self):
        try:
            wait_for_element_by_selector(self.driver, self.OPENED_PLAYER)
            return True
        except:
            return False

    def get_movie_id(self):
        return wait_for_element_by_selector(self.driver, self.WRAPPER).get_attribute(self.ID)

    def add_to_favourites(self):
        wait_for_element_by_selector(self.driver, self.ADD_TO_FAVOURITE_BTN).click()

    def remove_from_favourite(self):
        wait_for_element_by_selector(self.driver, self.REMOVE_FROM_FAVOURITE_BTN).click()

    def like(self):
        wait_for_element_by_selector(self.driver, self.LIKE_BTN).click()

    def wait_for_liked(self):
        wait_for_element_by_selector(self.driver, self.PRESSED_LIKE_BTN)

    def dislike(self):
        wait_for_element_by_selector(self.driver, self.DISLIKE_BTN).click()

    def wait_for_disliked(self):
        wait_for_element_by_selector(self.driver, self.PRESSED_DISLIKE_BTN)

    def is_liked(self):
        try:
            wait_for_element_by_selector(self.driver, self.PRESSED_LIKE_BTN)
            return True
        except:
            return False

    def is_disliked(self):
        try:
            wait_for_element_by_selector(self.driver, self.PRESSED_DISLIKE_BTN)
            return True
        except:
            return False

    def get_rating(self):
        return wait_for_element_by_selector(self.driver, self.RATING).text

    def set_player(self):
        self.player = Player(self.driver)
