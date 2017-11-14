# -*- coding: utf-8 -*-

from vp_check_list.base_test import BaseTest


class SimpleActionsWithCommentsTest(BaseTest):
	TEST_COMMENT = 'Test comment'

	def setUp(self):
		self.user_avatar.open_avatar()
		self.avatar_footer = self.user_avatar.comments

		# self.avatar_footer.add_comment_to_avatar(self.TEST_COMMENT)

	def tearDown(self):
		# self.avatar_footer.delete_comment_from_avatar()
		pass

	def test_like_comment(self):
		like_before = self.avatar_footer.last_comment.is_like()
		self.avatar_footer.last_comment.like()
		like_after = self.avatar_footer.last_comment.is_like()

		self.assertNotEqual(like_before, like_after)
