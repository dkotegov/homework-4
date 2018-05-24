# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webelement import WebElement

from src.components.base_element import BaseElement
from src.components.elements.gift_element import GiftElement
from src.components.elements.gift_not_sent_element import GiftNotSentElement
from src.components.elements.gift_sent_element import GiftSentElement
from src.components.elements.search_gift_element import SearchGiftElement
from src.pages.actual_gift_page import ActualGiftPage
from src.pages.auth_page import AuthPage
from src.pages.authors_gift_page import AuthorsGiftPage
from src.pages.create_gift_page import CreateGiftPage
from src.pages.feed_page import FeedPage
from src.pages.games_page import GamesPage
from src.pages.groups_page import GroupsPage
from src.pages.inventories_page import InventoriesPage
from src.pages.notes_page import NotesPage
from src.pages.photo_page import PhotoPage
from src.pages.postcard_page import PostCardPage
from src.pages.vip_gift_page import VipGiftPage


class GiftPage(BaseElement):

    def __init__(self, driver):
        super(GiftPage, self).__init__(driver)
        self._url = 'https://ok.ru/gifts'
        self._gift_element = GiftElement(driver)
        self._auth_page = AuthPage(driver)
        self._gift_sent_element = GiftSentElement(driver)
        self._gift_not_sent_element = GiftNotSentElement(driver)
        self._search_gift_element = SearchGiftElement(driver)
        self._driver = driver

    def is_loaded(self):
        return self._gift_element.is_marked()

    def is_gift_sent(self):
        return self._gift_sent_element.is_gift_sent()

    def is_gift_not_sent(self):
        return self._gift_not_sent_element.is_gift_not_sent()

    def is_search_done(self):
        return self._search_gift_element.is_search_done()

    def send_gift_usual(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        #   choose receiver
        receiver = self._gift_element.get_receiver()
        receiver.click()
        return GiftPage(self.driver)

    def send_gift_by_receivers_name(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        #   finding receiver
        text_input = 'kosmos'
        edit_text_find_reciever = self._gift_element.get_edit_text_find_receiver()
        edit_text_find_reciever.send_keys(text_input)

        receiver = self._gift_element.get_receiver()
        receiver.click()
        return GiftPage(self.driver)

    def send_gift_by_receivers_name_not_exists(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        #   finding receiver
        text_input = 'reciever that not exists'
        edit_text_find_reciever = self._gift_element.get_edit_text_find_receiver()
        edit_text_find_reciever.send_keys(text_input)

        return GiftPage(self.driver)

    def send_gift_by_receivers_name_big_str(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        #   finding receiver
        text_input = ''
        for i in range(0, 1000):
            text_input += 'big str'
        edit_text_find_reciever = self._gift_element.get_edit_text_find_receiver()
        edit_text_find_reciever.send_keys(text_input)

        return GiftPage(self.driver)

    def send_gift_private_by_receivers_name(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        #   finding receiver
        text_input = 'kosmos'
        edit_text_find_reciever = self._gift_element.get_edit_text_find_receiver()
        edit_text_find_reciever.send_keys(text_input)

        receiver = self._gift_element.get_receiver()
        receiver.click()
        return GiftPage(self.driver)

    def open_authors_gifts(self):
        btn = self._gift_element.get_authors_gift_button()
        btn.click()
        return AuthorsGiftPage(self.driver)

    def open_actual_gifts(self):
        btn = self._gift_element.get_actual_gift_button()
        btn.click()
        return ActualGiftPage(self.driver)

    def open_postcards(self):
        btn = self._gift_element.get_postcard_button()
        btn.click()
        return PostCardPage(self.driver)

    def open_vip_gifts(self):
        btn = self._gift_element.get_vip_gift_button()
        btn.click()
        return VipGiftPage(self.driver)

    def open_create_gift(self):
        btn = self._gift_element.get_create_gift_button()
        btn.click()
        return CreateGiftPage(self.driver)

    def send_gift_secretly(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        # this functional was putted out!!!
        #   pressing button to send gift by secret
        # secret_button = self._gift_element.get_secret_button()
        # secret_button.click()

        #   choose receiver
        receiver = self._gift_element.get_receiver()
        receiver.click()
        return GiftPage(self.driver)

    def search_gift(self):
        text_input = "flower"
        edit_text_search_gift = self._gift_element.get_edit_text()
        edit_text_search_gift.send_keys(text_input)

        return GiftPage(self.driver)

    def send_gift_private(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        #   pressing button to send gift by private
        private_button = self._gift_element.get_private_button()
        private_button.click()

        #   choose receiver
        receiver = self._gift_element.get_receiver()
        receiver.click()
        return GiftPage(self.driver)

    def open_self_gifts(self):
        self._gift_element.get_self_gifts_button().click()
        return

    def like_gift_exists(self):
        return self._gift_element.get_like_gift()
    
    def is_loaded_own_gifts(self):
        return self._gift_element.is_exists_receive_gifts_nav_side()

    def open(self):
        self._auth_page.open_and_sign_in()
        self.driver.get(self._url)

    def open_without_auth(self):
        self.driver.get(self._url)

    def open_feed_page_by_logo(self):
        self._gift_element.get_logo().click()
        return FeedPage(self.driver)

    def open_feed_page_by_nav_menu(self):
        self._gift_element.get_feed_item_nav_menu().click()
        return FeedPage(self.driver)

    def open_friends_page_by_nav_menu(self):
        self._gift_element.get_friends_item_nav_menu().click()
        return FriendsPage(self.driver)

    def open_photo_page_by_nav_menu(self):
        self._gift_element.get_photo_item_nav_menu().click()
        return PhotoPage(self.driver)

    def open_groups_page_by_nav_menu(self):
        self._gift_element.get_groups_item_nav_menu().click()
        return GroupsPage(self.driver)

    def open_games_page_by_nav_menu(self):
        self._gift_element.get_games_item_nav_menu().click()
        return GamesPage(self.driver)

    def open_notes_page_by_nav_menu(self):
        self._gift_element.get_notes_item_nav_menu().click()
        return NotesPage(self.driver)

    def open_inventories_page_by_nav_menu(self):
        self._gift_element.get_inventories_item_nav_menu().click()
        return InventoriesPage(self.driver)

    def open_own_gifts(self):
        self._gift_element.get_own_gifts_nav_side_ico().click()
        return self

    def open_add_music_editor(self):
        self._gift_element.add_music_ico().click()
        return MusicEditor(self.driver)

    def is_added_music(self):
        return self._gift_element.is_exists_added_music()

    def add_music(self):
        music_editor = self.open_add_music_editor()
        return music_editor.select_sound()

    def send_gift_with_selected_profile(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        self._gift_element.submit_send_gift()
        return GiftPage(self.driver)

    def check_gift_exist(self):
        return self._gift_element.exist_receive_gifts()

    def create_new_gift(self):
        self._gift_element.get_create_custom_gift_button().click()
        self._gift_element.switch_to_text_gift_frame()
        self._gift_element.get_create_text_gift_button().click()
        input = self._gift_element.get_create_text_gift_input()
        input.send_keys("Test gift")
        self._gift_element.get_save_custom_gift_button().click()
        self._gift_element.get_present_custom_gift_button().click()
        self._driver.switch_to_default_content()
        self._gift_element.get_select_myself_button().click()

from src.pages.friends_page import FriendsPage
from src.pages.music_editor import MusicEditor

