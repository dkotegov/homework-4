# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class SendPanel(BaseElement):
    MESSAGE_INPUT = (By.XPATH, "//div[@name='st.txt']")
    SEND_BUTTON = (By.XPATH, "//button[@class='button-pro comments_add-controls_save']")
