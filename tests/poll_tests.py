from selenium.common.exceptions import WebDriverException

from tests.PostPage.PostPage import PostPage
from tests.main import Tests


class PollTests(Tests):
    def test_post_poll_no_answer(self):
        post_page = self._to_post_page()
        post_form = post_page.get_post_form()
        poll_view = post_form.open_poll_creation()
        poll_view.write_question("question")
        self.assertRaises(WebDriverException, post_form.share)
        post_form.close()

    def test_post_poll_one_answer(self):
        post_page = self._to_post_page()
        post_form = post_page.get_post_form()
        poll_view = post_form.open_poll_creation()
        poll_view.write_question("question")
        poll_view.write_answer("answer_1", 0)
        self.assertRaises(WebDriverException, post_form.share)
        post_form.close()

    def test_post_poll_no_question(self):
        post_page = self._to_post_page()
        post_form = post_page.get_post_form()
        poll_view = post_form.open_poll_creation()
        poll_view.write_answer("answer_1", 0)
        poll_view.write_answer("answer_2", 1)
        self.assertRaises(WebDriverException, post_form.share)
        post_form.close()

    def test_post_poll(self):
        self._post_poll_to_status()
        profile_page = self._to_profile_page()
        status = profile_page.get_status()
        self.assertTrue(status.contains_poll())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_poll_vote_answer(self):
        self._post_poll_to_status()
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        variants = post.get_poll_variants()
        variants[0].set_voted()
        self.assertTrue(variants[0].is_voted())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_poll_change_answer_single_answer_submit(self):
        self._post_poll_to_status()
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        variants = post.get_poll_variants()
        variants[0].set_voted()
        variants[1].set_voted()

        self.assertFalse(variants[0].is_voted())
        self.assertTrue(variants[1].is_voted())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_poll_change_answer_single_answer_not_submit(self):
        self._post_poll_to_status()
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        variants = post.get_poll_variants()
        variants[0].set_voted()
        variants[1].set_voted(False)

        self.assertTrue(variants[0].is_voted())
        self.assertFalse(variants[1].is_voted())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_poll_unvote_single_answer_submit(self):
        self._post_poll_to_status()
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        variants = post.get_poll_variants()
        variants[0].set_voted()
        variants[0].set_unvoted()

        self.assertFalse(variants[0].is_voted())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_poll_unvote_single_answer_not_submit(self):
        self._post_poll_to_status()
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        variants = post.get_poll_variants()
        variants[0].set_voted()
        variants[0].set_unvoted(False)

        self.assertTrue(variants[0].is_voted())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_poll_two_variants_multi_answer(self):
        self._post_poll_to_status(False)
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        variants = post.get_poll_variants()
        variants[0].set_voted()
        variants[1].set_voted()

        self.assertTrue(variants[0].is_voted())
        self.assertTrue(variants[1].is_voted())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def _post_poll_to_status(self, is_single_answer=True):
        post_page = PostPage(self.driver)
        post_page.open()
        post_form = post_page.get_post_form()
        poll_view = post_form.open_poll_creation()
        poll_view.set_single_answer(is_single_answer)
        poll_view.write_question("question")
        poll_view.write_answer("answer_1", 0)
        poll_view.write_answer("answer_2", 1)
        post_form.input_post_text("msg")
        post_form.share()
