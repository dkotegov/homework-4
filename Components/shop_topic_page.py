# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys

from Components.component import Component


class TopicPopup(Component):
    POPUP = '//div[@id="mtLayerMain"]'
    CREATE_TOPIC = '//a[contains(@data-l, "OpenPostingPopup")]'
    TOPIC_TEXT = '//div[@data-module="postingForm/mediaText"]'
    SUBMIT = '//div[@class="posting_submit button-pro"]'

    def open(self):
        super(TopicPopup, self).click_element(self.CREATE_TOPIC)

    def set_text(self, text):
        super(TopicPopup, self).input_text(self.TOPIC_TEXT, text)

    def submit(self):
        super(TopicPopup, self).click_element(self.SUBMIT)
        self.waiting_closing()

    def waiting_closing(self):
        super(TopicPopup, self).waiting_until_invisible(self.POPUP)


class TopicWidget(Component):
    TOPIC_TEXT = '//div[contains(@class,"media-text_cnt_tx")]'
    TOPIC_SHOP_NAME = '//span[@class="shortcut-wrap"]/a[contains(@hrefattrs,"VisitProfile")]'
    TOPIC_AUTHOR = '//span[@class="shortcut-wrap"]/a[contains(@hrefattrs,"userMain")]'

    def get_topic_text(self):
        return super(TopicWidget, self).get_element_text(self.TOPIC_TEXT)

    def get_topic_shop_name(self):
        return super(TopicWidget, self).get_element_text(self.TOPIC_SHOP_NAME)

    def get_topic_author(self):
        return super(TopicWidget, self).get_element_text(self.TOPIC_AUTHOR)


class TopicTags(Component):
    ADD_TAGS_BUTTON = '//a[contains(@href,"AddTopicTag")]'
    EDIT_TAG = '//a[contains(@href,"EditTopicTag")]'

    REMOVE_TAG_BUTTON_TEMPLATE = '//div[@class="tag"]//span[../../span="{}"]'
    SUBMIT = '//span[contains(@class,"tag-box_button")]'

    TAG = '//a[contains(@hrefattrs,"_TopicTag")]'
    TAG_TEMPLATE = '//a[contains(@hrefattrs,"_TopicTag") and text()="{}"]'
    TAGS_INPUT = '//input[@name="st.newTag"]'

    HASHTAG = '//a[contains(@class,"__hashtag")]'
    HASHTAG_TEMPLATE = '//a[contains(@class,"__hashtag") and text()="#{}"]'

    ERROR = '//span[@class="input-e"]'
    TAG_LENGTH_COUNTER = '//span[contains(@class,"txt-counter")]'

    def open_tags_input(self):
        super(TopicTags, self).click_element(self.ADD_TAGS_BUTTON)

    def set_tag(self, tag):
        super(TopicTags, self).input_text(self.TAGS_INPUT, tag)
        super(TopicTags, self).input_key(self.TAGS_INPUT, Keys.ENTER)

    def remove_tag(self, tag):
        remove_tag_button = self.REMOVE_TAG_BUTTON_TEMPLATE.format(tag)
        super(TopicTags, self).click_element(remove_tag_button)

    def edit_tags(self):
        super(TopicTags, self).click_element(self.EDIT_TAG)

    def is_exist_temp_tag(self, tag):
        tag_element = self.TAG_TEMPLATE.format(tag)
        return super(TopicTags, self).is_exist_element(tag_element)

    def no_one_hashtags(self):
        return not super(TopicTags, self).is_exist_element(self.HASHTAG)

    def is_exist_hashtag(self, hashtag):
        hashtag_element = self.HASHTAG_TEMPLATE.format(hashtag)
        return super(TopicTags, self).is_exist_element(hashtag_element)

    def submit(self):
        super(TopicTags, self).click_element(self.SUBMIT)

    def get_error_text(self):
        return super(TopicTags, self).get_element_text(self.ERROR)

    def get_remaining_tag_length(self):
        remaining_tag_length_str = super(TopicTags, self).get_element_text(self.TAG_LENGTH_COUNTER)
        return int(remaining_tag_length_str)

    def get_number_of_temp_tags(self):
        return super(TopicTags, self).get_number_of_elements(self.TAG)

    def get_number_of_hashtags(self):
        return super(TopicTags, self).get_number_of_elements(self.HASHTAG)
