# -*- coding: utf-8 -*-

from components.component import Component


class FilmBlock(Component):
    # login constants
    LOGIN_BUTTON = '//a[contains(text(),"Вход")]'
    LOGOUT_BUTTON = '//a[contains(text(),"выход")]'
    LOGIN_INPUT = '//input[@name="Username"]'
    PASSWORD_INPUT = '//input[@class="b-input b-input_password b-input_"]'
    LOGIN_SUBMIT_BUTTON = '//button[@class="btn btn_stylish btn_main btn_single btn_fluid btn_form btn_ "]'
    TEST_USER_LOGIN = 'valeriy-test'
    TEST_USER_DOMAIN = '@mail.ru'

    # rate_film constants
    RATING_STAR = '//a[@data="4"]'
    RATING = '//span[@class="voter__val__inner js-rating__value"]'

    # add_to_watch_list constants
    ADD_TO_WATCH_LIST_BUTTON = '//div[@class="button__text" and contains(text(), "Хочу посмотреть")]'
    ADDED_STATE_CLASS = "button button_full button_watch js-favorite-switch button_active"
    ADD_BUTTON_PARENT = '//div[@class="movieabout__info__button__item js-module"]'

    # like/dislike review
    LIKE_REVIEW_BUTTON = '//span[@class="review__item__likecount__plus js-rating__star voter__stars__item__cur"]'
    AFTER_LIKE_REVIEW_BUTTON = '//span[@class="review__item__likecount__plus js-rating__star voter__stars__item__cur"]'
    DISLIKE_REVIEW_BUTTON = '//span[@class="review__item__likecount__minus js-rating__star"]'
    REVIEW_RATING_ITEM = '//div[@class="review__item__likecount js-rating__container voter__rated"]'
    REVIEW_RATING_VALUE_CLASS = 'js-rating__average-value'

    def click_logout_link(self):
        self.click(self.LOGOUT_LINK)

    def click_signin_link(self):
        self.click(self.SIGNIN_LINK)

    def login(self):
        self.click(self.LOGIN_BUTTON)
        self.driver.switch_to.frame(self.driver.find_element_by_class_name("ag-popup__frame__layout__iframe"))
        self.send_keys(self.LOGIN_INPUT, self.TEST_USER_LOGIN)
        self.send_keys(self.PASSWORD_INPUT, self.TEST_USER_PASSWORD)
        self.click(self.LOGIN_SUBMIT_BUTTON)
        self.driver.switch_to.default_content()

    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    def rate_film(self):
        self.click(self.RATING_STAR)
        return self.driver.find_element_by_xpath(self.RATING).text == '0'

    def add_to_watch_list(self):
        self.click(self.ADD_TO_WATCH_LIST_BUTTON)
        element = self.driver.find_element_by_xpath(self.ADD_BUTTON_PARENT).find_elements_by_css_selector("*")[0]
        return element.get_attribute('class') == self.ADDED_STATE_CLASS

    def rate_review(self, button, action):
        current_rating = self.driver.find_element_by_xpath(self.REVIEW_RATING_ITEM).find_element_by_class_name(
                self.REVIEW_RATING_VALUE_CLASS).text[1:]
        self.click(button)
        self.driver.refresh()
        after_rating = self.driver.find_element_by_xpath(self.REVIEW_RATING_ITEM).find_element_by_class_name(
                self.REVIEW_RATING_VALUE_CLASS).text[1:]
        return int(after_rating) == action(int(current_rating), 1) or int(after_rating) == action(int(current_rating),
                                                                                                  2)

    def like_review(self):
        current_rating = self.driver.find_element_by_xpath(self.REVIEW_RATING_ITEM).find_element_by_class_name(
                self.REVIEW_RATING_VALUE_CLASS).text[1:]
        self.click(self.DISLIKE_REVIEW_BUTTON)
        after_rating = self.driver.find_element_by_xpath(self.REVIEW_RATING_ITEM).find_element_by_class_name(
                self.REVIEW_RATING_VALUE_CLASS).text[1:]
        return current_rating == after_rating


