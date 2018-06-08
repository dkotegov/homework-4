# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopForumPage
from tests.common import get_driver, Auth, Shop, Main, Topic, Tag


class SetDeleteKeyWordTests(unittest.TestCase):
    """Набор тестов на разные варианты создания ключевого слова"""
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

        self.shop = Shop(self.driver)
        self.shop.create()
        self.shop.open_forum_page()

        Topic(self.driver).create()

    def tearDown(self):
        self.shop.remove()
        self.driver.quit()

    def test(self):
        tag = Tag(self.driver)
        tag.add_tag('123')
        self.driver.refresh()

        tag.remove_tag('123')
        self.driver.refresh()

    def test_simple_keyword_creation_and_delete(self):
        """Позитивный тест на создание и удаление простого слова"""
        keyword = Tag(self.driver)
        keyword.create(self.SIMPLE_KEYWORD)

        key = keyword.get()
        self.assertEqual(self.SIMPLE_KEYWORD, key)

        keyword.remove()
        self.assertFalse(keyword.is_exist())

    def test_too_long_keyword_creation(self):
        """Негативный тест на создание слишком длинного слова"""
        keyword_component = ShopForumPage(self.driver).topic_tags
        keyword_component.open_tags_input()
        keyword_component.set_tag(self.LONG_KEYWORD_CASE['word'])

        length_counter = keyword_component.get_keyword_length_counter_text()
        self.assertEqual(self.LONG_KEYWORD_CASE['extra_length'], length_counter)

        keyword_component.submit()
        self.assertFalse(keyword_component.is_exists_tag())

    def test_empty_keyword_creation(self):
        """Позитивный тест на то, что пустое слово не создастся"""
        keyword_component = ShopForumPage(self.driver).topic_tags
        keyword_component.open_tags_input()
        keyword_component.set_tag(self.EMPTY_KEYWORD)
        keyword_component.submit()
        self.assertFalse(keyword_component.is_exists_tag())

    def test_too_short_keyword_creation(self):
        """Негативный тест на создание слишком короткого слова"""
        keyword_component = ShopForumPage(self.driver).topic_tags
        keyword_component.open_tags_input()
        keyword_component.set_tag(self.SHORT_KEYWORD)
        keyword_component.submit()

        self.assertTrue(keyword_component.is_keyword_error_min_length_exist())
        self.assertFalse(keyword_component.is_exists_tag())

    def test_keyword_with_space_creation(self):
        """Позитивный тест на создание ключевого слова с пробелом"""
        keyword_component = ShopForumPage(self.driver).topic_tags
        keyword_component.open_tags_input()
        keyword_component.set_tag(self.KEYWORD_WITH_SPACE)
        keyword_component.submit()
        keyword = keyword_component.get_tag()
        self.assertEqual(self.KEYWORD_WITH_SPACE, keyword)

    def test_wrong_keyword_creation(self):
        """Негативный тест на создание слова с запрещенными символами"""
        keyword_component = ShopForumPage(self.driver).topic_tags
        keyword_component.open_tags_input()
        keyword_component.set_tag(self.WRONG_KEYWORD)
        keyword_component.submit()

        self.assertTrue(keyword_component.is_keyword_error_wrong_symbols_exist())
        self.assertFalse(keyword_component.is_exists_tag())

    def test_digit_keyword_creation(self):
        """Позитивный тест на создание слова из цифр"""
        keyword_component = ShopForumPage(self.driver).topic_tags
        keyword_component.open_tags_input()
        keyword_component.set_tag(self.DIGIT_KEYWORD)
        keyword_component.submit()
        keyword = keyword_component.get_tag()
        self.assertEqual(self.DIGIT_KEYWORD, keyword)

    # TODO не работает
    def test_some_keywords_creation(self):
        """Позитивный тест на создание нескольких слов"""
        keyword_component = ShopForumPage(self.driver).topic_tags
        keyword_component.open_tags_input()
        keyword_component.set_tag(self.SOME_WORDS_CASE['first_word'])
        keyword_component.set_tag(self.ENTER)
        keyword_component.set_tag(self.SOME_WORDS_CASE['second_word'])
        keyword_component.submit()
        # TODO посчитать количество слов
        # assert

    def test_too_much_keyword_creation(self):
        """Негативный тест на создание слишком большого количества слов"""
        keyword_component = ShopForumPage(self.driver).topic_tags
        keyword_component.open_tags_input()
        # тут придется сделать цикл
        for i in range(1, 9):
            keyword_component.set_tag(self.EIGHT_WORD_CASE[i])
            keyword_component.set_tag(self.ENTER)
        keyword_component.submit()
        self.assertTrue(keyword_component.is_keyword_error_too_much_words())
        self.assertFalse(keyword_component.is_exists_tag())

    def test_two_same_keyword_creation(self):
        """Позитивный тест на создание только одного слова из двух одинаковых"""
        keyword_component = ShopForumPage(self.driver).topic_tags
        keyword_component.open_tags_input()
        keyword_component.set_tag(self.TWICE_WORD)
        keyword_component.set_tag(self.ENTER)
        keyword_component.set_tag(self.TWICE_WORD)
        keyword_component.submit()
    #     TODO посчитать кочилество слов
