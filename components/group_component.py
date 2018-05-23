from components.base_component import BaseComponent


class GroupComponent(BaseComponent):
    START_BLOCK_BUTTON = "//span[@class='dropdown_ac button-pro __sec']"
    BLOCK_BUTTON = "//div[@class='dropdown_ic ic_subscribe-off']"
    NEW_THEME = "//div[@class='input_placeholder']"
    MESSAGE_INPUT = "//div[@data-module='postingForm/mediaText']"
    SEND_BUTTON = "//div[@class='posting_submit button-pro']"
    #HREF_ITEM = "//div[@class='feed-list']/div[2]/div/div[2]/div[3]/div/div/div/div/div/a"
    HREF_ITEM = "//div[@class='media-text_cnt_tx emoji-tx textWrap']/a"
    HREF_ITE = "//a[@class='media-text_a']"
    TEXT_ITEM = "//div[@class='feed-list']/div[2]/div/div[2]/div[3]/div/div/div/div/div"
    HREF_SENDER_ITEM = "//div[@class='media-text_cnt_tx emoji-tx textWrap']/a"
    GROUPS_NEWS_BUTTON = "//a[contains(@href,'filterGroupId=205')]"
    DOWN_ARROW = "//div[@class='ic12 ic12_arrow-down']"
    DELETE_BUTTON = "//i[@class='tico_img ic ic_delete']"

    def get_start_block_button(self):
        return self.get_element_by_path(self.START_BLOCK_BUTTON)

    def get_block_button(self):
        return self.get_visibility_element(self.BLOCK_BUTTON)

    def get_new_theme(self):
        return self.get_clickable_element(self.NEW_THEME)

    def get_message_input(self):
        return self.get_visibility_element(self.MESSAGE_INPUT)

    def get_send_button(self):
        return self.get_clickable_element(self.SEND_BUTTON)

    def get_href_item(self):
        return self.get_visibility_element_with_exception(self.HREF_ITE)

    def get_href_sender_item(self):
        return self.get_visibility_element(self.HREF_SENDER_ITEM)

    def get_text_item(self):
        return self.get_visibility_element(self.TEXT_ITEM)

    def get_groups_news_button(self):
        #return self.get_clickable_element(self.GROUPS_NEWS_BUTTON)
        #return self.get_element_by_path(self.GROUPS_NEWS_BUTTON)
        return self.get_visibility_element(self.GROUPS_NEWS_BUTTON)

    def get_down_arrow(self):
        return self.get_visibility_element(self.DOWN_ARROW)

    def get_delete_button(self):
        return self.get_clickable_element(self.DELETE_BUTTON)

