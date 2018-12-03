# coding=utf-8

from tests.send_tests.base_send import BaseSend

# Тестирование отправки сообщения самому себе
class SendEmailToMeTest(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()
        self.email_sending_form.set_destionation_email()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.email_sending_form.click_close_msg_sent_button()
        self.email_sending_form.click_incoming_emails_button()
        self.assertTrue(self.email_sending_form.checkMessageSentBySubject(self.SUBJECT))

# Тестирование отправки сообщения на существующий email
class SendEmailToCorrectEmailTest(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()
        self.email_sending_form.set_correct_recipient()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.assertTrue(self.email_sending_form.check_correct_recipient())

# Тестирование отправки сообщения на группу существующих email'ов
class SendEmailToGroupCorrectEmailsTest(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()
        self.email_sending_form.set_group_correct_recipients()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.assertTrue(self.email_sending_form.check_group_correct_recipients())

# Тестирование отправки сообщения на не существующий email
class SendEmailToWrongEmailTest(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()
        self.email_sending_form.set_wrong_recipient()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.check_wrong_emails())

# Тестирование отправки сообщения на группу не существующих email'ов
class SendEmailToGroupWrongEmailsTest(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()
        self.email_sending_form.set_group_wrong_recipients()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.check_wrong_emails())

# Тестирование отправки сообщения самому себе 
# с копией для самого себя
class SendEmailToMeWithCopyTest(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()
        self.email_sending_form.set_destionation_email()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_copy_button()
        self.email_sending_form.set_copy_email()
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.email_sending_form.click_close_msg_sent_button()
        self.email_sending_form.click_incoming_emails_button()
        self.assertTrue(self.email_sending_form.checkMessageSentBySubject(self.SUBJECT))

# Тестирование отправки сообщения существующий email 
# с копией для самого себя
class SendEmailToCorrectEmailWithCopyTest(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()
        self.email_sending_form.set_correct_recipient()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_copy_button()
        self.email_sending_form.set_copy_email_correct_recipient()
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.email_sending_form.click_close_msg_sent_button()
        self.email_sending_form.click_incoming_emails_button()
        self.assertTrue(self.email_sending_form.checkMessageSentBySubject(self.SUBJECT))

# Тестирование отправки сообщения на группу не существующий email'ов
# с копией для самого себя
class SendEmailToGroupWrongEmailsWithCopyTest(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()
        self.email_sending_form.set_group_wrong_recipients()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_copy_button()
        self.email_sending_form.set_copy_email()
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.check_wrong_emails())
