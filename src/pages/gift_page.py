# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webelement import WebElement

from src.components.base_element import BaseElement
from src.components.elements.gift_element import GiftElement
from src.components.elements.gift_sent_element import GiftSentElement
from src.components.elements.search_gift_element import SearchGiftElement
from src.pages.actual_gift_page import ActualGiftPage
from src.pages.auth_page import AuthPage
from src.pages.authors_gift_page import AuthorsGiftPage
from src.pages.create_gift_page import CreateGiftPage
from src.pages.postcard_page import PostCardPage
from src.pages.vip_gift_page import VipGiftPage


class GiftPage(BaseElement):

    def __init__(self, driver):
        super(GiftPage, self).__init__(driver)
        self._url = 'https://ok.ru/gifts'
        self._gift_element = GiftElement(driver)
        self._auth_page = AuthPage(driver)
        self._gift_sent_element = GiftSentElement(driver)
        self._search_gift_element = SearchGiftElement(driver)

    def is_loaded(self):
        return self._gift_element.is_marked()

    def is_gift_sent(self):
        return self._gift_sent_element.is_gift_sent()

    def is_search_done(self):
        return self._search_gift_element.is_search_done()

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

    def send_gift_usual(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        #   choose receiver
        receiver = self._gift_element.get_receiver()
        receiver.click()
        return GiftPage(self.driver)

    def search_gift(self):
        text_input = "flower"
        edit_text_search_gift = self._gift_element.get_edit_text()
        edit_text_search_gift.send_keys(text_input)

        return GiftPage(self.driver)

    def send_gift_by_receivers_name(self):
        #   clicking on gift
        present = self._gift_element.get_present()
        present.click()

        #   finding receiver
        text_input = ('Космос').decode('utf-8')
        edit_text_find_reciever = self._gift_element.get_edit_text_find_receiver()
        edit_text_find_reciever.send_keys(text_input)

        receiver = self._gift_element.get_receiver()
        receiver.click()
        return GiftPage(self.driver)

    def open(self):
        self._auth_page.open_and_sign_in()
        self.driver.get(self._url)
