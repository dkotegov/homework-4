# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait

from Components.component import Component


class KeywordsComponent(Component):
    ADD_KEYWORD_BTN = '//a[contains(text(),"ключевые слова")]'
    KEYWORD_FIELD = '//input[@name="st.newTag"]'
    SUBMIT_KEYWORD = '//td[contains(@class,"tag-box_button_w")]'
    KEYWORD = '//a[contains(@title,"все темы")]'
    KEYWORD_EDIT_BTN = '//a[contains(@class,"tab-box_edit")]'
    HASHTAG = '//a[contains(@class,"__hashtag")]'
    KEYWORD_DELETE_BTN = '//span[contains(@class,"tag_del")]'
    OPEN_TOPIC_POPUP = '//a[contains(@class,"media-text_a")]'
    KEYWORD_ERROR_MIN_LENGTH = '//span[contains(text(), "Минимальная длина")]'
    KEYWORD_ERROR_WRONG_SYMBOLS = '//span[contains(text(), "запрещенные символы")]'
    KEYWORD_ERROR_TOO_MUCH_WORDS = '//span[contains(text(), "слов достаточно")]'

    KEYWORD_LENGTH_COUNTER = '//span[contains(@class,"txt-counter")]'

    def open_keyword_field(self):
        super(KeywordsComponent, self).click_element(self.ADD_KEYWORD_BTN)

    def set_keyword(self, word="word"):
        super(KeywordsComponent, self).input_text_to_element(self.KEYWORD_FIELD, word)

    def submit_keyword(self):
        super(KeywordsComponent, self).click_element(self.SUBMIT_KEYWORD)

    def get_keyword(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.KEYWORD)
        ).text

    def open_keyword_edit_field(self):
        super(KeywordsComponent, self).click_element(self.KEYWORD_EDIT_BTN)

    def get_hashtag(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.HASHTAG)
        ).text

    def delete_keyword(self):
        super(KeywordsComponent, self).click_element(self.KEYWORD_DELETE_BTN)

    def get_keyword_length_counter_text(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.KEYWORD_LENGTH_COUNTER)
        ).text

    def is_keyword_exists(self):
        try:
            WebDriverWait(self.driver, 4, 0.1).until(
                lambda d: d.find_element_by_xpath(self.KEYWORD)
            )
        except:
            return False
        return True

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
            lambda d: (d.find_element_by_xpath(self.KEYWORD))
        )
        count = self.driver.find_element_by_xpath(self.KEYWORD)
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
