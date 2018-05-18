# -*- coding: utf-8 -*-

from src.components.base_element import BaseElement


class GiftDialogElement(BaseElement):

    STICKER_BUTTON = '//a[@class="disc_toolbar_i_ic smiles_w __more"]'
    STICKER_LIST_BUTTON = '//a[@class="js-tabs-t comments_smiles_tabs_i __smiles"]'
    SMILE_STICKER = '//img[@class="emoji emoji_ok_26"]'

    SEND_BUTTON = '//div[@uid="sendComment"]'
    SEND_CHANGE_COMMENT_BUTTON = '//div[@id="ok-e-d_button"]'

    COMMENT_WITH_STICKER = '//img[@class="emoji emoji_ok_26"]'
    CLIP_BUTTON = '//a[@class="disc_toolbar_i_ic smiles_w __staple"]'

    ADD_PHOTO_BUTTON = '//a[contains(@data-l, "t,photoLink")]/span[contains(@class, "tico")]'

    SELECT_PHOTO_BUTTON = '//img[@class="photo-crop_img"]'
    READY_BUTTON = '//input[@id="hook_FormButton_button_attach"]'

    COMMENT_WITH_PHOTO = '//div[contains(@class, "collage")]'

    VIDEO_BUTTON = '//a[@data-l="t,videoLink"]'

    INPUT_FIND_VIDEO = '//input[@id="attachVideoQuery"]'
    INPUT_COMMENT_MESSAGE = '//div[@class="ok-e js-ok-e add-placeholder add-caret __empty"]'
    INPUT_CHANGE_COMMENT = '//div[@id="ok-e-d"]'

    LIKE_COMMENT_BUTTON = '//div[@id="d-klass-klass-d-id-cmnt-local--100"]'
    LIKE_COMMENT = '//span[@class="tico_img ic ic_klass-o"]'

    SELECT_VIDEO = '//img[@src="//pimg.mycdn.me/getImage?disableStub=true&type=VIDEO_S_368&url=http%3A%2F%2Fvdp.mycdn.me%2FgetImage%3Fid%3D64640453334%26idx%3D3%26thumbType%3D32%26f%3D1&signatureToken=tSToFK4xGZaDwHtNCObT9Q"]'
    COMMENT_WITH_VIDEO = '//img[@class="vid-card_img"]'
    COMMENT_WITH_TEXT = '//*[contains(text(),"Hello!")]'
    COMMENT_WITH_DELETE_TEXT = '//*[contains(text(),"Test delete comment!")]'

    ADD_PHOTO_FROM_COMPUTER_BUTTON = '//span[@data-l="t,photo_upload_menu"]'
    PHOTO_INPUT = '//span[contains(@data-l, "t,photo_upload_menu")]/input[1]'
    SENT_MESSAGE = '//a[contains(@class,"collage_cnt image-hover")]'
    SET_FRIEND_BUTTON = '//span[@data-l="t,mention"]'

    # FIRST_FRIEND = '//img[@src="//i.mycdn.me/image?id=838343541059&t=32&plc=WEB&tkn=*3mzOlIwyGgxWXyErpIW2bgqZPLw"]'
    FIRST_FRIEND = '//ul[contains(@class, "suggest_ul")]/li[2]'

    SENT_FRIEND = '//a[@data-user-id="589325601063"]'
    # SENT_FRIEND = '//a[@href="/technopark17.technopark17"]'
    # SENT_FRIEND = '//div[contains(@class, "d_comment_text")]/div/a'

    DELETE_COMMENT_BUTTON = '//a[@uid="delComment"]'
    ACCEPT_DELETE_BUTTON = '//input[@value="Удалить"]'

    CHANGE_COMMENT_BUTTON = '//a[@uid="editComment"]'
    CHANGE_COMMENT = '//*[contains(text(),"Test comment!Changed text")]'

    LOADER = '//div[@class="progress __bottom __slim"]'

    def get_sticker_button(self):
        return self.get_button_by_xpath(self.STICKER_BUTTON)

    def get_sticker_list_button(self):
        return self.get_button_by_xpath(self.STICKER_LIST_BUTTON)

    def get_smile_sticker(self):
        return self.get_button_by_xpath(self.SMILE_STICKER)

    def get_send_button(self):
        return self.get_button_by_xpath(self.SEND_BUTTON)

    def get_comment_with_sticker(self):
        return self.existence_of_element_by_xpath(self.COMMENT_WITH_STICKER)

    def get_clip_button(self):
        return self.get_button_by_xpath(self.CLIP_BUTTON)

    def get_add_photo_button(self):
        return self.get_button_by_xpath(self.ADD_PHOTO_BUTTON)

    def get_photo(self):
        return self.get_button_by_xpath(self.SELECT_PHOTO_BUTTON)

    def get_ready_button(self):
        return self.get_button_by_xpath(self.READY_BUTTON)

    def get_comment_with_photo(self):
        return self.existence_of_element_by_xpath(self.COMMENT_WITH_PHOTO)

    def get_add_video_button(self):
        return self.get_button_by_xpath(self.VIDEO_BUTTON)

    def get_find_video_input(self):
        return self.get_field_by_xpath(self.INPUT_FIND_VIDEO)

    def get_video(self):
        return self.get_button_by_xpath(self.SELECT_VIDEO)

    def get_comment_with_video(self):
        return self.existence_of_element_by_xpath(self.COMMENT_WITH_VIDEO)

    def get_add_photo_from_computer_button(self):
        return self.get_button_by_xpath(self.ADD_PHOTO_FROM_COMPUTER_BUTTON)

    def get_photo_input(self):
        return self.get_hidden_input_by_xpath(self.PHOTO_INPUT)

    def get_loader(self):
        return self.existence_of_element_by_xpath(self.LOADER)

    def get_sent_comment(self):
        return self.existence_of_element_by_xpath(self.SENT_MESSAGE)

    def get_set_friend_button(self):
        return self.get_button_by_xpath(self.SET_FRIEND_BUTTON)

    def get_friend_from_list(self):
        return self.get_button_by_xpath(self.FIRST_FRIEND)

    def get_sent_friend(self):
        return self.existence_of_element_by_xpath(self.SENT_FRIEND)

    def get_comment_input(self):
        return self.get_field_by_xpath(self.INPUT_COMMENT_MESSAGE)

    def get_sent_text_comment(self):
        return self.existence_of_element_by_xpath(self.COMMENT_WITH_TEXT)

    def get_delete_comment_button(self):
        return self.get_button_by_xpath(self.DELETE_COMMENT_BUTTON)

    def get_accept_delete_comment_button(self):
        return self.get_button_by_xpath(self.ACCEPT_DELETE_BUTTON)

    def get_sent_delete_text_comment(self):
        return self.existence_of_element_by_xpath(self.COMMENT_WITH_DELETE_TEXT)

    def get_change_comment_button(self):
        return self.get_button_by_xpath(self.CHANGE_COMMENT_BUTTON)

    def get_send_change_comment_button(self):
        return self.get_button_by_xpath(self.SEND_CHANGE_COMMENT_BUTTON)

    def get_change_comment_input(self):
        return self.get_field_by_xpath(self.INPUT_CHANGE_COMMENT)

    def get_send_change_text_comment(self):
        return self.existence_of_element_by_xpath(self.CHANGE_COMMENT)

    def get_like_comment_button(self):
        return self.get_button_by_xpath(self.LIKE_COMMENT_BUTTON)

    def get_like_comment(self):
        return self.existence_of_element_by_xpath(self.LIKE_COMMENT)
