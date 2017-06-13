# -*- coding: utf-8 -*-

import os
from Component import Component
from selenium.webdriver.support.ui import WebDriverWait


def wait_ajax(driver):
    WebDriverWait(driver, 30, 0.1).until(
        lambda d: d.execute_script('return jQuery.active == 0')
    )

class MessageForm(Component):
    NEW_MESSAGE_TEXT = '//textarea[@class="messages__msg-text markitup-editor markItUpEditor"]'
    SEND_BUTTON = '//button[contains(text(),"Отправить")]'
    LAST_MESSAGE_TEXT = '(//ul[@class="messages__feed"]/li[last()]/div/div)[text()]'
    LAST_MESSAGE_TIME = '(//ul[@class="messages__feed"]/li[last()])/span'
    DIALOGS = '//div[@class="breadcrumbs__item"]/a[@href="/talk/"]'
    FRIEND_PAGE = '(//div[@class="breadcrumbs__item"])[last()]/a'
    IMG = '//li[@class="markItUpButton markItUpButton12 editor-picture"]/a'
    IMG_WINDOW = '//div[@class="modal modal-image-upload jqm-init"]'
    CLOSE_IMG_WINDOW = '//*[@id="window_upload_img"]/header/a'
    CANCEL_ADD_IMG = '(//div[@class="modal-content"]/form//button[@class="button jqmClose"])[2]'
    DOWNLOAD_IMG = '//*[@id="submit-image-upload"]'
    ERROR = '//*[@id="block_upload_img_content_pc"]/p[1]'
    CHOOSE_IMG = '//*[@id="img_file"]'



    def set_message_text(self, new_message_text):
        message = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NEW_MESSAGE_TEXT)
        )
        message.send_keys(new_message_text)

    def message_send(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SEND_BUTTON)
        )
        button.click()
        wait_ajax(self.driver)

    def get_last_message_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LAST_MESSAGE_TEXT).text.lstrip()
        )

    def get_textarea_value(self):
        text = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NEW_MESSAGE_TEXT)
        )
        self.set_cursor()
        return text.get_attribute("value")


    def set_cursor(self):
        cursor = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NEW_MESSAGE_TEXT)
        )
        cursor.send_keys()



    def back_to_dialogs(self):
        link = WebDriverWait(self.driver, 60, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DIALOGS)
        )
        link.click()

    def go_to_friend_page(self):
        link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FRIEND_PAGE)
        )
        link.click()

    def friend_name(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FRIEND_PAGE).get_attribute("textContent")
        )

    def get_last_message_time(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LAST_MESSAGE_TIME).get_attribute("textContent")
        )

    def open_img_window(self):
        link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.IMG)
        )
        link.click()

    def close_img_window(self):
        link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CLOSE_IMG_WINDOW)
        )
        link.click()

    def display_img_window(self):
        return self.driver.find_element_by_xpath(self.IMG_WINDOW).is_displayed()


    def cancel_add_img(self):
        link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CANCEL_ADD_IMG)
        )
        link.click()

    def download_img(self):
        link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DOWNLOAD_IMG)
        )
        link.click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ERROR).get_attribute("textContent")
        )

    def choose_img_button(self):
        link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHOOSE_IMG)
        )
        link.click()

    def choose_img(self, path):
        file = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHOOSE_IMG)
        )
        file.send_keys(os.getcwd() + path)
