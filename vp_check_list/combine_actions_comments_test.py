# -*- coding: utf-8 -*-

from vp_check_list.base_test import BaseTest


class CombineActionsCommentsTest(BaseTest):
	TEST_COMMENT = 'Test comment'

	@classmethod
	def setUpClass(cls):
		super(CombineActionsCommentsTest, cls).setUpClass()
		cls.user_avatar.open_avatar()

	def test_add_and_delete_comment(self):
		avatar_footer = self.user_avatar.comments

		comment_before = avatar_footer.last_comment.text()
		avatar_footer.add_comment_to_avatar(self.TEST_COMMENT)

		avatar_footer.delete_comment_from_avatar()
		comment_after = avatar_footer.last_comment.text()

		self.assertEqual(comment_before, comment_after)
