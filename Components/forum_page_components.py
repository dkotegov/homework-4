# -*- coding: utf-8 -*-
from Components.component import Component
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TopicCreationPopup(Component):
    CREATE_THEME = '//a[contains(@data-l, "OpenPostingPopup")]'
    THEME_TEXT = '//div[@data-module="postingForm/mediaText"]'
    SUBMIT = '//div[@data-action="submit"]'

    def open_popup(self):
        super(TopicCreationPopup, self).click_element(self.CREATE_THEME)

    def set_text(self, text="Default text"):
        super(TopicCreationPopup, self).input_text_to_element(self.THEME_TEXT, text)

    def submit(self):
        super(TopicCreationPopup, self).click_element(self.SUBMIT)



class TopicPopup(Component):
    COMMENT_FIELD = '//div[contains(@class,"js-comments_add")]'
    CLOSE = '//div[contains(@class,"media-layer_close_ico")]'
    SUBMIT_COMMENT_BTN = '//button[contains(@class,"form-actions_yes")]'
    COMMENT_COUNTER = '//div[contains(@class,"mlr_cnts js-video-scope")]' \
                      '//a[@data-module = "CommentWidgets"]' \
                      '/span[contains(@class,"widget_count") and {}(contains(@class,"__empty"))]'
    COMMENT_TEXT = '//div[contains(@class, "comments_text")]/div'
    REMOVE_COMMENT_BTN = '//a[contains(@class, "comments_remove")]'
    REMOVE_COMMENT_INFO = '//span[contains(@class, "delete-stub_info")]'
    RECOVER_COMMENT_BTN = '//a[contains(@class, "delete-stub_cancel")]'
    EDIT_COMMENT_BTN = '//a[contains(@class, "comments_edit")]'
    EDIT_COMMENT_SAVE_BTN = '//button[contains(@class,"comments_add-controls_save")]'

    def close_topic_popup(self):
        super(TopicPopup, self).click_element(self.CLOSE)

    def set_comment(self, comment="comment"):
        super(TopicPopup, self).input_text_to_element(self.COMMENT_FIELD, comment)

    def submit_comment(self):
        super(TopicPopup, self).click_element(self.SUBMIT_COMMENT_BTN)

    def get_comment_counter(self, empty=False):
        return WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.COMMENT_COUNTER.format(
                "" if empty else "not"
            ))
        ).text

    def get_comment_text(self):
        return super(TopicPopup, self).get_element_text(self.COMMENT_TEXT)

    def remove_comment(self):
        remove_btn = WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.REMOVE_COMMENT_BTN)
        )
        self.driver.execute_script("arguments[0].classList.remove('fade-on-hover');", remove_btn)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of(remove_btn)
        ).click()

    def open_edit_comment_field(self):
        edit_btn = WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.EDIT_COMMENT_BTN)
        )
        self.driver.execute_script("arguments[0].classList.remove('fade-on-hover');", edit_btn)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of(edit_btn)
        ).click()

    def submit_edit_coment(self):
        super(TopicPopup, self).click_element(self.EDIT_COMMENT_SAVE_BTN)

    def remove_comment_info(self):
        return super(TopicPopup, self).get_element_text(self.REMOVE_COMMENT_INFO)

    def recover_comment(self):
        super(TopicPopup, self).click_element(self.RECOVER_COMMENT_BTN)


class TopicList(Component):
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
            lambda d: d.find_element_by_xpath(self.CLASS_COUNTER.format(
                "" if active else "not"
            ))
        ).text

    def open_topic_popup(self):
        super(TopicList, self).click_element(self.OPEN_TOPIC_POPUP)
