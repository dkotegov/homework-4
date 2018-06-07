# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait

from Components.component import Component


class TopicPopup(Component):
    CREATE_TOPIC = '//a[contains(@data-l, "OpenPostingPopup")]'
    TOPIC_TEXT = '//div[@data-module="postingForm/mediaText"]'
    SUBMIT = '//div[@data-action="submit"]'

    def open(self):
        super(TopicPopup, self).click_element(self.CREATE_TOPIC)

    def set_text(self, text):
        super(TopicPopup, self).input_text_to_element(self.TOPIC_TEXT, text)

    def submit(self):
        super(TopicPopup, self).click_element(self.SUBMIT)


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
