# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from Components.component import Component


class TopicPopup(Component):
    POPUP = '//div[@id="mtLayerMain"]'
    CREATE_TOPIC = '//a[contains(@data-l, "OpenPostingPopup")]'
    TOPIC_TEXT = '//div[@data-module="postingForm/mediaText"]'
    SUBMIT = '//div[@class="posting_submit button-pro"]'

    def open(self):
        super(TopicPopup, self).click_element(self.CREATE_TOPIC)

    def set_text(self, text):
        super(TopicPopup, self).input_text_to_element(self.TOPIC_TEXT, text)

    def submit(self):
        super(TopicPopup, self).click_element(self.SUBMIT)
        self.waiting_closing()

    def waiting_closing(self):
        super(TopicPopup, self).waiting_until_invisible(self.POPUP)


class TopicWidget(Component):
    TOPIC_TEXT = '//div[contains(@class,"media-text_cnt_tx")]'
    TOPIC_SHOP_NAME = '//span[@class="shortcut-wrap"]/a[contains(@hrefattrs,"VisitProfile")]'
    TOPIC_AUTHOR = '//span[@class="shortcut-wrap"]/a[contains(@hrefattrs,"userMain")]'

    ADD_KEYWORD_BTN = '//a[contains(text(),"ключевые слова")]'
    KEYWORD_FIELD = '//input[@name="st.newTag"]'
    SUBMIT_KEYWORD = '//td[contains(@class,"tag-box_button_w")]'
    KEYWORD = '//a[contains(@title,"все темы")]'
    KEYWORD_EDIT_BTN = '//a[contains(@class,"tab-box_edit")]'
    HASHTAG = '//a[contains(@class,"__hashtag")]'
    KEYWORD_DELETE_BTN = '//span[contains(@class,"tag_del")]'
    OPEN_TOPIC_POPUP = '//a[contains(@class,"media-text_a")]'

    CLASS = '//span[contains(@class,"controls-list_lk")]'
    CLASS_COUNTER = '//span[contains(@class,"controls-list_lk")]/' \
                    'span[contains(@class,"widget_count") and {}(contains(@class,"__react-like"))]'

    def get_topic_text(self):
        return super(TopicWidget, self).get_element_text(self.TOPIC_TEXT)

    def get_topic_shop_name(self):
        return super(TopicWidget, self).get_element_text(self.TOPIC_SHOP_NAME)

    def get_topic_author(self):
        return super(TopicWidget, self).get_element_text(self.TOPIC_AUTHOR)

    def open_keyword_field(self):
        super(TopicWidget, self).click_element(self.ADD_KEYWORD_BTN)

    def set_keyword(self, word="word"):
        super(TopicWidget, self).input_text_to_element(self.KEYWORD_FIELD, word)

    def submit_keyword(self):
        super(TopicWidget, self).click_element(self.SUBMIT_KEYWORD)

    def get_keyword(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.KEYWORD)
        ).text

    def open_keyword_edit_field(self):
        super(TopicWidget, self).click_element(self.KEYWORD_EDIT_BTN)

    def get_hashtag(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.HASHTAG)
        ).text

    def delete_keyword(self):
        super(TopicWidget, self).click_element(self.KEYWORD_DELETE_BTN)

    def click_class(self):
        super(TopicWidget, self).click_element(self.CLASS)

    def get_class_counter(self, active=True):
        return WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.CLASS_COUNTER.format(
                "" if active else "not"
            ))
        ).text

    def open_topic_popup(self):
        super(TopicWidget, self).click_element(self.OPEN_TOPIC_POPUP)


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

    OPEN_TOPIC_POPUP = '//a[contains(@class,"media-text_a")]'
    KEYWORD_ERROR_MIN_LENGTH = '//span[contains(text(), "Минимальная длина")]'
    KEYWORD_ERROR_WRONG_SYMBOLS = '//span[contains(text(), "запрещенные символы")]'
    KEYWORD_ERROR_TOO_MUCH_WORDS = '//span[contains(text(), "слов достаточно")]'

    def open_tags_input(self):
        super(TopicTags, self).click_element(self.ADD_TAGS_BUTTON)

    def set_tag(self, tag):
        super(TopicTags, self).input_text_to_element(self.TAGS_INPUT, tag)
        super(TopicTags, self).input_key(self.TAGS_INPUT, Keys.ENTER)

    def remove_tag(self, tag):
        remove_tag_button = self.REMOVE_TAG_BUTTON_TEMPLATE.format(tag)
        super(TopicTags, self).click_element(remove_tag_button)

    def edit_tag(self):
        super(TopicTags, self).click_element(self.EDIT_TAG)

    def no_one_tags(self):
        return super(TopicTags, self).is_not_exist_element(self.TAG)

    def is_exist_tag(self, tag):
        tag_element = self.TAG_TEMPLATE.format(tag)
        return super(TopicTags, self).is_exist_element(tag_element)

    def no_one_hashtags(self):
        return super(TopicTags, self).is_not_exist_element(self.HASHTAG)

    def is_exist_hashtag(self, hashtag):
        hashtag_element = self.HASHTAG_TEMPLATE.format(hashtag)
        return super(TopicTags, self).is_exist_element(hashtag_element)

    def is_not_exist_hashtag(self, hashtag):
        hashtag_element = self.HASHTAG_TEMPLATE.format(hashtag)
        return super(TopicTags, self).is_not_exist_element(hashtag_element)

    def submit(self):
        super(TopicTags, self).click_element(self.SUBMIT)

    def get_error_text(self):
        return super(TopicTags, self).get_element_text(self.ERROR)

    def get_remaining_tag_length(self):
        remaining_tag_length_str = super(TopicTags, self).get_element_text(self.TAG_LENGTH_COUNTER)
        return int(remaining_tag_length_str)
    #
    # def is_keyword_error_min_length_exist(self):
    #     try:
    #         WebDriverWait(self.driver, 4, 0.1).until(
    #             lambda d: d.find_element_by_xpath(self.KEYWORD_ERROR_MIN_LENGTH)
    #         )
    #     except:
    #         return False
    #     return True
    #
    # def is_keyword_error_wrong_symbols_exist(self):
    #     try:
    #         WebDriverWait(self.driver, 4, 0.1).until(
    #             lambda d: d.find_element_by_xpath(self.KEYWORD_ERROR_WRONG_SYMBOLS)
    #         )
    #     except:
    #         return False
    #     return True
    #
    # def get_count_of_keywords(self, count):
    #     # try:
    #     import time
    #     time.sleep(2)
    #     WebDriverWait(self.driver, 4, 0.1).until(
    #         lambda d: (d.find_element_by_xpath(self.TAG_TEMPLATE))
    #     )
    #     count = self.driver.find_element_by_xpath(self.TAG_TEMPLATE)
    #     print((count))
    #     # except:
    #     #     return 0
    #     return True
    #
    # def is_keyword_error_too_much_words(self):
    #     try:
    #         WebDriverWait(self.driver, 4, 0.1).until(
    #             lambda d: d.find_element_by_xpath(self.KEYWORD_ERROR_TOO_MUCH_WORDS)
    #         )
    #     except:
    #         return False
    #     return True
