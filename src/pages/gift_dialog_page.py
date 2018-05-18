import os

from selenium.webdriver.common.keys import Keys

from src.components.base_element import BaseElement
from src.components.elements.gift_dialog_element import GiftDialogElement


class GiftDialogPage(BaseElement):

    def __init__(self, driver):
        super(GiftDialogPage, self).__init__(driver)
        self._url = 'http://ok.ru/gifts/my'
        self._gift_dialog_element = GiftDialogElement(driver)

    def set_input_value(self, elem, val):
        elem.send_keys(val)

    def send_sticker(self):
        self._gift_dialog_element.get_sticker_button().click()
        self._gift_dialog_element.get_sticker_list_button().click()
        self._gift_dialog_element.get_smile_sticker().click()
        self._gift_dialog_element.get_send_button().click()
        return

    def send_photo(self):
        self._gift_dialog_element.get_clip_button().click()
        self._gift_dialog_element.get_add_photo_button().click()
        self._gift_dialog_element.get_photo().click()
        self._gift_dialog_element.get_ready_button().click()
        self._gift_dialog_element.get_send_button().click()
        return

    def send_video(self):
        self._gift_dialog_element.get_clip_button().click()
        self._gift_dialog_element.get_add_video_button().click()
        elem = self._gift_dialog_element.get_find_video_input()
        self.set_input_value(elem, 'sdfsdf1')
        self._gift_dialog_element.get_video().click()
        self._gift_dialog_element.get_send_button().click()
        return

    def send_photo_from_computer(self):
        self._gift_dialog_element.get_clip_button().click()
        self._gift_dialog_element.get_add_photo_from_computer_button().click()
        self._gift_dialog_element.get_photo_input().send_keys(os.getcwd()+"/staticfiles/red.jpg")
        if (self._gift_dialog_element.get_loader()):
            self._gift_dialog_element.get_send_button().click()
        return

    def send_friend(self):
        self._gift_dialog_element.get_clip_button().click()
        self._gift_dialog_element.get_set_friend_button().click()
        self._gift_dialog_element.get_friend_from_list().click()
        self._gift_dialog_element.get_send_button().click()
        return

    def delete_comment(self):
        self._gift_dialog_element.get_delete_comment_button().click()
        self._gift_dialog_element.get_accept_delete_comment_button().click()
        return

    def change_text_comment(self, change_text):
        self._gift_dialog_element.get_change_comment_button().click()
        elem = self._gift_dialog_element.get_change_comment_input()
        self.set_input_value(elem, change_text)
        self._gift_dialog_element.get_send_change_comment_button().click()
        return

    def like_comment(self):
        self._gift_dialog_element.get_like_comment_button().click()
        return

    def send_text_comment(self, text):
        elem = self._gift_dialog_element.get_comment_input()
        self.set_input_value(elem, text)
        self._gift_dialog_element.get_send_button().click()
        return

    def comment_with_photo_exists(self):
        return self._gift_dialog_element.get_comment_with_photo()

    def comment_with_sticker_exists(self):
        return self._gift_dialog_element.get_comment_with_sticker()

    def comment_with_video_exists(self):
        return self._gift_dialog_element.get_comment_with_video()

    def comment_with_photo_from_computer_exists(self):
        return self._gift_dialog_element.get_sent_comment()

    def comment_with_user_exists(self):
        return self._gift_dialog_element.get_sent_friend()

    def comment_with_text_exists(self):
        return self._gift_dialog_element.get_sent_text_comment()

    def comment_with_delete_text_exists(self):
        return self._gift_dialog_element.get_sent_delete_text_comment()

    def comment_with_change_text_exists(self):
        return self._gift_dialog_element.get_send_change_text_comment()

    def like_comment_exists(self):
        return self._gift_dialog_element.get_like_comment()

