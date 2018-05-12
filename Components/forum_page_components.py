# -*- coding: utf-8 -*-
from Components.component import Component
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TopicPopup(Component):
    CREATE_THEME = '//a[contains(@data-l, "OpenPostingPopup")]'
    THEME_TEXT = '//div[@data-module="postingForm/mediaText"]'
    SUBMIT = '//div[@data-action="submit"]'

    def open_popup(self):
        super(TopicPopup, self).click_element(self.CREATE_THEME)

    def set_text(self, text="Default text"):
        super(TopicPopup, self).input_text_to_element(self.THEME_TEXT, text)

    def submit(self):
        super(TopicPopup, self).click_element(self.SUBMIT)

class TopicList(Component):
    ADD_KEYWORD_BTN = '//a[contains(text(),"ключевые слова")]'
    KEYWORD_FIELD = '//input[@name="st.newTag"]'
    SUBMIT_KEYWORD = '//td[contains(@class,"tag-box_button_w")]'
    KEYWORD = '//a[contains(@title,"все темы")]'
    KEYWORD_EDIT_BTN = '//a[contains(@class,"tab-box_edit")]'
    HASHTAG = '//a[contains(@class,"__hashtag")]'
    KEYWORD_DELETE_BTN = '//span[contains(@class,"tag_del")]'

    CLASS = '//span[contains(@class,"controls-list_lk")]'
    CLASS_COUNTER_ACTIVE = '//span[contains(@class,"controls-list_lk")]/' \
                    'span[contains(@class,"widget_count") and {}(contains(@class,"__react-like"))]'

    def open_keyword_field(self):
        super(TopicList, self).click_element(self.ADD_KEYWORD_BTN)

    def set_keyword(self, word="word"):
        super(TopicList, self).input_text_to_element(self.KEYWORD_FIELD, word)

    def submit_keyword(self):
        super(TopicList, self).click_element(self.SUBMIT_KEYWORD)

    def get_keyword(self):
        return WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.KEYWORD)
        ).text

    def open_keyword_edit_field(self):
        super(TopicList, self).click_element(self.KEYWORD_EDIT_BTN)

    def get_hashtag(self):
        return WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.HASHTAG)
        ).text

    def delete_keyword(self):
        super(TopicList, self).click_element(self.KEYWORD_DELETE_BTN)

        # LIKE
    def click_class(self):
        super(TopicList, self).click_element(self.CLASS)

    def get_class_counter(self, active=True):
        return WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.CLASS_COUNTER_ACTIVE.format(
                "" if active else "not"
            ))
        ).text
