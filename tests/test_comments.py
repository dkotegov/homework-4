# -*- coding: utf-8 -*-

import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.pages.primary.auth_page import AuthPage
from tests.pages.primary.photo_page import PhotoPage
import tests.strings.str_comments as str_comments


class CommentsTest(unittest.TestCase):
    USERNAME = u'Куклина Нина'
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

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
        self.photo_page.goto_photo_comment()

    def tearDown(self):
        self.driver.quit()

    def test_add_comment_base(self):
        text = 'hello QA'
        input_comment = self.photo_page.input_comment
        input_comment.add_comment_text(text)
        comment_text = self.photo_page.comments.get_newest_comment_text()
        self.assertEqual(text, comment_text)

    def test_comment_too_much_not_send(self):
        text = str_comments.str_after_limit_11
        input_comment = self.photo_page.input_comment
        err = input_comment.try_add_comment_text(text)
        self.assertFalse(0, err)

    def test_add_comment_empty_not_send(self):
        text = ''
        input_comment = self.photo_page.input_comment
        input_comment.add_comment_text(text)
        err = input_comment.add_comment_text(text)
        self.assertFalse(0, err)

    def test_comment_too_much_err_msg(self):
        text = str_comments.str_after_limit_11
        input_comment = self.photo_page.input_comment
        input_comment.try_add_comment_text(text)
        err = input_comment.get_comments_add_err()
        ans = 'Слишком длинный комментарий.'
        self.assertEqual(ans, err)

    def test_comment_counter_before_limit(self):
        text = str_comments.str_before_limit_43
        before_limit_counter = '43'
        input_comment = self.photo_page.input_comment
        input_comment.insert_text(text)
        counter_symb = input_comment.get_comment_limit_counter()
        self.assertEqual(before_limit_counter, counter_symb)

    def test_comment_counter_limit(self):
        text = str_comments.str_limit_4096
        limit_counter = '0'
        input_comment = self.photo_page.input_comment
        input_comment.insert_text(text)
        counter_symb = input_comment.get_comment_limit_counter()
        self.assertEqual(limit_counter, counter_symb)

    def test_comment_counter_marker_after_limit(self):
        text = str_comments.str_after_limit_11
        after_limit_counter = '-11'
        input_comment = self.photo_page.input_comment
        input_comment.insert_text(text)
        counter_symb = input_comment.get_comment_limit_counter()
        self.assertEqual(after_limit_counter, counter_symb)

    def test_сomment_changing_counter_after_add_symbol(self):
        text = str_comments.str_after_limit_11
        input_comment = self.photo_page.input_comment
        input_comment.insert_text(text)
        current_counter = input_comment.get_comment_limit_counter()
        interaction = input_comment.counter_interact_add(current_counter)
        self.assertTrue(interaction)

    def test_сomment_changing_counter_after_del_symbol(self):
        text = str_comments.str_after_limit_11
        input_comment = self.photo_page.input_comment
        input_comment.insert_text(text)
        current_counter = input_comment.get_comment_limit_counter()
        interaction = input_comment.counter_interact_del(current_counter)
        self.assertTrue(interaction)

    def test_add_comment_html_injejction(self):
        text_html = '<i>hello QA</i>'
        text_ans = 'hello QA'
        input_comment = self.photo_page.input_comment
        input_comment.add_comment_text(text_html)
        comment_text = self.photo_page.comments.get_newest_comment_text()
        self.assertEqual(text_ans, comment_text)

    def test_add_comment_empty_html_not_send(self):
        text = '<br><br>'
        input_comment = self.photo_page.input_comment
        err = input_comment.add_comment_text(text)
        self.assertFalse(0, err)

    def test_answer_comment(self):
        answer_text = 'answer'
        comments = self.photo_page.comments
        comments.click_answer()

        input_comment = self.photo_page.input_comment
        input_comment.add_answer_text(answer_text)

        ans = comments.check_answer()
        self.assertTrue(ans)

    def test_add_video(self):
        input_comment = self.photo_page.input_comment
        input_comment.add_video()
        input_comment.send()

        comments = self.photo_page.comments
        video_in_attach_number = comments.get_newest_comment_video_attach_num()
        self.assertEqual(1, video_in_attach_number)

    def test_add_video_by_url(self):
        url = 'https://www.youtube.com/watch?v=Ep6SQcMg3Jk&list=PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5&index=1 '
        input_comment = self.photo_page.input_comment
        input_comment.input_text(url)
        input_comment.wait_video_preview_display()
        input_comment.send()

        comments = self.photo_page.comments
        video_in_attach_number = comments.get_newest_comment_video_attach_num()
        self.assertEqual(1, video_in_attach_number)

    def test_add_video_by_url_link(self):
        url = 'https://www.youtube.com/watch?v=Ep6SQcMg3Jk&list=PLPOCJi2Sznkr2p-HenHsOQ384fkek4QB5&index=1 '
        input_comment = self.photo_page.input_comment
        input_comment.input_text(url)
        input_comment.wait_video_preview_display()
        input_comment.send()

        comments = self.photo_page.comments
        video_in_attach_link = comments.get_newest_comment_video_attach_url()
        self.assertEqual(url.strip(), video_in_attach_link)

    def test_add_one_photo(self):
        input_comment = self.photo_page.input_comment

        input_comment.add_one_photo()
        input_comment.wait_progress_bar()
        input_comment.send()

        comments = self.photo_page.comments
        photo_in_attach_number = comments.get_newest_comment_photo_attach_num()

        self.assertEqual(1, photo_in_attach_number)

    def test_add_two_photo(self):
        input_comment = self.photo_page.input_comment

        input_comment.add_one_photo()
        input_comment.wait_progress_bar()

        input_comment.add_one_photo()
        input_comment.wait_progress_bar()

        input_comment.send()

        comments = self.photo_page.comments
        photo_in_attach_number = comments.get_newest_comment_photo_attach_num()

        self.assertEqual(2, photo_in_attach_number)

    def test_add_photo_by_url(self):
        url = 'https://img.getbg.net/upload/small/www.GetBg.net_Cartoons_Homer_Simpson_quickly_runs_away_095322_.jpg '
        input_comment = self.photo_page.input_comment
        input_comment.input_text(url)
        input_comment.wait_img_preview_display()
        input_comment.send()

        comments = self.photo_page.comments
        photo_in_attach_number = comments.get_newest_comment_photo_attach_num()

        self.assertEqual(1, photo_in_attach_number)

    def test_add_comment_sticker(self):
        input_comment = self.photo_page.input_comment
        sticker_data_code = input_comment.add_comment_sticker()

        self.photo_page.reload()

        comments = self.photo_page.comments
        newest_sticker_data_code = comments.get_newest_comment_sticker()
        self.assertEqual(sticker_data_code, newest_sticker_data_code)

    def test_add_comment_smile(self):
        smile_class = "emoji_ok_04"
        input_comment = self.photo_page.input_comment
        input_comment.add_comment_smile(smile_class)

        self.photo_page.reload()

        comments = self.photo_page.comments
        content = comments.get_newest_comment_smile()
        self.assertIn(smile_class, content)

    def test_undelete_comment(self):
        comments = self.photo_page.comments

        count_first = comments.count_comments()

        comments.delete_comment()
        comments.undelete_comment()
        self.photo_page.reload()

        count_second = comments.count_comments()
        delta = count_first - count_second
        self.assertEqual(delta, 0)

    def test_delete_comment(self):
        comments = self.photo_page.comments
        count_first = comments.count_comments()

        comments.delete_comment()
        self.photo_page.reload()

        count_second = comments.count_comments()
        delta = count_first - count_second
        self.assertNotEqual(delta, 0)
