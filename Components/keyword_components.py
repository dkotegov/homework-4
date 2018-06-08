# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait

from Components.component import Component


class TopicTags(Component):
    ADD_TAG = '//a[contains(@href,"AddTopicTag")]'
    EDIT_TAG = '//a[contains(@href,"EditTopicTag")]'
    REMOVE_TAG = '//span[contains(@class,"tag_del")]'
    SUBMIT = '//span[contains(@class,"tag-box_button")]'

    TAG = '//a[contains(@hrefattrs,"_TopicTag")]'
    TAG_INPUT = '//input[@name="st.newTag"]'

    HASHTAG = '//a[contains(@class,"__hashtag")]'
    OPEN_TOPIC_POPUP = '//a[contains(@class,"media-text_a")]'
    KEYWORD_ERROR_MIN_LENGTH = '//span[contains(text(), "Минимальная длина")]'
    KEYWORD_ERROR_WRONG_SYMBOLS = '//span[contains(text(), "запрещенные символы")]'
    KEYWORD_ERROR_TOO_MUCH_WORDS = '//span[contains(text(), "слов достаточно")]'
    KEYWORD_LENGTH_COUNTER = '//span[contains(@class,"txt-counter")]'

    def add_tag(self):
        super(TopicTags, self).click_element(self.ADD_TAG)

    def edit_tag(self):
        super(TopicTags, self).click_element(self.EDIT_TAG)

    def set_tag(self, tag):
        super(TopicTags, self).input_text_to_element(self.TAG_INPUT, tag)

    def get_tag(self):
        return super(TopicTags, self).get_element_text(self.TAG)

    def submit(self):
        super(TopicTags, self).click_element(self.SUBMIT)

    def remove_tag(self):
        super(TopicTags, self).click_element(self.REMOVE_TAG)

    def is_exists_tag(self):
        return super(TopicTags, self).is_exist_element(self.TAG)

    def get_hashtag(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.HASHTAG)
        ).text

    def get_keyword_length_counter_text(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.KEYWORD_LENGTH_COUNTER)
        ).text

    def is_hashtag_exists(self):
        try:
            WebDriverWait(self.driver, 4, 0.1).until(
                lambda d: d.find_element_by_xpath(self.HASHTAG)
            )
        except:
            return False
        return True

    def is_keyword_error_min_length_exist(self):
        try:
            WebDriverWait(self.driver, 4, 0.1).until(
                lambda d: d.find_element_by_xpath(self.KEYWORD_ERROR_MIN_LENGTH)
            )
        except:
            return False
        return True

    def is_keyword_error_wrong_symbols_exist(self):
        try:
            WebDriverWait(self.driver, 4, 0.1).until(
                lambda d: d.find_element_by_xpath(self.KEYWORD_ERROR_WRONG_SYMBOLS)
            )
        except:
            return False
        return True

    # TODO не работает
    def get_count_of_keywords(self, count):
        # try:
        import time
        time.sleep(2)
        WebDriverWait(self.driver, 4, 0.1).until(
            lambda d: (d.find_element_by_xpath(self.TAG))
        )
        count = self.driver.find_element_by_xpath(self.TAG)
        print((count))
        # except:
        #     return 0
        return True

    def is_keyword_error_too_much_words(self):
        try:
            WebDriverWait(self.driver, 4, 0.1).until(
                lambda d: d.find_element_by_xpath(self.KEYWORD_ERROR_TOO_MUCH_WORDS)
            )
        except:
            return False
        return True
