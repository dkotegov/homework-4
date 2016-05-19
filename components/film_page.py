# -*- coding: utf-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException

from components.component import *


def add_value(initial, value):
    return initial + value


def sub_value(initial, value):
    return initial - value


class FilmBlock(Component):
    # login constants
    LOGIN_BUTTON = '//a[contains(text(),"Вход")]'
    LOGOUT_BUTTON = '//a[contains(text(),"выход")]'
    LOGIN_INPUT = '//input[@name="Username"]'
    PASSWORD_INPUT = '//input[@class="b-input b-input_password b-input_"]'
    LOGIN_SUBMIT_BUTTON = '//button[@class="btn btn_stylish btn_main btn_single btn_fluid btn_form btn_ "]'
    TEST_USER_LOGIN = 'valeriy-test'
    TEST_USER_DOMAIN = '@mail.ru'
    TEST_USER_PASSWORD = 'passw0rd'

    # rate_film constants
    RATING_STAR = '//li[@class="voter__stars__item js-rating__star"]'
    RATING = '//span[@class="voter__val__inner js-rating__value"]'

    # add_to_watch_list constants
    ADD_TO_WATCH_LIST_BUTTON = '//div[@class="movieabout__info__button__item js-module"]'
    ADDED_STATE = '//a[@class="button button_full button_watch js-favorite-switch button_active"]'

    # like/dislike review
    LIKE_REVIEW_BUTTON = '//span[@class="review__item__likecount__plus js-rating__star"]'
    DISLIKE_REVIEW_BUTTON = '//span[@class="review__item__likecount__minus js-rating__star"]'
    REVIEW_RATING_ITEM = '//div[@class="review__item__likecount js-rating__container voter__rated"]'
    REVIEW_RATING_VALUE_CLASS = 'js-rating__average-value'

    def click_logout_link(self):
        self.click(self.LOGOUT_LINK)

    def click_signin_link(self):
        self.click(self.SIGNIN_LINK)

    def login(self):
        if self.driver.find_element_by_xpath(self.LOGIN_BUTTON):
            self.click(self.LOGIN_BUTTON)
            self.driver.switch_to.frame(self.driver.find_element_by_class_name("ag-popup__frame__layout__iframe"))
            self.send_keys(self.LOGIN_INPUT, self.TEST_USER_LOGIN)
            self.send_keys(self.PASSWORD_INPUT, self.TEST_USER_PASSWORD)
            self.click(self.LOGIN_SUBMIT_BUTTON)
            self.driver.switch_to.default_content()

    def logout(self):
        if self.driver.find_element_by_xpath(self.LOGOUT_BUTTON):
            self.click(self.LOGOUT_BUTTON)

    def rate_film(self):
        self.click(self.RATING_STAR)
        if self.driver.find_element_by_xpath(self.RATING).text != '0':
            return True
        else:
            return False

    def add_to_watch_list(self):
        self.click(self.ADD_TO_WATCH_LIST_BUTTON)
        try:
            if self.driver.find_element_by_xpath(self.ADDED_STATE):
                return True
        except NoSuchElementException:
            return False

    def rate_review(self, button, action):
        current_rating = self.driver.find_element_by_xpath(self.REVIEW_RATING_ITEM).find_element_by_class_name(
            self.REVIEW_RATING_VALUE_CLASS).text[1:]
        self.click(button)
        time.sleep(3)
        after_rating = self.driver.find_element_by_xpath(self.REVIEW_RATING_ITEM).find_element_by_class_name(
            self.REVIEW_RATING_VALUE_CLASS).text[1:]
        print "Current: " + str(current_rating) + ", After: " + str(after_rating)
        if int(after_rating) == action(int(current_rating), 1) or int(after_rating) == action(int(current_rating), 2):
            return True
        else:
            return False

    def like_review(self):
        return self.rate_review(self.LIKE_REVIEW_BUTTON, add_value)

    def dislike_review(self):
        return self.rate_review(self.DISLIKE_REVIEW_BUTTON, sub_value)
