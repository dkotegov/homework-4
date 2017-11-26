from tests.main import Tests
from selenium.common.exceptions import StaleElementReferenceException


class ReshareTests(Tests):
    # def test_share_now(self):
    #     self._post_string("msg", False)
    #     profile_page = self._to_profile_page()
    #     post = profile_page.get_last_post()
    #     reshare_panel = post.get_reshare_panel()
    #     reshare_panel.share_now()
    #     self.assertTrue(reshare_panel.is_shared_now())
    #
    # def test_share_in_message(self):
    #     self._post_string("msg", False)
    #     profile_page = self._to_profile_page()
    #     post = profile_page.get_last_post()
    #     reshare_panel = post.get_reshare_panel()
    #     reshare_in_msg_view = reshare_panel.share_in_message()
    #     reshare_in_msg_view.select_friend(0)
    #     reshare_in_msg_view.submit()
    #     self.assertRaises(StaleElementReferenceException, reshare_in_msg_view.visible)
    #
    # def test_share_with_text(self):
    #     self._post_string("msg", False)
    #     profile_page = self._to_profile_page()
    #     post = profile_page.get_last_post()
    #     reshare_panel = post.get_reshare_panel()
    #     reshare_with_text = reshare_panel.share_with_text()
    #     comment_msg = "some_text"
    #     reshare_with_text.set_text(comment_msg)
    #     reshare_with_text.set_to_status(True)
    #     reshare_with_text.submit()
    #
    #     profile_page = self._to_profile_page()
    #     status = profile_page.get_status()
    #     self.assertTrue(status.contains_text())
    #     self.assertEqual(comment_msg, status.get_status_string())

    def test_share_in_group(self):
        self._post_string("msg", False)
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        reshare_panel = post.get_reshare_panel()
        reshare_in_group = reshare_panel.share_in_group()
        reshare_in_group.set_text("reshare")

        group_name = "test.technopark.sasad"
        reshare_in_group.set_group(group_name)
        reshare_in_group.submit()
        got_group_name = profile_page.get_reshared_group_name()
        self.assertEqual(group_name, got_group_name)