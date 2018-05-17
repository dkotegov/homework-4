from base_element import BaseElement


class AttachForm(BaseElement):
    MUSIC_BUTTON = '//a[contains(@data-l, "musicLink")]'
    DOCUMENT_INPUT = '//span[contains(@data-l, "file_upload_menu")]/input[1]'
    VIDEO_BUTTON = '//a[contains(@data-l, "videoLink")]'
    GAME_BUTTON = '//a[contains(@data-l, "gameLink")]'
    VIDEO_INPUT = '//span[contains(@data-l, "videoAttachUploadLink")]/input[1]'
    PHOTO_INPUT = '//span[contains(@data-l, "t,photo_upload_menu")]/input[1]'
    SONG = '//div[contains(@class, "track __selectable  soh-s")]'
    SEND_SONG_BUTTON = '//input[@id="hook_FormButton_button_done"]'
    DIALOG_PHOTO_INPUT = '//div[contains(@id, "ConversationAvatarDialog")]/span/input'
    PRESENT_BUTTON = '//a[contains(@data-l, "presentLink")]'
    MONEY_BUTTON = '//a[contains(@data-l, "sendMoneyLink")]'

    LOADER = '//div[@class="progress __bottom __slim"]'
    PHOTO_READY_BUTTON = '//div[@id="__plpcte_buttons"]/div/form/button[1]'

    def get_music_button(self):
        return self.get_button_by_xpath(self.MUSIC_BUTTON)

    def get_document_input(self):
        return self.get_button_by_xpath(self.DOCUMENT_INPUT)
    
    def get_song(self):
        return self.get_field_by_xpath(self.SONG)

    def get_send_song_button(self):
        return self.get_button_by_xpath(self.SEND_SONG_BUTTON)

    def get_photo_input(self):
        return self.get_button_by_xpath(self.PHOTO_INPUT)
    
    def get_video_input(self):
        return self.get_hidden_input_by_xpath(self.VIDEO_INPUT)

    def get_video_button(self):
        return self.get_field_by_xpath(self.VIDEO_BUTTON)

    def get_loader(self):
        return self.existance_of_element_in_dom_by_xpath(self.LOADER)

    def get_dialog_photo(self):
        return self.get_hidden_input_by_xpath(self.DIALOG_PHOTO_INPUT)

    def existence_ready_photo_button(self):
        return self.existance_of_element_by_xpath(self.PHOTO_READY_BUTTON)

    def get_ready_photo_button(self):
        return self.get_button_by_xpath(self.PHOTO_READY_BUTTON)

    def get_game_button(self):
        return self.get_field_by_xpath(self.GAME_BUTTON)

    def get_present_button(self):
        return self.get_field_by_xpath(self.PRESENT_BUTTON)

    def get_money_button(self):
        return self.get_field_by_xpath(self.MONEY_BUTTON)
