from components.base_component import BaseComponent


class NotesComponent(BaseComponent):
    NOTE_HREF = "//div[@class='media_feed user-statuses']/div[4]/div[1]" \
                " //div[@class='media-text_cnt_tx emoji-tx textWrap']/a"
    NOTE_INPUT = "//a[@data-l='t,feed.posting.ui.input']"
    NOTE_INPUT_TEXT = "//div[@data-module='postingForm/mediaText']"
    SUBMIT_BUTTON = "//div[@class='posting_submit button-pro']"
    CHECK_SEARCH = "//div[@class='feed-list'] and /a[contains(@href,'/profile/578592967841/')]"
    FRIENDS_NEWS_BUTTON = "//a[contains(@href,'filterGroupId=311')]"
    NOTE_RECEIVER_HREF = "//div[@class='feed-list']/div[2] //div[contains(@class, 'media-text_cnt_tx emoji-tx textWrap')]//a"
    #DELETE_HOVER = "//div[@class='loader-container']/div[1]/div[1]"
    #DELETE_BUTTON = "//div[@class='loader-container']/div[1]/div[1]/div[3]/div[3]/a/div"
    DELETE_HOVER = "//div[@class='media_feed user-statuses']/div[4]/div[1]/div[3]/div[3]/a/div"

    def get_note_href(self):
        return self.get_visibility_element_with_exception(self.NOTE_HREF)

    def get_note_input(self):
        return self.get_clickable_element(self.NOTE_INPUT)

    def get_submit_button(self):
        return self.get_clickable_element(self.SUBMIT_BUTTON)

    def get_note_input_text(self):
        return self.get_visibility_element(self.NOTE_INPUT_TEXT)

    def get_friends_news_button(self):
        return self.get_visibility_element(self.FRIENDS_NEWS_BUTTON)

    def get_note_receiver_href(self):
        return self.get_visibility_element_with_exception(self.NOTE_RECEIVER_HREF)

    def get_check_search(self):
        return self.get_visibility_element_with_exception(self.CHECK_SEARCH)

    def get_delete_href(self):
        return self.get_visibility_element(self.DELETE_HOVER)

    # def get_delete_button(self):
    #     return self.get_visibility_element(self.DELETE_BUTTON)
