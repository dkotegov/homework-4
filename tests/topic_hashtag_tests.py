# -*- coding: utf-8 -*-
import unittest

from tests.common import get_driver, Auth, Shop, Main, Topic


class TopicHashTagsTests(unittest.TestCase):
    TAG_WITH_SPEC_SYMBOL_ERROR_MESSAGE = u'В ключевых словах содержатся запрещенные символы'
    TAGS_ARE_ENOUGH_WARNING_MESSAGE = u'Ключевых слов достаточно, спасибо'
    MINIMUM_LENGTH_OF_TAG_WARNING_MESSAGE = u'Минимальная длина ключевого слова 2 символа'

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
        self.assertEqual(self.MINIMUM_LENGTH_OF_TAG_WARNING_MESSAGE, error_message)

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

    def test_add_tag_with_spec_symbols(self):
        tag_with_spec_symbols = '.@!/my-hash_tag()\":\'&?'
        self.topic.add_tag(tag_with_spec_symbols)

        self.driver.refresh()
        number_of_hashtags = self.topic.get_number_of_hashtags()
        self.assertEqual(1, number_of_hashtags)
        is_exist_hashtag = self.topic.is_exist_hashtag('MyHash_tag')
        self.assertTrue(is_exist_hashtag)

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

    def test_add_remove_two_different_tags(self):
        there_are_no_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(there_are_no_hashtags)

        tags = ['first', 'second']
        self.topic.add_tags(tags)

        number_of_tags = self.topic.get_number_of_tags()
        self.assertEqual(len(tags), number_of_tags)
        is_exist_first_tag = self.topic.is_exist_tag(tags[0])
        self.assertTrue(is_exist_first_tag)
        is_exist_second_tag = self.topic.is_exist_tag(tags[1])
        self.assertTrue(is_exist_second_tag)

        self.driver.refresh()
        number_of_hashtags = self.topic.get_number_of_hashtags()
        self.assertEqual(len(tags), number_of_hashtags)
        is_exist_first_hashtag = self.topic.is_exist_hashtag(tags[0])
        self.assertTrue(is_exist_first_hashtag)
        is_exist_second_hashtag = self.topic.is_exist_hashtag(tags[1])
        self.assertTrue(is_exist_second_hashtag)

        self.topic.remove_all_tags(tags)
        self.driver.refresh()
        there_are_no_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(there_are_no_hashtags)

    def test_add_two_same_tags(self):
        tags = ['same', 'same']
        self.topic.add_tags(tags)

        number_of_tags = self.topic.get_number_of_tags()
        self.assertEqual(1, number_of_tags)

        self.driver.refresh()
        number_of_hashtags = self.topic.get_number_of_hashtags()
        self.assertEqual(1, number_of_hashtags)

    def test_add_remove_maximum_tags(self):
        there_are_no_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(there_are_no_hashtags)

        tags = ['11', '22', '33', '44', '55', '66', '77']
        self.topic.add_tags(tags)

        number_of_tags = self.topic.get_number_of_tags()
        self.assertEqual(len(tags), number_of_tags)
        for tag in tags:
            is_exist_tag = self.topic.is_exist_tag(tag)
            self.assertTrue(is_exist_tag)

        self.driver.refresh()
        number_of_hashtags = self.topic.get_number_of_hashtags()
        self.assertEqual(len(tags), number_of_hashtags)
        for tag in tags:
            is_exist_hashtag = self.topic.is_exist_hashtag(tag)
            self.assertTrue(is_exist_hashtag)

        self.topic.remove_all_tags(tags)
        self.driver.refresh()
        there_are_no_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(there_are_no_hashtags)

    def test_add_too_much_tags(self):
        tags = ['11', '22', '33', '44', '55', '66', '77', '88']
        self.topic.add_tags(tags)

        error_message = self.topic.get_tag_error()
        self.assertEqual(self.TAGS_ARE_ENOUGH_WARNING_MESSAGE, error_message)
