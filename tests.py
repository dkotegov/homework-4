# -*- coding: utf-8 -*-

import os
import unittest

from datetime import datetime, time

from selenium.webdriver import DesiredCapabilities, Remote

from elements.AuthPage import AuthPage
from elements.CreatePage import CreatePage
from elements.MessageForm import MessageForm
from elements.UserForm import UserForm
from elements.DialogForm import DialogForm



class Test(unittest.TestCase):
    USEREMAIL = os.environ['USEREMAIL']
    PASSWORD = os.environ['PASSWORD']

    MESSAGE_TEXT = u'Привет! Тебе сообщение)'
    EMPTY_MESSAGE_TEXT = ' \n \t\t   '
    STYLE = 'display: block'
    ERROR_TYPE = u'Пожалуйста, выберите изображение (jpg/gif/png).'
    ERROR_SIZE = u'Размер изображения не должен превышать 20 Мб.'
    BIG_IMG_PATH = '/Zebras.jpg'
    NOT_IMG_PATH = '/basic.py'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        user_name = auth_page.top_menu.get_username()

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.message_open()

    def test_send_message(self):
        message_form = MessageForm(self.driver)
        message_form.set_message_text(self.MESSAGE_TEXT)
        message_form.message_send()
        last_message_text = message_form.get_last_message_text()
        self.assertEqual(self.MESSAGE_TEXT, last_message_text)

    def test_send_empty_message(self):
        message_form = MessageForm(self.driver)
        message_form.set_message_text(self.EMPTY_MESSAGE_TEXT)
        message_form.message_send()
        messagebox_text = message_form.get_textarea_value()
        self.assertNotEqual(messagebox_text, u'')

    def test_go_to_the_dialogues(self):
        message_form = MessageForm(self.driver)
        message_form_url = self.driver.current_url
        message_form.back_to_dialogs()
        dialogs_url = self.driver.current_url
        self.assertNotEqual(message_form_url, dialogs_url)

    def test_go_to_the_friend_page(self):
        message_form = MessageForm(self.driver)
        message_form_friend_name = message_form.friend_name()
        message_form.go_to_friend_page()
        user_form = UserForm(self.driver)
        friend_name = user_form.user_name()
        self.assertEqual(message_form_friend_name, friend_name)

    def test_check_time(self):
        message_form = MessageForm(self.driver)
        message_form.set_message_text(self.MESSAGE_TEXT)
        message_form.message_send()
        last_message_time = message_form.get_last_message_time()
        self.assertEqual(datetime.strftime(datetime.now(), '%H:%M:%S'), str(last_message_time))

    def test_avatar(self):
        self.driver.back()
        dialog_form = DialogForm(self.driver)
        dialog_avatar_src = dialog_form.get_dialogs_avatar_src()
        dialog_form.go_to_user_page()
        user_form = UserForm(self.driver)
        avatar_src = user_form.get_avatar_src()
        self.assertEqual(dialog_avatar_src, avatar_src)

    def test_open_close_img_window(self):
        message_form = MessageForm(self.driver)
        message_form.open_img_window()
        self.assertTrue(message_form.display_img_window())
        message_form.close_img_window()
        self.assertFalse(message_form.display_img_window())

    def test_cancel_add_img(self):
        message_form = MessageForm(self.driver)
        message_form.open_img_window()
        message_form.cancel_add_img()
        self.assertFalse(message_form.display_img_window())

    def test_download_unselected_img(self):
        message_form = MessageForm(self.driver)
        message_form.open_img_window()
        message_form.download_img()
        error_message = message_form.get_error_message()
        self.assertEqual(error_message, self.ERROR_TYPE)

    def test_download_big_or_not_img(self):
        message_form = MessageForm(self.driver)
        message_form.open_img_window()
        message_form.choose_img_button()
        message_form.choose_img(self.BIG_IMG_PATH)
        message_form.download_img()
        error_message = message_form.get_error_message()
        self.assertEqual(error_message, self.ERROR_SIZE)
        self.driver.refresh()
        message_form.open_img_window()
        message_form.choose_img_button()
        message_form.choose_img(self.NOT_IMG_PATH)
        message_form.download_img()
        error_message = message_form.get_error_message()
        self.assertEqual(error_message, self.ERROR_TYPE)

    def tearDown(self):
        self.driver.quit()

