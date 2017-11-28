# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class CallWindow(BaseElement):
    MODAL = (By.CSS_SELECTOR, ".video-chat_view.video-chat_view-remote")
    HANG_UP_BUTTON = (By.CSS_SELECTOR, ".video-chat_btn.__hangup")
    RECALL_BUTTON = (By.CSS_SELECTOR, ".video-chat_btn_ic.vc_ic32_recall-w")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".video-chat_ac_ic.vc_ic vc_ic_close")
    MIC_ON_BUTTON = (By.CSS_SELECTOR,
                     "#hook_Block_VideoChatCall > div > div.video-chat_cnt > div.video-chat_controls > div.video-chat_btn.__camera-on > div")
    MIC_OFF_BUTTON = (By.CSS_SELECTOR,
                      "#hook_Block_VideoChatCall > div > div.video-chat_cnt > div.video-chat_controls > div.video-chat_btn.__camera-off > div")
    CAM_ON_BUTTON = (By.CSS_SELECTOR,
                     "#hook_Block_VideoChatCall > div > div.video-chat_cnt > div.video-chat_controls > div.video-chat_btn.__mic-off > div")
    CAM_OFF_BUTTON = (By.CSS_SELECTOR,
                      "#hook_Block_VideoChatCall > div > div.video-chat_cnt > div.video-chat_controls > div.video-chat_btn.__mic-on > div")
