# coding=utf-8
from tests.letter_functions.base_send import BaseSend


class ImportantMarkTest(BaseSend):
    def test(self):
        BaseSend.test(self)
        # Тестирование простой отметки важного сообщения.
        self.functions_form.open_writing_letter()
        self.functions_form.set_destionation_email()
        # self.functions_form.write_some_text("Important letter Test")
        self.functions_form.click_on_important_mark()
        self.functions_form.click_send_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_sent()
        self.assertEqual(self.functions_form.check_important_letter(), True)

        # Тестирование простой отметки сохраненного важного сообщения.
        self.functions_form.open_writing_letter()
        self.functions_form.set_destionation_email()
        # self.functions_form.write_some_text("Important letter Test")
        self.functions_form.click_on_important_mark()
        self.functions_form.click_save_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_draft()
        self.assertEqual(self.functions_form.check_important_letter(), True)


class NotificationMarkTest(BaseSend):
    def test(self):
        BaseSend.test(self)
        self.functions_page.redirectQA()
        self.functions_form.open_writing_letter()
        self.functions_form.set_destionation_email()
        self.functions_form.click_on_notification_mark()
        self.functions_form.click_send_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_sent()
