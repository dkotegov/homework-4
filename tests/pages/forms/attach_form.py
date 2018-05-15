from base_element import BaseElement

class AttachForm(BaseElement):
    MUSIC_BUTTON = '//a[contains(@data-l, "musicLink")]'
    DOCUMENT_INPUT = '//span[contains(@data-l, "file_upload_menu")]/input[1]'
    VIDEO_BUTTON = '//a[contains(@data-l, "videoLink")]'
    VIDEO_INPUT = '//span[contains(@data-l, "videoAttachUploadLink")]/input[1]'
    PHOTO_INPUT = '//span[contains(@data-l, "t,photo_upload_menu")]/input[1]'
    SONG = '//div[contains(@class, "track __selectable  soh-s")]'
    SEND_SONG_BUTTON = '//input[@id="hook_FormButton_button_done"]'

    LOADER = '//div[@class="progress __bottom __slim"]'

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