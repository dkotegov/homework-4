from tests.main.main_base_test import MainBaseTest

from utils.random_strings import _randomString, _randomMail

import settings as s

DEFAULT_DIALOGUE = "support@liokor.ru"


class MessagesTest(MainBaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.page.delete_all_dialogues()

    def tearDown(self) -> None:
        self.page.delete_all_dialogues()

    def test_send_message_positive_HTML_in_title(self):
        title = "<p>Title</p> <strong>STRONG TITLE</strong>"
        new_title = "Title STRONG TITLE"

        recipient = s.USERNAME2 + "@liokor.ru"

        self._create_dialogue_with_name(recipient)
        self._send_message(title, _randomString(10))

        self.assertEqual(self.page.getLastYourMessageTitle(), new_title)

    def test_send_message_positive_HTML_in_body(self):
        body = "<p>body</p><strong>STRONG BODY</strong>normal body"
        recipient = s.USERNAME2 + "@liokor.ru"

        self._create_dialogue_with_name(recipient)
        self._send_message(_randomString(10), body)

        self.assertEqual(self.page.getLastYourMessageBody(), body)

    def test_send_message_negative_empty_body(self):
        recipient = s.USERNAME2 + "@liokor.ru"
        self._create_dialogue_with_name(recipient)
        messagesCount = self.page.getMessagesCount()

        self._send_message(_randomString(10), "")
        self.assertEqual(self.page.getMessagesCount(), messagesCount, "Messages count is not equal")

    def test_send_message_negative_recipient_not_exists(self):
        mail = _randomMail(15) + '.nonexistingdomainwolf123'
        self._create_dialogue_with_name(mail)
        self._send_message(_randomString(10), _randomString(20))

        self.assertTrue(self.page.is_popup_error())
        self.assertTrue(self.page.isMessageNotDelivered(), "Message delivered but mustn't be")
        self.assertTrue(self.page.is_popup_error(), "Message delivered but mustn't be")

        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    def test_delete_message(self):
        recipient = s.USERNAME2 + "@liokor.ru"

        self._create_dialogue_with_name(recipient)
        self._send_message(_randomString(15), _randomString(100))

        self.page.clickDeleteLastMessage(your=True)
        self.page.submitOverlay()

        self.assertTrue(self.page.is_popup_success())
        self.page.wait_until(lambda d: self.page.getMessagesCount() == 0)

    def test_message_body_saved_after_refresh(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail)
        body = "Message body\nWith one string break."
        self.page.setMessageBody(body)

        self.driver.refresh()

        self.assertEqual(self.page.getMessageBody(), body, "Message body was not loaded")

    def test_load_message_body_after_dialogues_checkout(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail)
        body = "Message body\nWith one string break."
        self.page.setMessageBody(body)
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.assertEqual(self.page.getMessageBody(), "", "Can't checkout to default dialogue")
        self.page.clickDialogue(mail)
        self.assertEqual(self.page.getMessageBody(), body, "Message body was not loaded")
