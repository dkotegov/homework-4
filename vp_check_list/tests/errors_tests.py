# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException

from vp_check_list.tests.base_test import BaseTest


class ErrorsCommentsTest(BaseTest):
	TEST_COMMENT = 'Test comment error'

	@classmethod
	def setUpClass(cls):
		super(ErrorsCommentsTest, cls).setUpClass()

		cls.user_avatar.open_avatar()
		cls.avatar_footer = cls.user_avatar.comments

		cls.avatar_footer.add_comment_to_avatar(cls.TEST_COMMENT)

	def test_like_deleted_comment(self):
		avatar_footer = self.user_avatar.comments

		last_comment = avatar_footer.last_comment
		comment_before = last_comment.is_like()
		last_comment.delete_comment()
		last_comment.like()
		comment_after = last_comment.is_like()

		self.assertEqual(comment_before, comment_after)

	def test_repost_deleted_comment(self):
		avatar_footer = self.user_avatar.comments
		last_comment = avatar_footer.last_comment

		repost_before = last_comment.repost_count()
		last_comment.delete_comment()
		try:
			last_comment.repost()
			repost_after = last_comment.repost_count()

			self.assertEqual(repost_before, repost_after)
		except TimeoutException:
			self.assertEqual(1, 1)
