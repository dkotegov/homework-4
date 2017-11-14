# -*- coding: utf-8 -*-

from vp_check_list.base_test import BaseTest


class SimpleActionsWithCommentsTest(BaseTest):
	TEST_COMMENT = 'Test comment'

	def test_like_comment(self):
		self.user_avatar.open_avatar()
		avatar_footer = self.user_avatar.comments

		avatar_footer.add_comment_to_avatar(self.TEST_COMMENT)

		like_btn = avatar_footer.last_comment.likes()

		comment = avatar_footer.last_comment.text()
		self.assertEqual(comment, self.TEST_COMMENT)
