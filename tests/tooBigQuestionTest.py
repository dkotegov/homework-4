from tests.pages.AskPage import AskPage

import unittest

class TooBigQuestionTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.page = AskPage()
        super(TooBigQuestionTest, self).__init__(*args, **kwargs)

    def test_01(self):
        bigStr = ''
        for _ in range(122):
            bigStr = bigStr + 'a'
        self.page.setQuestionTheme(bigStr)
        self.assertEqual(self.page.getAlertUnderQuestion(),
            'Поле «Тема вопроса» не может быть больше 120 символов.')

    def tearDown(self):
        self.page.quitDriver()