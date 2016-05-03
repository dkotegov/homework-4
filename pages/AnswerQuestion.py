# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.Common import Page, Element


class OtvetPageQuestion(Page):
    QUESTION_CLASS = "question"
    LIKES_CLASS = "action--mark"
    DISLIKES_CLASS = "action--unmark"
    SUBSCRIBE_XPATH = "//button[@title='Подписаться']"
    UNSUBSCRIBE_XPATH = "//button[@title='Отписаться']"

    def like(self):
        self.driver.find_element_by_class_name(self.QUESTION_CLASS).find_element_by_class_name(self.LIKES_CLASS).click()
        WebDriverWait(self.driver, 10)\
            .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, self.DISLIKES_CLASS)))


    def dislike(self):
        self.driver.find_element_by_class_name(self.QUESTION_CLASS).find_element_by_class_name(self.DISLIKES_CLASS).click()
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.presence_of_element_located((By.CLASS_NAME, self.LIKES_CLASS)))

    def is_liked(self):
        return self.driver.find_element_by_class_name(self.QUESTION_CLASS).find_element_by_class_name(self.DISLIKES_CLASS) is not None

    def is_unliked(self):
        return self.driver.find_element_by_class_name(self.QUESTION_CLASS).find_element_by_class_name(self.LIKES_CLASS) is not None

    def subscribe(self):
        self.driver.find_element_by_xpath(self.SUBSCRIBE_XPATH).click()
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, self.UNSUBSCRIBE_XPATH)))

    def unsubscribe(self):
        self.driver.find_element_by_xpath(self.UNSUBSCRIBE_XPATH).click()
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, self.SUBSCRIBE_XPATH)))

    def is_subscribed(self):
        return self.driver.find_element_by_xpath(self.UNSUBSCRIBE_XPATH) is not None

    def is_unsubscribed(self):
        return self.driver.find_element_by_xpath(self.SUBSCRIBE_XPATH) is not None

    def answer_form(self):
        return AnswerForm(self.driver)


class AnswerForm(Element):
    FORM_CLASS = "form-form"
    TEXT_AREA_CLASS = "form--text"
    IMAGE_ADD_CLASS = "action--upload-photo"
    SUBMIT_CLASS = "action--save"
    COUNT_SYMBOLS_CLASS = "count-symbol-number"
    MAX_SYMBOLS = 3800

    def __init__(self, driver):
        super(AnswerForm, self).__init__(driver)
        self.form = self.driver.find_element_by_class_name(self.FORM_CLASS)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.form)
        actions.perform()

    def set_text(self, text):
        self.form.find_element_by_class_name(self.TEXT_AREA_CLASS).send_keys(text)

    def submit(self):
        el = self.form.find_element_by_class_name(self.SUBMIT_CLASS)
        actions = ActionChains(self.driver)
        actions.move_to_element(el)
        actions.click(el)
        actions.perform()

    def count_symbols_value(self):
        return self.form.find_element_by_class_name(self.COUNT_SYMBOLS_CLASS).text