# -*- coding: utf-8 -*-

from like_tests.elements.component import *


class FriendsFeedButton(Clickable):
    CLICK = '//div[@class="main-feed portlet"]//a[text()[contains(., "Друзья")]]'


class FeedPhoto(Clickable):
    CLICK = '//div[@class="media-block media-photos "]//a'


class OwnPhotoLikeButton(Component):
    BASE_BUTTON = 'button[@class="h-mod widget_cnt controls-list_lk"][@data-type="PHOTO"]'
    ACTIVE = '//div[@class="widget  __active __compact"]/' + BASE_BUTTON
    DISABLED = '//div[@class="widget  __compact"]/' + BASE_BUTTON

    def click_disabled(self):
        Clickable.hard_click(self.driver, self.DISABLED)

    def click_active(self):
        Clickable.hard_click(self.driver, self.ACTIVE)


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
        return int(self.driver.find_element_by_xpath(self.EMPTY).text) == 0

    def non_zero_count(self):
        return int(self.driver.find_element_by_xpath(self.ACTIVE).text)
