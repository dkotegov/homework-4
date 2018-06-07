# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Components.component import Component


class TopicCreationPopup(Component):
    CREATE_TOPIC = '//a[contains(@data-l, "OpenPostingPopup")]'
    TOPIC_TEXT = '//div[@data-module="postingForm/mediaText"]'
    SUBMIT = '//div[@data-action="submit"]'
    ADD_PHOTO_BTN = '//div[@data-module="postingForm/mediaPhotosAddButton"]'
    ADD_PHOTO_FROM_COMPUTER_BTN = '//a[contains(@class, "__photo-full")]'

    def open_popup(self):
        super(TopicCreationPopup, self).click_element(self.CREATE_TOPIC)

    def set_text(self, text="Default text"):
        super(TopicCreationPopup, self).input_text_to_element(self.TOPIC_TEXT, text)

    def submit(self):
        super(TopicCreationPopup, self).click_element(self.SUBMIT)

    def clear_edit_field(self):
        WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.TOPIC_TEXT)
        ).clear()

    def add_photo(self):
        super(TopicCreationPopup, self).click_element(self.ADD_PHOTO_BTN)

    def add_photo_from_computer(self):
        super(TopicCreationPopup, self).click_element(self.ADD_PHOTO_FROM_COMPUTER_BTN)


class TopicPopup(Component):
    TOPIC_TEXT = '//div[contains(@class,"media-text __full")]/div'
    COMMENT_FIELD = '//div[contains(@class,"js-comments_add")]'
    CLOSE = '//div[contains(@class,"media-layer_close_ico")]'
    SUBMIT_COMMENT_BTN = '//button[contains(@class,"form-actions_yes")]'
    COMMENT_COUNTER = '//div[contains(@class,"mlr_cnts js-video-scope")]' \
                      '//a[@data-module = "CommentWidgets"]' \
                      '/span[contains(@class,"widget_count") and {}(contains(@class,"__empty"))]'
    COMMENT_TEXT = '//div[contains(@class, "comments_text")]/div'
    COMMENT_AUTHOR = '//div[@class = "comments_author"]/span/a'
    REMOVE_COMMENT_BTN = '//a[contains(@class, "comments_remove")]'
    REMOVE_COMMENT_INFO = '//span[contains(@class, "delete-stub_info")]'
    RECOVER_COMMENT_BTN = '//a[contains(@class, "delete-stub_cancel")]'
    EDIT_COMMENT_BTN = '//a[contains(@class, "comments_edit")]'
    EDIT_COMMENT_SAVE_BTN = '//button[contains(@class,"comments_add-controls_save")]'

    RIGHT_MENU = '//div[@class="mlr_top_ac"]' \
                 '/div[@data-module="ShortcutMenu"]/div/div[contains(@class,"sc-menu")]'
    REMOVE_TOPIC_BTN = '//a[contains(@href, "Topic_Remove")]'
    REMOVE_TOPIC_INFO = '//span[contains(@class, "delete-stub_info")]'
    EDIT_TOPIC_BTN = '//a[contains(@href, "Topic_Edit")]'

    def get_topic_text(self):
        return super(TopicPopup, self).get_element_text(self.TOPIC_TEXT)

    def close_topic_popup(self):
        super(TopicPopup, self).click_element(self.CLOSE)

    def set_comment(self, comment="comment"):
        super(TopicPopup, self).input_text_to_element(self.COMMENT_FIELD, comment)

    def clear_comment_field(self):
        WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.COMMENT_FIELD)
        ).clear()

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

    def get_comment_author(self):
        return super(TopicPopup, self).get_element_text(self.COMMENT_AUTHOR)

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

    def open_right_menu(self):
        right_menu = WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.RIGHT_MENU)
        )
        self.driver.execute_script("arguments[0].classList.remove('sc-menu__hidden');", right_menu)

    def remove_topic(self):
        super(TopicPopup, self).click_element(self.REMOVE_TOPIC_BTN)

    def edit_topic(self):
        super(TopicPopup, self).click_element(self.EDIT_TOPIC_BTN)

    def remove_topic_info(self):
        return super(TopicPopup, self).get_element_text(self.REMOVE_TOPIC_INFO)

    def clear_edit_field(self):
        WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.THEME_TEXT)
        ).clear()


class TopicListElement(Component):
    TOPIC_TEXT = '//div[contains(@class,"media-text_cnt_tx")]'
    TOPIC_OWNER = '//span[@class="shortcut-wrap"]/a[contains(@hrefattrs,"GroupTopicLayer_VisitProfile")]'

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
        return super(TopicListElement, self).get_element_text(self.TOPIC_TEXT)

    def get_topic_owner(self):
        return super(TopicListElement, self).get_element_text(self.TOPIC_OWNER)

    def open_keyword_field(self):
        super(TopicListElement, self).click_element(self.ADD_KEYWORD_BTN)

    def set_keyword(self, word="word"):
        super(TopicListElement, self).input_text_to_element(self.KEYWORD_FIELD, word)

    def submit_keyword(self):
        super(TopicListElement, self).click_element(self.SUBMIT_KEYWORD)

    def get_keyword(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.KEYWORD)
        ).text

    def open_keyword_edit_field(self):
        super(TopicListElement, self).click_element(self.KEYWORD_EDIT_BTN)

    def get_hashtag(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.HASHTAG)
        ).text

    def delete_keyword(self):
        super(TopicListElement, self).click_element(self.KEYWORD_DELETE_BTN)

        # LIKE

    def click_class(self):
        super(TopicListElement, self).click_element(self.CLASS)

    def get_class_counter(self, active=True):
        return WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element_by_xpath(self.CLASS_COUNTER.format(
                "" if active else "not"
            ))
        ).text

    def open_topic_popup(self):
        super(TopicListElement, self).click_element(self.OPEN_TOPIC_POPUP)


class NotifyPanel(Component):
    MESSAGE = '//div[@id = "notifyPanel_msg"]'
    CLOSE_BTN = '//input[@name = "button_close"]'

    def get_message(self):
        return super(NotifyPanel, self).get_element_text(self.MESSAGE)

    def close_panel(self):
        super(NotifyPanel, self).click_element(self.CLOSE_BTN)
