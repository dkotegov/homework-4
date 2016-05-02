# -*- coding: utf-8 -*-
from pages.AnswerQuestion import OtvetPageQuestion
from tests.ask import BaseTest


class AnswerQuestionTests(BaseTest):

    def setUp(self):
        super(AnswerQuestionTests, self).setUp()
        self.answer_page = OtvetPageQuestion(self.driver)
        self.answer_page.open()
        self.answer_page.open_login_frame()
        t = self.answer_page.auth_form()
        t.set_login("zzz-zzzz-90")
        t.set_domain("list.ru")
        t.set_password("Qwerty12")
        t.login()
        self.answer_page.close_login_frame()
        self.answer_page.open_question()
        self.driver.implicitly_wait(5)

    def test_empty_text(self):
        form = self.answer_page.answer_form()
        form.submit()
        self.driver.implicitly_wait(2)
        self.assertEqual(u'Невозможно опубликовать пустой текст',self.answer_page.error_poput())

    def test_text_limit_exceed_check(self):
        form = self.answer_page.answer_form()
        form.set_text('a' * (form.MAX_SYMBOLS + 100))
        self.assertEqual(int(form.count_symbols_value()), 0)

    def test_like_dislike(self):
        self.answer_page.like()
        self.assertTrue(self.answer_page.is_liked())
        self.answer_page.dislike()
        self.assertTrue(self.answer_page.is_unliked())

    def test_sub_unsub(self):
        self.answer_page.subscribe()
        self.assertTrue(self.answer_page.is_subscribed())
        self.answer_page.unsubscribe()
        self.assertTrue(self.answer_page.is_unsubscribed())