# -*- coding: utf-8 -*-

from like_tests.elements.component import *


class FriendsFeedButton(Clickable):
    CLICK = '//div[@class="main-feed portlet"]//a[text()[contains(., "Друзья")]]'


class FeedPhoto(Clickable):
    CLICK = '//div[@class="media-block media-photos "]//a'


class PhotoLikeButton(Component):
    BASE_BUTTON = 'button[@class="h-mod widget_cnt controls-list_lk"][@data-type="PHOTO"]'
    ACTIVE = '//div[@class="widget  __active __compact"]/' + BASE_BUTTON
    DISABLED = '//div[@class="widget  __compact"]/' + BASE_BUTTON

    def click_disabled(self):
        self.driver.execute_script('arguments[0].click();', self.driver.find_element_by_xpath(self.DISABLED))

    def click_active(self):
        self.driver.execute_script('arguments[0].click();', self.driver.find_element_by_xpath(self.ACTIVE))

class PhotoLikeCounter(Component):
    ACTIVE = PhotoLikeButton.ACTIVE + '/span[@class="widget_count js-count"]'
    EMPTY = PhotoLikeButton.DISABLED + '/span[@class="widget_count js-count __empty"]'

    def is_empty(self):
        return int(self.driver.find_element_by_xpath(self.EMPTY).text) == 0

    def non_zero_count(self):
        return int(self.driver.find_element_by_xpath(self.ACTIVE).text)
