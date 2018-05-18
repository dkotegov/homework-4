# -*- coding: utf-8 -*-

import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.primary.auth_page import AuthPage
from tests.pages.primary.photo_page import PhotoPage


class CommentsTest(unittest.TestCase):
    USERNAME = u'Куклина Нина'
    LOGIN = os.environ.get('LOGIN')
    PASSWORD = os.environ.get('PASSWORD')
    
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.LOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()
        self.photo_page = PhotoPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_answer_comment(self):
        answer_text = 'answer'
        self.photo_page.goto_photo_comment()
        comments = self.photo_page.comments

        comments.click_answer()

        input_comment = self.photo_page.input_comment
        input_comment.add_answer_text(answer_text)

        ans = comments.check_answer()
        self.assertTrue(ans)

    def test_add_video(self):
        self.photo_page.goto_photo_comment()
        input_comment = self.photo_page.input_comment

        input_comment.add_video()

        input_comment.send()

        comments = self.photo_page.comments
        video_in_attach_number = comments.get_newest_comment_video_attach_num()
        self.assertEqual(1, video_in_attach_number)

    def test_add_one_photo(self):
        self.photo_page.goto_photo_comment()
        input_comment = self.photo_page.input_comment

        input_comment.add_one_photo()
        input_comment.wait_progress_bar()
        input_comment.send()

        comments = self.photo_page.comments
        photo_in_attach_number = comments.get_newest_comment_photo_attach_num()

        self.assertEqual(1, photo_in_attach_number)

    def test_add_two_photo(self):
        self.photo_page.goto_photo_comment()
        input_comment = self.photo_page.input_comment

        input_comment.add_one_photo()
        input_comment.wait_progress_bar()

        input_comment.add_one_photo()
        input_comment.wait_progress_bar()

        input_comment.send()

        comments = self.photo_page.comments
        photo_in_attach_number = comments.get_newest_comment_photo_attach_num()

        self.assertEqual(2, photo_in_attach_number)

    def test_add_comment_sticker(self):
        self.photo_page.goto_photo_comment()

        input_comment = self.photo_page.input_comment
        sticker_data_code = input_comment.add_comment_sticker()

        self.photo_page.reload()

        comments = self.photo_page.comments
        newest_sticker_data_code = comments.get_newest_comment_sticker()
        self.assertEqual(sticker_data_code, newest_sticker_data_code)

    def test_add_comment_smile(self):
        smile_class = "emoji_ok_04"
        self.photo_page.goto_photo_comment()

        input_comment = self.photo_page.input_comment
        input_comment.add_comment_smile(smile_class)

        self.photo_page.reload()

        comments = self.photo_page.comments
        content = comments.get_newest_comment_smile()
        self.assertIn(smile_class, content)

    def test_add_comment(self):
        text = 'hello QA'
        self.photo_page.goto_photo_comment()
        input_comment = self.photo_page.input_comment
        input_comment.add_comment_text(text)

        comment_text = self.photo_page.comments.get_newest_comment_text()
        self.assertEqual(text, comment_text)

    def test_undelete_comment(self):
        self.photo_page.goto_photo_comment()
        comments = self.photo_page.comments

        count_first = comments.count_comments()

        comments.delete_comment()
        comments.undelete_comment()
        self.photo_page.reload()

        count_second = comments.count_comments()
        delta = count_first - count_second
        self.assertEqual(delta, 0)

    def test_delete_comment(self):
        self.photo_page.goto_photo_comment()

        comments = self.photo_page.comments

        count_first = comments.count_comments()

        comments.delete_comment()
        self.photo_page.reload()

        count_second = comments.count_comments()
        delta = count_first - count_second
        self.assertNotEqual(delta, 0)
