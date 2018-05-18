from src.components.base_element import BaseElement
from src.components.elements.gift_element import GiftElement
from src.pages.auth_page import AuthPage
from src.pages.feed_page import FeedPage
from src.pages.friends_page import FriendsPage
from src.pages.games_page import GamesPage
from src.pages.groups_page import GroupsPage
from src.pages.inventories_page import InventoriesPage
from src.pages.notes_page import NotesPage
from src.pages.photo_page import PhotoPage


class GiftPage(BaseElement):

    def __init__(self, driver):
        super(GiftPage, self).__init__(driver)
        self._url = 'http://ok.ru/gifts'
        self._element = GiftElement(driver)
        self._auth_page = AuthPage(driver)

    def is_loaded(self):
        return self._element.is_marked()

    def is_loaded_own_gifts(self):
        return self._element.is_exists_receive_gifts_nav_side()

    def open(self):
        self._auth_page.open_and_sign_in()
        self.driver.get(self._url)

    def open_feed_page_by_logo(self):
        self._element.get_logo().click()
        return FeedPage(self.driver)

    def open_feed_page_by_nav_menu(self):
        self._element.get_feed_item_nav_menu().click()
        return FeedPage(self.driver)

    def open_friends_page_by_nav_menu(self):
        self._element.get_friends_item_nav_menu().click()
        return FriendsPage(self.driver)

    def open_photo_page_by_nav_menu(self):
        self._element.get_photo_item_nav_menu().click()
        return PhotoPage(self.driver)

    def open_groups_page_by_nav_menu(self):
        self._element.get_groups_item_nav_menu().click()
        return GroupsPage(self.driver)

    def open_games_page_by_nav_menu(self):
        self._element.get_games_item_nav_menu().click()
        return GamesPage(self.driver)

    def open_notes_page_by_nav_menu(self):
        self._element.get_notes_item_nav_menu().click()
        return NotesPage(self.driver)

    def open_inventories_page_by_nav_menu(self):
        self._element.get_inventories_item_nav_menu().click()
        return InventoriesPage(self.driver)

    def open_own_gifts(self):
        self._element.get_own_gifts_nav_side_ico().click()
        return self
