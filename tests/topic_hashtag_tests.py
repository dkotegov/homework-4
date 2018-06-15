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

    def test_add_remove_one_tag(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        TAG = 'hashtag'
        self.topic.add_tag(TAG)

        self.check_temp_tag(TAG)
        self.driver.refresh()
        self.check_hashtag(TAG)

        self.topic.remove_tag(TAG)

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_empty_tag(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        self.topic.add_tag('')

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_too_short_tag(self):
        TOO_SHORT_TAG = '1'
        self.topic.add_tag(TOO_SHORT_TAG)

        error_message = self.topic.get_tag_error()
        self.assertEqual(self.MINIMUM_LENGTH_OF_TAG_WARNING_MESSAGE, error_message)

    def test_add_remove_short_tag(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        SHORT_TAG = 'ab'
        self.topic.add_tag(SHORT_TAG)

        self.check_temp_tag(SHORT_TAG)
        self.driver.refresh()
        self.check_hashtag(SHORT_TAG)

        self.topic.remove_tag(SHORT_TAG)

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_remove_max_length_tag(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        TAG_LENGTH = 25
        LONG_TAG = 'x' * TAG_LENGTH
        self.topic.add_tag(LONG_TAG)

        self.check_temp_tag(LONG_TAG)
        self.driver.refresh()
        self.check_hashtag(LONG_TAG)

        self.topic.remove_tag(LONG_TAG)

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_too_long_tag(self):
        TAG_LENGTH = 26
        TOO_LONG_TAG = 'x' * TAG_LENGTH
        self.topic.add_tag(TOO_LONG_TAG)

        remaining_tag_length = self.topic.get_remaining_tag_length()
        self.assertEqual(-1, remaining_tag_length)

    def test_add_remove_tag_with_one_space(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        TAG_WITH_SPACE = 'hash tag'
        self.topic.add_tag(TAG_WITH_SPACE)

        self.check_temp_tag(TAG_WITH_SPACE)
        self.driver.refresh()
        self.check_hashtag('HashTag')

        self.topic.remove_tag(TAG_WITH_SPACE)

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_remove_tag_with_multiple_spaces(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        TAG_WITH_SPACES = '  my   hash  tag '
        self.topic.add_tag(TAG_WITH_SPACES)

        trimmed_tag_with_spaces = TAG_WITH_SPACES.strip()
        self.check_temp_tag(trimmed_tag_with_spaces)
        self.driver.refresh()
        self.check_hashtag('MyHashTag')

        self.topic.remove_tag(trimmed_tag_with_spaces)

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_tag_with_hash_sign(self):
        WRONG_TAG = '#tag'
        self.topic.add_tag(WRONG_TAG)

        error_message = self.topic.get_tag_error()
        self.assertEqual(self.TAG_WITH_SPEC_SYMBOL_ERROR_MESSAGE, error_message)

    def test_add_tag_with_plus_sign(self):
        WRONG_TAG = 'tag+'
        self.topic.add_tag(WRONG_TAG)

        error_message = self.topic.get_tag_error()
        self.assertEqual(self.TAG_WITH_SPEC_SYMBOL_ERROR_MESSAGE, error_message)

    def test_add_tag_with_spec_symbols(self):
        TAG_WITH_SPEC_SYMBOLS = '.@!/my-hash_tag()\":\'&?'
        self.topic.add_tag(TAG_WITH_SPEC_SYMBOLS)

        self.driver.refresh()
        self.check_hashtag('MyHash_tag')

    def test_add_remove_tag_with_digits(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        TAG_WITH_DIGITS = '1234567890'
        self.topic.add_tag(TAG_WITH_DIGITS)

        self.check_temp_tag(TAG_WITH_DIGITS)
        self.driver.refresh()
        self.check_hashtag(TAG_WITH_DIGITS)

        self.topic.remove_tag(TAG_WITH_DIGITS)

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_remove_tag_with_different_case(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        TAG_WITH_DIFFERENT_CASE = 'DiFfErEnT cAsE'
        self.topic.add_tag(TAG_WITH_DIFFERENT_CASE)

        tag_lower_case = TAG_WITH_DIFFERENT_CASE.lower()
        self.check_temp_tag(tag_lower_case)
        self.driver.refresh()
        self.check_hashtag('DifferentCase')

        self.topic.remove_tag(tag_lower_case)

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_remove_two_different_tags(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        TAGS = ['first', 'second']
        self.topic.add_all_tags(TAGS)

        number_of_tags = self.topic.get_number_of_temp_tags()
        self.assertEqual(len(TAGS), number_of_tags)
        for tag in TAGS:
            is_exist_tag = self.topic.is_exist_temp_tag(tag)
            self.assertTrue(is_exist_tag)

        self.driver.refresh()
        number_of_hashtags = self.topic.get_number_of_hashtags()
        self.assertEqual(len(TAGS), number_of_hashtags)
        for tag in TAGS:
            is_exist_hashtag = self.topic.is_exist_hashtag(tag)
            self.assertTrue(is_exist_hashtag)

        self.topic.remove_all_tags(TAGS)

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_two_same_tags(self):
        TAGS = ['same', 'same']
        self.topic.add_all_tags(TAGS)

        self.check_temp_tag(TAGS[0])
        self.driver.refresh()
        self.check_hashtag(TAGS[0])

    def test_add_remove_maximum_tags(self):
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

        TAGS = ['11', '22', '33', '44', '55', '66', '77']
        self.topic.add_all_tags(TAGS)

        number_of_tags = self.topic.get_number_of_temp_tags()
        self.assertEqual(len(TAGS), number_of_tags)
        for tag in TAGS:
            is_exist_tag = self.topic.is_exist_temp_tag(tag)
            self.assertTrue(is_exist_tag)

        self.driver.refresh()
        number_of_hashtags = self.topic.get_number_of_hashtags()
        self.assertEqual(len(TAGS), number_of_hashtags)
        for tag in TAGS:
            is_exist_hashtag = self.topic.is_exist_hashtag(tag)
            self.assertTrue(is_exist_hashtag)

        self.topic.remove_all_tags(TAGS)

        self.driver.refresh()
        no_one_hashtags = self.topic.no_one_hashtags()
        self.assertTrue(no_one_hashtags)

    def test_add_too_much_tags(self):
        TAGS = ['11', '22', '33', '44', '55', '66', '77', '88']
        self.topic.add_all_tags(TAGS)

        error_message = self.topic.get_tag_error()
        self.assertEqual(self.TAGS_ARE_ENOUGH_WARNING_MESSAGE, error_message)

    def test_add_edit_one_tag(self):
        TAG = 'tag'
        self.topic.add_tag(TAG)
        self.check_temp_tag(TAG)

        NEW_TAG = 'new_tag'
        self.topic.edit_tag(TAG, NEW_TAG)

        self.check_temp_tag(NEW_TAG)
        self.driver.refresh()
        self.check_hashtag(NEW_TAG)

    def test_add_two_tags_edit_first(self):
        TAGS = ['first', 'last']
        self.topic.add_all_tags(TAGS)

        NEW_TAG = 'new_tag'
        self.topic.edit_tag(TAGS[0], NEW_TAG)

        NEW_TAGS = [TAGS[1], NEW_TAG]
        self.check_all_temp_tags(NEW_TAGS)
        self.driver.refresh()
        self.check_all_hashtags(NEW_TAGS)

    def test_add_two_tags_edit_last(self):
        TAGS = ['first', 'last']
        self.topic.add_all_tags(TAGS)

        NEW_TAG = 'new_tag'
        self.topic.edit_tag(TAGS[1], NEW_TAG)

        NEW_TAGS = [TAGS[0], NEW_TAG]
        self.check_all_temp_tags(NEW_TAGS)
        self.driver.refresh()
        self.check_all_hashtags(NEW_TAGS)

    def test_add_several_tags_edit_all(self):
        TAG = ['11', '22', '33', '44']
        self.topic.add_all_tags(TAG)

        NEW_TAGS = ['00', '100']
        self.topic.edit_all_tags(TAG, NEW_TAGS)

        self.check_all_temp_tags(NEW_TAGS)
        self.driver.refresh()
        self.check_all_hashtags(NEW_TAGS)

    def check_temp_tag(self, tag):
        number_of_tags = self.topic.get_number_of_temp_tags()
        self.assertEqual(1, number_of_tags)
        is_exist_tag = self.topic.is_exist_temp_tag(tag)
        self.assertTrue(is_exist_tag)

    def check_all_temp_tags(self, tags):
        number_of_tags = self.topic.get_number_of_temp_tags()
        self.assertEqual(len(tags), number_of_tags)
        for tag in tags:
            is_exist_tag = self.topic.is_exist_temp_tag(tag)
            self.assertTrue(is_exist_tag)

    def check_hashtag(self, hashtag):
        number_of_hashtags = self.topic.get_number_of_hashtags()
        self.assertEqual(1, number_of_hashtags)
        is_exist_hashtag = self.topic.is_exist_hashtag(hashtag)
        self.assertTrue(is_exist_hashtag)

    def check_all_hashtags(self, hashtags):
        number_of_hashtags = self.topic.get_number_of_hashtags()
        self.assertEqual(len(hashtags), number_of_hashtags)
        for tag in hashtags:
            is_exist_hashtag = self.topic.is_exist_hashtag(tag)
            self.assertTrue(is_exist_hashtag)
