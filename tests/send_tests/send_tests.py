# coding=utf-8

from tests.send_tests.base_send import BaseSend


class SendTestEmailToMe(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_destionation_email()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertEqual(self.email_sending_form.checkMessageSent(), True)
        self.email_sending_form.click_close_msg_sent_button()
        self.email_sending_form.click_incoming_emails_button()
        self.assertEqual(self.email_sending_form.checkMessageSentBySubject(self.SUBJECT), True)


class SendTestEmailToCorrectEmail(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_correct_recipient()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertEqual(self.email_sending_form.checkMessageSent(), True)
        self.assertEqual(self.email_sending_form.check_correct_recipient(), True)


class SendTestEmailToGroupCorrectEmails(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_group_correct_recipients()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertEqual(self.email_sending_form.checkMessageSent(), True)
        self.assertEqual(self.email_sending_form.check_group_correct_recipients(), True)


class SendTestEmailToWrongEmail(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_wrong_recipient()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertEqual(self.email_sending_form.check_wrong_emails(), True)


class SendTestEmailToGroupWrongEmails(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_group_wrong_recipients()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertEqual(self.email_sending_form.check_wrong_emails(), True)


class SendTestEmailToMeWithCopy(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_destionation_email()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_copy_button()
        self.email_sending_form.set_copy_email()
        self.email_sending_form.click_send_button()

        self.assertEqual(self.email_sending_form.checkMessageSent(), True)
        self.email_sending_form.click_close_msg_sent_button()
        self.email_sending_form.click_incoming_emails_button()
        self.assertEqual(self.email_sending_form.checkMessageSentBySubject(self.SUBJECT), True)


class SendTestEmailToCorrectEmailWithCopy(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_correct_recipient()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_copy_button()
        self.email_sending_form.set_copy_email_correct_recipient()
        self.email_sending_form.click_send_button()

        self.assertEqual(self.email_sending_form.checkMessageSent(), True)
        self.email_sending_form.click_close_msg_sent_button()
        self.email_sending_form.click_incoming_emails_button()
        self.assertEqual(self.email_sending_form.checkMessageSentBySubject(self.SUBJECT), True)


class SendTestEmailToGroupWrongEmailsWithCopy(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_group_wrong_recipients()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_copy_button()
        self.email_sending_form.set_copy_email()
        self.email_sending_form.click_send_button()

        self.assertEqual(self.email_sending_form.check_wrong_emails(), True)
