from tests.cases.base import TestAuthorized
from tests.pages.chat import ChatPage


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = ChatPage(self.driver)

    def _send_message(self, name, text, **kwargs):
        self.page.form_list.search_user(name)
        self.assertFalse(self.page.form_list.get_error(), "Got unexpected error")

        self.assertEqual(
            self.page.form_concrete.get_companion_name(), name, "Wrong companion name"
        )
        return self.page.form_concrete.send_message_confirmed(text, **kwargs)

    def test_send_plain_to_existed(self):
        name, text = "testTest", "43424342"
        from_me, got_text = self._send_message(name, text)
        self.assertTrue(from_me, "Message not from me")
        self.assertEqual(got_text, text, "Got wrong message")

    def test_search_non_existent(self):
        name = "odjwedjfdjefce"
        self.page.form_list.search_user(name)
        err = self.page.form_list.get_error(timeout=5)
        self.assertNotEqual(err, "")

    def test_forgot_to_print_username(self):
        name = ""
        self.page.form_list.search_user(name)
        err = self.page.form_list.get_error(timeout=5)
        self.assertNotEqual(err, "")

    def test_send_empty_message(self):
        name = "testTest"
        text = ""
        try:
            self._send_message(name, text, timeout=3)
            self.fail("There must not any message-list alteration be found, but smt has changed")
        except TimeoutError:
            return

    def test_send_smiles_only(self):
        name, text = "testTest", "😁😅😊😋😎"
        from_me, got_text = self._send_message(
            name, text, printer=self.page.form_concrete.enter_smiles
        )
        self.assertTrue(from_me, "Got message not from me")
        self.assertEqual(got_text, text, "Got wrong message")

    def test_send_smiles_and_text(self):
        name, text = "testTest", "😁😅😊kokoko😋😎"
        from_me, got_text = self._send_message(
            name, text, printer=self.page.form_concrete.enter_smiles
        )
        self.assertTrue(from_me, "Got message not from me")
        self.assertEqual(got_text, text, "Got wrong message")

    def test_open_saved_dialog(self):
        name = "ForTest"
        self._send_message(name, "setup")
        self.page.open()
        self.page.form_list.open_dialog_from_list(name)
        self.page.form_concrete.wait_for_load()
        companion = self.page.form_concrete.get_companion_name()
        self.assertEqual(companion, name, "Wrong companion name")

    def test_send_message_check_update_chats_list(self):
        name, text = "testTest", "fkererfrfe"
        self._send_message(name, text)
        self.driver.refresh()
        self.page.form_list.wait_for_load()
        self.assertEqual(self.page.form_list.check_dialog(name), text)
