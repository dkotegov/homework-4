# coding=utf-8
from tests.letter_functions.base_send import BaseSend


class ImportantMarkTest(BaseSend):
    def test(self):
        BaseSend.test(self)
        # Тестирование отметки важного сообщения.
        self.writeLetter("Important", "Important mark letter Test")
        self.functions_form.click_on_important_mark()
        self.functions_form.click_send_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_incoming()
        self.assertTrue(self.functions_form.check_letter_by_subj("Important"))

        self.functions_page.redirectQA()

        # Тестирование отметки сохраненного важного сообщения.
        self.writeLetter("ImportantS", "Important mark letter Test")
        self.functions_form.click_on_important_mark()
        self.functions_form.click_save_button()
        # self.functions_form.click_cancel_button()
        self.functions_form.click_cancel_writing_message()
        self.functions_form.show_message_draft()
        self.assertTrue(self.functions_form.check_letter_by_subj("ImportantS"))


class NotificationMarkTest(BaseSend):
    def test(self):
        # Тестирование отметки сообщения с оповещением
        BaseSend.test(self)
        self.writeLetter("Notified", "Notify mark letter Test")
        self.functions_form.click_on_notification_mark()
        self.functions_form.click_send_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_incoming()
        self.assertTrue(self.functions_form.check_letter_by_subj("Notified"))

        self.functions_page.redirectQA()

        # Тестирование сохранения отметки сообщения с оповещением
        self.writeLetter("NotifiedS", "Notify mark letter Test")
        self.functions_form.click_on_notification_mark()
        self.functions_form.click_save_button()
        # self.functions_form.click_cancel_button()
        self.functions_form.click_cancel_writing_message()
        self.functions_form.show_message_draft()
        self.assertTrue(self.functions_form.check_letter_by_subj("NotifiedS"))


class ReminderMarkTest(BaseSend):
    def test(self):
        # Тестирование отметки сообщения с оповещением
        BaseSend.test(self)
        self.writeLetter("Remind", "Remind mark letter Test")
        self.functions_form.click_on_reminder_mark()
        self.functions_form.click_send_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_incoming()
        self.assertTrue(self.functions_form.check_letter_by_subj("Remind"))

        self.functions_page.redirectQA()

        # Тестирование сохранения отметки сообщения с оповещением
        self.writeLetter("RemindS", "Remind mark letter Test")
        self.functions_form.click_on_reminder_mark()
        self.functions_form.click_save_button()
        # self.functions_form.click_cancel_button()
        self.functions_form.click_cancel_writing_message()
        self.functions_form.show_message_draft()
        self.assertTrue(self.functions_form.check_letter_by_subj("RemindS"))


class DelayedMarkTest(BaseSend):
    def test(self):
        # Тестирование отметки сообщения с отложенным отправлением
        BaseSend.test(self)
        self.writeLetter("Delayed", "Delayed mark letter Test")
        self.functions_form.click_on_delayed_mark()
        self.functions_form.click_send_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_sent()
        self.assertTrue(self.functions_form.check_letter_by_subj("Delayed"))

        self.functions_page.redirectQA()

        # Тестирование сохранения сообщения с отложенным отправлением
        self.writeLetter("DelayedS", "Delayed mark letter Test")
        self.functions_form.click_on_delayed_mark()
        self.functions_form.click_save_button()
        # self.functions_form.click_cancel_button()
        self.functions_form.click_cancel_writing_message()
        self.functions_form.show_message_draft()
        self.assertTrue(self.functions_form.check_letter_by_subj("DelayedS"))


class CrossFuncsTest(BaseSend):
    def test(self):
        # Тестирование отметки сообщения с разными функциями
        BaseSend.test(self)

        self.writeLetter("CrossFuncs", "CrossFuncs mark letter Test")
        self.functions_form.click_on_notification_mark()
        self.functions_form.click_on_important_mark()
        self.functions_form.click_on_delayed_mark()
        self.functions_form.click_on_reminder_mark()
        self.functions_form.click_send_button()
        self.functions_form.closeMessageSent()
        self.functions_form.show_message_sent()
        self.assertTrue(self.functions_form.check_letter_by_subj("CrossFuncs"))

        self.functions_page.redirectQA()

        # Тестирование сохранения сообщения с разными функциями

        self.writeLetter("CrossFuncsS", "CrossFuncs mark letter Test")
        self.functions_form.click_on_notification_mark()
        self.functions_form.click_on_important_mark()
        self.functions_form.click_on_delayed_mark()
        self.functions_form.click_on_reminder_mark()
        self.functions_form.click_save_button()
        # self.functions_form.click_cancel_button()
        self.functions_form.click_cancel_writing_message()
        # self.functions_form.closeMessageSent()
        self.functions_form.show_message_draft()
        self.assertTrue(self.functions_form.check_letter_by_subj("CrossFuncsS"))


class TemplateTest(BaseSend):
    def test(self):
        # Тестирование отметки сообщения с отложенным отправлением
        BaseSend.test(self)
        self.writeLetter("Template", "Template mark letter Test")
        self.functions_form.click_on_notification_mark()
        self.functions_form.click_on_important_mark()
        self.functions_form.click_on_delayed_mark()
        self.functions_form.click_template_mark()
        self.functions_form.click_save_template()
        self.functions_form.click_template_mark()
        self.assertEqual(self.functions_form.get_first_template(), "Template")
