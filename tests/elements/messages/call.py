# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class CallWindow(BaseElement):
    MODAL = (By.CSS_SELECTOR, ".video-chat_view.video-chat_view-remote")
    HANG_UP_BUTTON = (By.CSS_SELECTOR, ".video-chat_btn.__hangup")
    RECALL_BUTTON = (By.CSS_SELECTOR, ".video-chat_btn_ic.vc_ic32_recall-w")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".video-chat_ac_ic.vc_ic vc_ic_close")
    MIC_ON_BUTTON = (By.CSS_SELECTOR, ".vc_ic32_mic-on")
    MIC_OFF_BUTTON = (By.CSS_SELECTOR, ".vc_ic32_mic-off")
    CAM_ON_BUTTON = (By.CSS_SELECTOR, ".vc_ic32_camera-on")
    CAM_OFF_BUTTON = (By.CSS_SELECTOR, ".vc_ic32_camera-off")
    HELP_BUTTON = (By.CSS_SELECTOR, "a.video-chat_ac_ic")
    HELP_CLOSE_BUTTON = (By.CSS_SELECTOR, "input.form-actions_yes")
