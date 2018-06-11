# -*- coding: utf-8 -*-
import unittest

from tests.common import get_driver, Auth, Shop, Main, Topic


class TopicHashTagsTests(unittest.TestCase):

    TAG_WITH_SPEC_SYMBOL_ERROR_MESSAGE = u'В ключевых словах содержатся запрещенные символы'

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

        self.topic = Topic(self.driver)
        self.topic.create()

    def tearDown(self):
        self.shop.remove()
        self.driver.quit()

    def test_add_remove_simple_tag(self):
        self.assertTrue(self.topic.no_one_hashtags())

        tag = 'hashtag'
        self.topic.add_tag(tag)
        self.assertTrue(self.topic.is_exist_tag(tag))

        self.driver.refresh()
        self.assertTrue(self.topic.is_exist_hashtag(tag))

        self.topic.remove_tag(tag)
        self.driver.refresh()
        self.assertTrue(self.topic.no_one_hashtags())

    def test_add_empty_tag(self):
        self.assertTrue(self.topic.no_one_hashtags())

        empty_tag = ''
        self.topic.add_tag(empty_tag)

        self.driver.refresh()
        self.assertTrue(self.topic.no_one_hashtags())

    def test_add_too_short_tag(self):
        too_short_tag = '1'
        self.topic.add_tag(too_short_tag)

        error_message = self.topic.get_tag_error()
        self.assertEqual(u'Минимальная длина ключевого слова 2 символа', error_message)

    def test_add_remove_short_tag(self):
        self.assertTrue(self.topic.no_one_hashtags())

        tag = 'ab'
        self.topic.add_tag(tag)
        self.assertTrue(self.topic.is_exist_tag(tag))

        self.driver.refresh()
        self.assertTrue(self.topic.is_exist_hashtag(tag))

        self.topic.remove_tag(tag)
        self.driver.refresh()
        self.assertTrue(self.topic.no_one_hashtags())

    def test_add_remove_max_length_tag(self):
        self.assertTrue(self.topic.no_one_hashtags())

        max_length = 25
        max_length_tag = 'x' * max_length
        self.topic.add_tag(max_length_tag)
        self.assertTrue(self.topic.is_exist_tag(max_length_tag))

        self.driver.refresh()
        self.assertTrue(self.topic.is_exist_hashtag(max_length_tag))

        self.topic.remove_tag(max_length_tag)
        self.driver.refresh()
        self.assertTrue(self.topic.no_one_hashtags())

    def test_add_too_long_tag(self):
        too_long_length = 26
        too_long_tag = 'x' * too_long_length
        self.topic.add_tag(too_long_tag)

        remaining_tag_length = self.topic.get_remaining_tag_length()
        self.assertEqual(-1, remaining_tag_length)

    def test_add_remove_tag_with_one_space(self):
        self.assertTrue(self.topic.no_one_hashtags())

        tag_with_space = 'hash tag'
        self.topic.add_tag(tag_with_space)
        self.assertTrue(self.topic.is_exist_tag(tag_with_space))

        self.driver.refresh()
        self.assertTrue(self.topic.is_exist_hashtag('HashTag'))

        self.topic.remove_tag(tag_with_space)
        self.driver.refresh()
        self.assertTrue(self.topic.no_one_hashtags())

    def test_add_remove_tag_with_multiple_spaces(self):
        self.assertTrue(self.topic.no_one_hashtags())

        tag_with_spaces = '  my   hash  tag '
        self.topic.add_tag(tag_with_spaces)
        trimmed_tag_with_spaces = tag_with_spaces.strip()
        is_exist_tag = self.topic.is_exist_tag(trimmed_tag_with_spaces)
        self.assertTrue(is_exist_tag)

        self.driver.refresh()
        self.assertTrue(self.topic.is_exist_hashtag('MyHashTag'))

        self.topic.remove_tag(trimmed_tag_with_spaces)
        self.driver.refresh()
        self.assertTrue(self.topic.no_one_hashtags())

    def test_add_tag_with_hash_sign(self):
        wrong_tag = '#tag'
        self.topic.add_tag(wrong_tag)

        error_message = self.topic.get_tag_error()
        self.assertEqual(self.TAG_WITH_SPEC_SYMBOL_ERROR_MESSAGE, error_message)

    def test_add_tag_with_dollar_sign(self):
        wrong_tag = '$tag'
        self.topic.add_tag(wrong_tag)

        error_message = self.topic.get_tag_error()
        self.assertEqual(self.TAG_WITH_SPEC_SYMBOL_ERROR_MESSAGE, error_message)

    def test_add_tag_with_plus_sign(self):
        wrong_tag = 'tag+'
        self.topic.add_tag(wrong_tag)

        error_message = self.topic.get_tag_error()
        self.assertEqual(self.TAG_WITH_SPEC_SYMBOL_ERROR_MESSAGE, error_message)

    def test_add_remove_tag_with_digits(self):
        self.assertTrue(self.topic.no_one_hashtags())

        tag_with_digits = '1234567890'
        self.topic.add_tag(tag_with_digits)
        self.assertTrue(self.topic.is_exist_tag(tag_with_digits))

        self.driver.refresh()
        self.assertTrue(self.topic.is_exist_hashtag(tag_with_digits))

        self.topic.remove_tag(tag_with_digits)
        self.driver.refresh()
        self.assertTrue(self.topic.no_one_hashtags())

    def test_add_remove_tag_with_different_case(self):
        self.assertTrue(self.topic.no_one_hashtags())

        tag_with_different_case = 'DiFfErEnT cAsE'
        self.topic.add_tag(tag_with_different_case)
        tag_lower_case = tag_with_different_case.lower()
        self.assertTrue(self.topic.is_exist_tag(tag_lower_case))

        self.driver.refresh()
        self.assertTrue(self.topic.is_exist_hashtag('DifferentCase'))

        self.topic.remove_tag(tag_lower_case)
        self.driver.refresh()
        self.assertTrue(self.topic.no_one_hashtags())

    # def test_some_keywords_creation(self):
    #     """Позитивный тест на создание нескольких слов"""
    #     keyword_component = ShopForumPage(self.driver).topic_tags
    #     keyword_component.open_tags_input()
    #     keyword_component.set_tag(self.SOME_WORDS_CASE['first_word'])
    #     keyword_component.set_tag(self.ENTER)
    #     keyword_component.set_tag(self.SOME_WORDS_CASE['second_word'])
    #     keyword_component.submit()
    #     # assert
    #
    # def test_too_much_keyword_creation(self):
    #     """Негативный тест на создание слишком большого количества слов"""
    #     keyword_component = ShopForumPage(self.driver).topic_tags
    #     keyword_component.open_tags_input()
    #     # тут придется сделать цикл
    #     for i in range(1, 9):
    #         keyword_component.set_tag(self.EIGHT_WORD_CASE[i])
    #         keyword_component.set_tag(self.ENTER)
    #     keyword_component.submit()
    #     self.assertTrue(keyword_component.is_keyword_error_too_much_words())
    #     self.assertFalse(keyword_component.is_exists_tag())
    #
    # def test_two_same_keyword_creation(self):
    #     """Позитивный тест на создание только одного слова из двух одинаковых"""
    #     keyword_component = ShopForumPage(self.driver).topic_tags
    #     keyword_component.open_tags_input()
    #     keyword_component.set_tag(self.TWICE_WORD)
    #     keyword_component.set_tag(self.ENTER)
    #     keyword_component.set_tag(self.TWICE_WORD)
    #     keyword_component.submit()
