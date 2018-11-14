# coding=utf-8
from tests.letter_functions.base_send import BaseSend


class ImportantMarkTest(BaseSend):
    def test(self):
        BaseSend.test(self)
        # Тестирование отметки важного сообщения.
        self.functions_form.open_writing_letter()
        self.functions_form.set_destionation_email()
        self.functions_form.click_on_subject_field()
        self.functions_form.write_some_text("Important")
        self.functions_form.click_on_message_field()
        self.functions_form.write_some_text("Important mark letter Test")
        self.functions_form.click_on_important_mark()
        self.functions_form.click_send_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_sent()
        self.assertEqual(self.functions_form.check_letter_by_subj("Important"), True)

        # Тестирование отметки сохраненного важного сообщения.
        self.functions_form.open_writing_letter()
        self.functions_form.set_destionation_email()
        self.functions_form.click_on_subject_field()
        self.functions_form.write_some_text("ImportantS")
        self.functions_form.click_on_message_field()
        self.functions_form.write_some_text("Important mark letter Test")
        self.functions_form.click_on_important_mark()
        self.functions_form.click_save_button()
        self.functions_form.click_cancel_button()
        self.functions_form.show_message_draft()
        self.assertEqual(self.functions_form.check_letter_by_subj("ImportantS"), True)


class NotificationMarkTest(BaseSend):
    def test(self):
        # Тестирование отметки сообщения с оповещением
        BaseSend.test(self)
        self.functions_form.open_writing_letter()
        self.functions_form.set_destionation_email()
        self.functions_form.click_on_subject_field()
        self.functions_form.write_some_text("Notified")
        self.functions_form.click_on_message_field()
        self.functions_form.write_some_text("Notify mark letter Test")
        self.functions_form.click_on_notification_mark()
        self.functions_form.click_send_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_sent()
        self.assertEqual(self.functions_form.check_letter_by_subj("Notified"), True)

        # Тестирование сохранения отметки сообщения с оповещением
        self.functions_form.open_writing_letter()
        self.functions_form.set_destionation_email()
        self.functions_form.click_on_subject_field()
        self.functions_form.write_some_text("NotifiedS")
        self.functions_form.click_on_message_field()
        self.functions_form.write_some_text("Notify mark letter Test")
        self.functions_form.click_on_notification_mark()
        self.functions_form.click_save_button()
        self.functions_form.click_cancel_button()
        self.functions_form.show_message_draft()
        self.assertEqual(self.functions_form.check_letter_by_subj("NotifiedS"), True)

class ReminderMarkTest(BaseSend):
    def test(self):
        self.functions_form.open_writing_letter()



class DelayedMarkTest(BaseSend):
    def test(self):
        self.functions_form.open_writing_letter()


