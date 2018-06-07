# -*- coding: utf-8 -*-
import time
import unittest

from PageObjects.page_objects import ShopForumPage
from tests.common import get_driver, Auth, Shop, Main, Topic


class SetDeleteKeyWordTests(unittest.TestCase):
    """Набор тестов на разные варианты создания ключевого слова"""
    TOPIC_TEXT = "my topic text"
    SHOP_NAME = u'Shop'

    SIMPLE_KEYWORD = u'ключевое_слово'
    LONG_KEYWORD_CASE = {'word': u'слишком_слишком_длинное_слово',
                         'extra_length': u'-4'}
    EMPTY_KEYWORD = u''
    SHORT_KEYWORD = u'ъ'

    KEYWORD_WITH_SPACE = u'слово с пробелом'
    WRONG_KEYWORD = u'#плохое_слово'
    DIGIT_KEYWORD = u'1234'

    ENTER = u'\n'
    SOME_WORDS_CASE = {'first_word': u'первое_слово',
                       'second_word': u'второе_слово'}
    EIGHT_WORD_CASE = {1: u'первое_слово',
                       2: u'второе_слово',
                       3: u'третье_слово',
                       4: u'четвертое_слово',
                       5: u'пятое_слово',
                       6: u'шестое_слово',
                       7: u'седьмое_слово',
                       8: u'восьмое_слово'}

    TWICE_WORD = u'такое_же_слово'

    def setUp(self):
        self.driver = get_driver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()

        shop = Shop(self.driver)
        shop.create(self.SHOP_NAME)
        shop.open_forum_page()

        Topic(self.driver).create(text=self.TOPIC_TEXT)

    def tearDown(self):
        # Topic(self.driver).remove()
        # # TODO Element <a ...> is not clickable
        # import time
        time.sleep(1)

        Shop(self.driver).remove()
        self.driver.quit()

    def test_simple_keyword_creation_and_delete(self):
        """Позитивный тест на создание и удаление простого слова"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.SIMPLE_KEYWORD)
        keyword_component.submit_keyword()
        keyword = keyword_component.get_keyword()
        self.assertEqual(self.SIMPLE_KEYWORD, keyword)

        keyword_component.open_keyword_edit_field()
        keyword_component.delete_keyword()
        keyword_component.submit_keyword()

        self.assertFalse(keyword_component.is_keyword_exists())

    def test_too_long_keyword_creation(self):
        """Негативный тест на создание слишком длинного слова"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.LONG_KEYWORD_CASE['word'])

        length_counter = keyword_component.get_keyword_length_counter_text()
        self.assertEqual(self.LONG_KEYWORD_CASE['extra_length'], length_counter)

        keyword_component.submit_keyword()
        self.assertFalse(keyword_component.is_keyword_exists())

    def test_empty_keyword_creation(self):
        """Позитивный тест на то, что пустое слово не создастся"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.EMPTY_KEYWORD)
        keyword_component.submit_keyword()
        self.assertFalse(keyword_component.is_keyword_exists())

    def test_too_short_keyword_creation(self):
        """Негативный тест на создание слишком короткого слова"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.SHORT_KEYWORD)
        keyword_component.submit_keyword()

        self.assertTrue(keyword_component.is_keyword_error_min_length_exist())
        self.assertFalse(keyword_component.is_keyword_exists())

    def test_keyword_with_space_creation(self):
        """Позитивный тест на создание ключевого слова с пробелом"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.KEYWORD_WITH_SPACE)
        keyword_component.submit_keyword()
        keyword = keyword_component.get_keyword()
        self.assertEqual(self.KEYWORD_WITH_SPACE, keyword)

    def test_wrong_keyword_creation(self):
        """Негативный тест на создание слова с запрещенными символами"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.WRONG_KEYWORD)
        keyword_component.submit_keyword()

        self.assertTrue(keyword_component.is_keyword_error_wrong_symbols_exist())
        self.assertFalse(keyword_component.is_keyword_exists())

    def test_digit_keyword_creation(self):
        """Позитивный тест на создание слова из цифр"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.DIGIT_KEYWORD)
        keyword_component.submit_keyword()
        keyword = keyword_component.get_keyword()
        self.assertEqual(self.DIGIT_KEYWORD, keyword)

    # TODO не работает
    def test_some_keywords_creation(self):
        """Позитивный тест на создание нескольких слов"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.SOME_WORDS_CASE['first_word'])
        keyword_component.set_keyword(self.ENTER)
        keyword_component.set_keyword(self.SOME_WORDS_CASE['second_word'])
        keyword_component.submit_keyword()
        # TODO посчитать количество слов
        # assert

    def test_too_much_keyword_creation(self):
        """Негативный тест на создание слишком большого количества слов"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        # тут придется сделать цикл
        for i in range(1, 9):
            keyword_component.set_keyword(self.EIGHT_WORD_CASE[i])
            keyword_component.set_keyword(self.ENTER)
        keyword_component.submit_keyword()
        self.assertTrue(keyword_component.is_keyword_error_too_much_words())
        self.assertFalse(keyword_component.is_keyword_exists())

    def test_two_same_keyword_creation(self):
        """Позитивный тест на создание только одного слова из двух одинаковых"""
        keyword_component = ShopForumPage(self.driver).keyword_component
        keyword_component.open_keyword_field()
        keyword_component.set_keyword(self.TWICE_WORD)
        keyword_component.set_keyword(self.ENTER)
        keyword_component.set_keyword(self.TWICE_WORD)
        keyword_component.submit_keyword()
    #     TODO посчитать кочилество слов
    #     assert
