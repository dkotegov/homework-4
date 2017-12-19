# coding=utf-8
from _ast import Assert

import time
import random
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

from test.ok.Page import Page


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

    def assert_left_menu_items_visible(self):
        leftMenu = self.driver.find_element_by_id("layer_left_cnt_scroll")
        items = leftMenu.find_elements_by_class_name("mml_cat_li")
        assert len(items) == 8
        assert items[0].find_elements_by_class_name("mml_cat_n")[0].text == u'Топ недели'
        assert items[1].find_elements_by_class_name("mml_cat_n")[0].text == u'OK Live'
        assert items[2].find_elements_by_class_name("mml_cat_n")[0].text == u'Популярное'
        assert items[3].find_elements_by_class_name("mml_cat_n")[0].text == u'Новинки'
        assert items[4].find_elements_by_class_name("mml_cat_n")[0].text == u'Прямой эфир'
        assert items[5].find_elements_by_class_name("mml_cat_n")[0].text == u'Каталог'
        assert items[6].find_elements_by_class_name("mml_cat_n")[0].text == u'Моё видео'
        assert items[7].find_elements_by_class_name("mml_cat_n")[0].text == u'Мои подписки'

    def assert_video_load_dialog_visible(self):
        uplBtn = self.driver.find_element_by_class_name("vl_btn")
        uplBtn.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.ID, "hook_Block_VideoVitrinaPopupUploader")))

    def assert_video_open(self):
        videos = self.driver.find_elements_by_class_name("vid-card_img")
        video = random.choice(videos)
        video.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "html5-vpl_vid_display")))

    def assert_comments_under_video_visible(self):
        videos = self.driver.find_elements_by_class_name("vid-card_img")
        video = random.choice(videos)
        video.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "comments_lst_cnt")))

    def assert_video_info_viewers_visible(self):
        videos = self.driver.find_elements_by_class_name("vid-card_img")
        video = random.choice(videos)
        video.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "vp-layer-info_views")))

    def assert_video_suggested_exist(self):
        videos = self.driver.find_elements_by_class_name("vid-card_img")
        video = random.choice(videos)
        video.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.ID, "vp_rel_list")))

    def assert_video_is_closeable(self):
        videos = self.driver.find_elements_by_class_name("vid-card_img")
        video = random.choice(videos)
        video.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "html5-vpl_vid_display")))
        closeBtn = self.driver.find_element_by_css_selector("#vpl_close > div")
        closeBtn.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.ID, "hook_Block_VideoVitrinaContent")))

    def assert_live_open(self):
        openLiveBtn = self.driver.find_element_by_xpath("// *[ @ id = 'vv_btn_liveApp'] / span / span[2]")
        openLiveBtn.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "vl_ic-head__liveApp")))
        videos = self.driver.find_elements_by_class_name("vid-card_img")
        video = random.choice(videos)
        video.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "html5-vpl_vid_display")))

    def assert_live_closable(self):
        openLiveBtn = self.driver.find_element_by_xpath("// *[ @ id = 'vv_btn_liveApp'] / span / span[2]")
        openLiveBtn.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "vl_ic-head__liveApp")))
        videos = self.driver.find_elements_by_class_name("vid-card_img")
        video = random.choice(videos)
        video.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "html5-vpl_vid_display")))
        closeBtn = self.driver.find_element_by_css_selector("#vpl_close > div")
        closeBtn.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.ID, "hook_Block_VideoVitrinaContent")))

    def assert_subscribes_open(self):
        openSubsBtn = self.driver.find_element_by_xpath("//*[@id='vv_btn_subscriptions']/span/span[2]")
        openSubsBtn.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.ID, "hook_Block_VideoVitrinaContent")))
