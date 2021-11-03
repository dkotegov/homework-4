from tests.main.main_base_test import MainBaseTest

from tests.main.utils import _randomString, _randomMail

import settings as s

DEFAULT_DIALOGUE = "support@liokor.ru"


class MessagesTest(MainBaseTest):
    def test_send_message_positive(self):
        self._send_message_positive(_randomString(15), _randomString(100))

    def test_send_message_positive_special_symbols(self):
        self._send_message_positive("!@)(:?*!&cz@$^@(!*#)*(@&^", "(!@*#&*^&@$^(::;*!@#&%!(@^#%!@*#%^&#%*&!@#^&6IA")

    def test_send_message_positive_HTML_in_title(self):
        title = "<p>Title</p> <strong>STRONG TITLE</strong>"
        recipient = s.USERNAME2 + "@liokor.ru"
        self._send_message_positive(title, _randomString(10), recipient, delete=False)
        self.assertEqual(self.page.getLastYourMessageTitle(), "Title STRONG TITLE")
        self.page.clickDeleteDialogue(recipient)
        self.page.submitOverlay()

    def test_send_message_positive_HTML_in_body(self):
        body = "<p>body</p><strong>STRONG BODY</strong>normal body"
        recipient = s.USERNAME2 + "@liokor.ru"
        self._send_message_positive(_randomString(10), body, recipient, delete=False)
        self.assertEqual(self.page.getLastYourMessageBody(), body)
        self.page.clickDeleteDialogue(recipient)
        self.page.submitOverlay()

    def test_send_message_negative_empty_body(self):
        recipient = s.USERNAME2 + "@liokor.ru"
        self._create_dialogue_with_name(recipient, delete=False)
        messagesCount = self.page.getMessagesCount()
        self._send_message(_randomString(10), "")
        self.assertEqual(self.page.getMessagesCount(), messagesCount, "Messages count is not equal")
        self.page.clickDeleteDialogue(recipient)
        self.page.submitOverlay()

    def test_send_message_negative_recipient_not_exists(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail, delete=False)
        self._send_message(_randomString(10), _randomString(20))
        self.assertTrue(self.page.isMessageNotDelivered(), "Message delivered but mustn't be")
        self.assertFalse(self.page.is_popup_success(), "Message delivered but mustn't be")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    def test_delete_message(self):
        recipient = s.USERNAME2 + "@liokor.ru"
        self._send_message_positive(_randomString(15), _randomString(100), recipient, delete=False)
        messagesCount = self.page.getMessagesCount()
        self.page.clickDeleteLastMessage(your=True)
        self.page.submitOverlay()
        self.assertEqual(self.page.getMessagesCount(), messagesCount-1, "Message wasn't deleted")
        self.page.clickDeleteDialogue(recipient)
        self.page.submitOverlay()

    def test_load_message_body_after_refresh(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail, delete=False)
        body = "Message body\nWith one string break."
        self.page.setMessageBody(body)
        self.driver.refresh()
        self.assertEqual(self.page.getMessageBody(), body, "Message body was not loaded")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    def test_load_message_body_after_dialogues_checkout(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail, delete=False)
        body = "Message body\nWith one string break."
        self.page.setMessageBody(body)
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.assertEqual(self.page.getMessageBody(), "", "Can't checkout to default dialogue")
        self.page.clickDialogue(mail)
        self.assertEqual(self.page.getMessageBody(), body, "Message body was not loaded")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    # TODO: autocomplete message theme (надо отправить сообщение себе и посмотреть, какая тема будет при открытии
    #  диалога. Там приколы с Re[number]: тема
