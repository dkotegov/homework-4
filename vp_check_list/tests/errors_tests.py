# -*- coding: utf-8 -*-

from vp_check_list.tests.base_test import BaseTest


class CombineActionsCommentsTest(BaseTest):
	@classmethod
	def setUpClass(cls):
		super(CombineActionsCommentsTest, cls).setUpClass()
		cls.user_avatar.open_avatar()

	def test_like_deleted_comment(self):
		avatar_footer = self.user_avatar.comments

		last_comment = avatar_footer.last_comment
		comment_before = last_comment.is_like()
		last_comment.delete_comment()
		last_comment.like()
		comment_after = last_comment.is_like()

		self.assertEqual(comment_before, comment_after)
