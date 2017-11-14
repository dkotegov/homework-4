# -*- coding: utf-8 -*-

from vp_check_list.base_test import BaseTest


class SimpleActionsWithCommentsTest(BaseTest):
	TEST_COMMENT = 'Test comment'

	def test_add_comment(self):
		avatar = self.user_avatar.get_avatar()
		self.user_avatar.open_avatar(avatar)
		avatar_footer = self.user_avatar.get_avatar_footer()

		self.user_avatar.add_comment_to_avatar(avatar_footer, self.TEST_COMMENT)

		comment = self.user_avatar.get_last_comment_text(avatar_footer)
		self.assertEqual(comment, self.TEST_COMMENT)

	def test_delete_comment(self):
		avatar = self.user_avatar.get_avatar()
		self.user_avatar.open_avatar(avatar)

		avatar_footer = self.user_avatar.get_avatar_footer()
		comment_before_delete = self.user_avatar.get_last_comment_text(avatar_footer)

		self.user_avatar.delete_comment_from_avatar(avatar_footer)

		comment_after_delete = self.user_avatar.get_last_comment_text(avatar_footer)
		self.assertNotEqual(comment_before_delete, comment_after_delete)
