# -*- coding: utf-8 -*-

import os

import urlparse

from selenium.webdriver.support.ui import WebDriverWait

class Page(object):
    BASE_URL = 'http://ftest.tech-mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход для участников"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class TopMenu(Component):
    USERNAME = '//a[@class="username"]'

    def get_username(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
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

class DialogForm(Component):
    DIALOGS_AVATAR = '(//img[@class="talk__user-image"])[1]'

    def get_dialogs_avatar_src(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DIALOGS_AVATAR).get_attribute("src")
        )

    def go_to_user_page(self):
        link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DIALOGS_AVATAR)
        )
        link.click()


class UserForm(Component):
    USERNAME = '//h1[@class="profile__full-name"]'
    AVATAR = '//img[@class="profile__photo"]'

    def user_name(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )

    def get_avatar_src(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AVATAR).get_attribute("src")
        )


class CreatePage(Page):
    PATH = '/talk/'
    MESSAGE = '//td[@class="cell-title talk__message"]'

    def message_open(self):
        self.driver.find_element_by_xpath(self.MESSAGE).click()