# -*- coding: utf-8 -*-

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from like_tests.elements.component import *


class FriendsFeedButton(Clickable):
    CLICK = '//div[@class="main-feed portlet"]//a[text()[contains(., "Друзья")]]'


class FeedPhotoLikeButtonBig(Clickable):
    CLICK = '//a[@class="photo-layer_klass_link"]'


class FeedPhotoIcon(Clickable):
    CLICK = '//div[@class="media-block media-photos "]//a'


class OwnPhotoLikeButton(Component):
    BASE_BUTTON = 'button[@class="h-mod widget_cnt controls-list_lk"][@data-type="PHOTO"]'
    ACTIVE = '//div[@class="widget  __active __compact"]/' + BASE_BUTTON
    DISABLED = '//div[@class="widget  __compact"]/' + BASE_BUTTON

    def click_disabled(self, wait_for_completion=False):
        Clickable.hard_click(self.driver, self.DISABLED)
        if wait_for_completion:
            self.driver.find_element_by_xpath(self.ACTIVE)

    def click_active(self, wait_for_completion=False):
        Clickable.hard_click(self.driver, self.ACTIVE)
        if wait_for_completion:
            self.driver.find_element_by_xpath(self.DISABLED)


class FeedPhotoLikeButton(OwnPhotoLikeButton):
    BASE_BUTTON = OwnPhotoLikeButton.BASE_BUTTON
    ACTIVE = '//div[@class="widget  __active"]/' + BASE_BUTTON
    DISABLED = '//div[@class="widget"]/' + BASE_BUTTON


class PhotoLikeCounter(Component):
    def __init__(self, driver, active_button, disabled_button):
        super(PhotoLikeCounter, self).__init__(driver)
        self.ACTIVE = active_button + '/span[@class="widget_count js-count"]'
        self.EMPTY = disabled_button + '/span[@class="widget_count js-count __empty"]'

    def is_empty(self):
        return int(self.driver.find_element_by_xpath(self.EMPTY).get_attribute("innerText")) == 0

    def non_zero_count(self):
        return int(self.driver.find_element_by_xpath(self.ACTIVE).get_attribute("innerText"))


class GiftLikeButton(OwnPhotoLikeButton):
    BASE_BUTTON = 'button[@class="h-mod widget_cnt controls-list_lk"][@data-type="PRESENT"]'
    ACTIVE = '//div[@class="widget  __active __compact"]/' + BASE_BUTTON
    DISABLED = '//div[@class="widget  __compact"]/' + BASE_BUTTON

    def click_disabled(self, wait_for_completion=False):
        self.driver.find_element_by_xpath(self.DISABLED).click()
        if wait_for_completion:
            self.driver.find_element_by_xpath(self.ACTIVE)

    def click_active(self, wait_for_completion=False):
        self.driver.find_element_by_xpath(self.ACTIVE).click()
        if wait_for_completion:
            self.driver.find_element_by_xpath(self.DISABLED)


class GiftLikeCounter(PhotoLikeCounter):
    ACTIVE = GiftLikeButton.ACTIVE + '/span[@class="widget_count js-count"]'
    EMPTY = GiftLikeButton.DISABLED + '/span[@class="widget_count js-count __empty"]'

    def __init__(self, driver):
        super(GiftLikeCounter, self).__init__(driver, GiftLikeButton.ACTIVE, GiftLikeButton.DISABLED)

    def is_empty(self):
        return self.driver.find_element_by_xpath(self.EMPTY)



