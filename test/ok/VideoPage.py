# coding=utf-8
from _ast import Assert

import time
from hamcrest import *
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

from Page import Page


class AnyEc:
    def __init__(self, *args):
        self.ecs = args

    def __call__(self, driver):
        for fn in self.ecs:
            try:
                if fn(driver): return True
            except:
                pass


class VideoPage(Page):
    def __init__(self, driver):
        super(VideoPage, self).__init__(driver, "video_page")

    def assert_advertisement_visible(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "trg-b-iframe")))

    def assert_lev_nav_visible(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "nav-side")))

    def assert_content_vertically_separated(self):
        names = self.driver.find_elements_by_class_name("portlet_h_name_t")
        assert names[0].text == u'Прямой эфир'
        assert names[1].text == u'Каналы'
        assert names[2].text == u'Видео'

    def assert_video_is_showing(self):
        videos = self.driver.find_element_by_id("hook_Block_AltGroupVideoMoviesRedesignBlock")
        video = videos.find_element_by_class_name("video-card")
        video.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "vp_video")))

    def assert_video_is_closeable(self):
        videos = self.driver.find_element_by_id("hook_Block_AltGroupVideoMoviesRedesignBlock")
        video = videos.find_element_by_class_name("video-card")
        video.click()
        self.wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "media-layer_close_ico")))
        cross = self.driver.find_element_by_class_name("media-layer_close_ico")
        cross.click()
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "vp_video")))

    def assert_video_is_turnable(self):
        videos = self.driver.find_element_by_id("hook_Block_AltGroupVideoMoviesRedesignBlock")
        video = videos.find_element_by_class_name("video-card")
        video.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "media-layer_turn_ico")))
        line = self.driver.find_element_by_class_name("media-layer_turn_ico")
        line.click()
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "vp_video")))
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "vp-modal_video")))

    def assert_video_is_turnable_and_closeable(self):
        self.assert_video_is_turnable()
        cross = self.driver.find_element_by_class_name("js-modal-close")
        cross.click()
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "vp_modal")))
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "vp_video")))

    def assert_chanel_videos(self):
        chanels = self.driver.find_element_by_id("hook_Block_AltGroupVideoTypeFilterAlbumsBlock")
        chanel = chanels.find_element_by_class_name("nav-side_i")
        chanel_name = chanel.text
        chanel.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "channel-panel_n")))
        chanel_panel_name = self.driver.find_element_by_class_name("channel-panel_n").text
        assert chanel_panel_name == chanel_name
        self.wait.until(
            EC.visibility_of_all_elements_located((By.ID, "hook_Loader_AltGroupVideoMoviesPagingBlockLoader")))

    def assert_subscription_is_ok(self):
        self.assert_chanel_videos()
        self.wait.until(
            AnyEc(
                EC.visibility_of_any_elements_located((By.CLASS_NAME, "js-action-subscribe")),
                EC.visibility_of_any_elements_located((By.CLASS_NAME, "js-action-unsubscribe")),
            ))
        subscribe_btn = self.driver.find_element_by_class_name("js-action-subscribe")
        unsubscribe_btn = self.driver.find_element_by_class_name("js-action-unsubscribe")

        if unsubscribe_btn.is_displayed():
            unsubscribe_btn.click()

        self.wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "js-action-subscribe")))
        subscribe_btn.click()
        self.wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "js-action-unsubscribe")))
        unsubscribe_btn.click()
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "ic_ok")))

    def assert_klass_increase(self):
        self.assert_video_is_showing()
        self.wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "controls-list_lk")))
        klass_container = self.driver.find_element_by_class_name("controls-list_lk")
        klass_count = int(klass_container.find_element_by_class_name("widget_count").text)
        klass_container.click()
        # time.sleep(2)
        # new_klass_count = int(self.driver.find_element_by_class_name("widget_count").text)
        # assert klass_count < new_klass_count
