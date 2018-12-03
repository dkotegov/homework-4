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

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.email_sending_form.click_close_msg_sent_button()
        self.email_sending_form.click_incoming_emails_button()
        self.assertTrue(self.email_sending_form.checkMessageSentBySubject(self.SUBJECT))


class SendTestEmailToCorrectEmail(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_correct_recipient()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.assertTrue(self.email_sending_form.check_correct_recipient())


class SendTestEmailToGroupCorrectEmails(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_group_correct_recipients()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.assertTrue(self.email_sending_form.check_group_correct_recipients())


class SendTestEmailToWrongEmail(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_wrong_recipient()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.check_wrong_emails())


class SendTestEmailToGroupWrongEmails(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_group_wrong_recipients()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertTrue(self.email_sending_form.check_wrong_emails())


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

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.email_sending_form.click_close_msg_sent_button()
        self.email_sending_form.click_incoming_emails_button()
        self.assertTrue(self.email_sending_form.checkMessageSentBySubject(self.SUBJECT))


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

        self.assertTrue(self.email_sending_form.checkMessageSent())
        self.email_sending_form.click_close_msg_sent_button()
        self.email_sending_form.click_incoming_emails_button()
        self.assertTrue(self.email_sending_form.checkMessageSentBySubject(self.SUBJECT))


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

        self.assertTrue(self.email_sending_form.check_wrong_emails())
