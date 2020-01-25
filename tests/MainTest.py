from pages.MainPage import MainPage
from BasicTest import BasicTest

from user.User import User


class MainTest(BasicTest):

    def setUp(self):
        super(MainTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.auth()
        self.main_page.hide_app_loader()

    def check_first_letter(self, subject, text):
        actual_subject = self.main_page.letter_manager.letter_selector.get_first_letter_subject()
        actual_text = self.main_page.letter_manager.letter_selector.get_first_letter_text()
        self.assertEqual(subject, actual_subject)
        self.assertEqual(text, actual_text)

    def test_receive_new_letter(self):
        SUBJECT = 'Subject_receive_new_letter'
        TEXT = 'Text_receive_new_letter'
        self.main_page.letter_manager.write_letter(self.login, SUBJECT, TEXT)
        self.check_first_letter(SUBJECT, TEXT)

    def test_receive_new_letter_from_another_account(self):
        SUBJECT = 'Subj_receive_new_letter_from_another_account'
        TEXT = 'Txt_receive_new_letter_from_another_account'

        receiver = User(self.login2, self.password2)

        self.main_page.letter_manager.write_letter(
            receiver.login, SUBJECT, TEXT)
        self.main_page.relogin(receiver.login, receiver.password)

        self.check_first_letter(SUBJECT, TEXT)

    def test_reading_letter(self):
        SUBJECT = 'Subject_reading_letter'
        TEXT = 'Text_reading_letter'
        self.main_page.letter_manager.write_letter(self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_selector.set_first_letter_read_status(
            True)
        self.assertTrue(
            self.main_page.letter_manager.letter_selector.get_first_letter_read_status())

    def test_remove_letter(self):
        SUBJECT = 'Subject_remove_letter'
        TEXT = 'Text_remove_letter'
        self.main_page.letter_manager.write_letter(self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.remove_first_letter()

        self.main_page.navigation_manager.go_to_trash()
        self.main_page.letter_manager.letter_selector.get_first_letter_subject()
        self.main_page.letter_manager.letter_selector.get_first_letter_text()
        self.check_first_letter(SUBJECT, TEXT)

    def test_restore_letter(self):
        SUBJECT = 'Subject_restore_letter'
        TEXT = 'Text_restore_letter'
        self.main_page.letter_manager.write_letter(self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.remove_first_letter()

        self.main_page.navigation_manager.go_to_trash()
        self.main_page.letter_manager.restore_first_letter()
        # Go back (to check for a letter in the inbox folder)
        self.main_page.navigation_manager.go_to_inbox()

        self.check_first_letter(SUBJECT, TEXT)

    def test_check_sent_new_letter(self):
        SUBJECT = 'Subject_check_sent_new_letter'
        TEXT = 'Text_check_sent_new_letter'
        self.main_page.letter_manager.write_letter(self.login, SUBJECT, TEXT)
        self.main_page.navigation_manager.go_to_sent_letters_folder()
        self.main_page.letter_manager.letter_selector.get_first_letter_subject()
        self.main_page.letter_manager.letter_selector.get_first_letter_text()
        self.check_first_letter(SUBJECT, TEXT)

    def test_open_letter(self):
        SUBJECT = 'Subject_opened_letter'
        TEXT = 'Text_opened_letter'
        self.main_page.letter_manager.write_letter(self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_selector.open_first_letter()
        actual_subject = self.main_page.letter_manager.letter_selector.get_opened_letter_subject()
        actual_text = self.main_page.letter_manager.letter_selector.get_opened_letter_text()
        self.assertEqual(SUBJECT, actual_subject)
        self.assertEqual(TEXT, actual_text)

    def test_reply_letter(self):
        SUBJECT = 'Subject_reply_letter'
        TEXT = 'Text_reply_letter'
        replied_text = 'Replied TEXT'

        first_user = User(self.login, self.password)
        receiver = User(self.login2, self.password2)

        self.main_page.letter_manager.write_letter(
            receiver.login, SUBJECT, TEXT)

        self.main_page.relogin(receiver.login, receiver.password)
        self.main_page.letter_manager.reply_letter(replied_text)

        self.main_page.relogin(first_user.login, first_user.password)
        self.main_page.letter_manager.letter_selector.open_first_letter()
        actual_replied_text = self.main_page.letter_manager.letter_selector.get_replied_letter_text()
        self.assertEqual(replied_text, actual_replied_text)

    def test_write_many_receivers(self):
        SUBJECT = 'Subject_write_many_receivers'
        TEXT = 'Text_write_many_receivers'
        receivers = [
            User(self.login, self.password),
            User(self.login2, self.password2),
        ]
        receivers_emails = [receiver.login for receiver in receivers]
        self.main_page.letter_manager.write_letter_many_receivers(
            receivers_emails, SUBJECT, TEXT)
        for receiver in receivers:
            self.main_page.relogin(receiver.login, receiver.password)
            self.check_first_letter(SUBJECT, TEXT)

    def test_bold_letter(self):
        SUBJECT = 'Subject_bold_letter'
        TEXT = 'Text_bold_letter'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_bold_text()
        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()

        bold_element = self.main_page.letter_manager.letter_selector.get_bold()
        self.assertEqual(TEXT, bold_element.text)

    def test_font_title1_letter(self):
        SUBJECT = 'Subject_font_title1_letter_letter'
        TEXT = 'font title1 letter'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_font_text_title1()

        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()
        element = self.main_page.letter_manager.letter_selector.get_font_text_title1()
        self.assertEqual(TEXT, element.text)

    def test_alignment_text_center(self):
        SUBJECT = 'Subject_alignment_text_center'
        TEXT = 'alignment_text_center'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_alignment_text_center()

        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()
        element = self.main_page.letter_manager.letter_selector.get_alignment_text_center()
        self.assertEqual(TEXT, element.text)

    def test_indent_text_plus(self):
        SUBJECT = 'Subject_alignment_text_center'
        TEXT = 'alignment_text_indent_text_plus'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_indent_text_plus()

        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()
        element = self.main_page.letter_manager.letter_selector.get_indent_text()
        self.assertEqual(TEXT, element.text)

    def test_indent_text_minus(self):
        SUBJECT = 'Subject_alignment_indent_text_minus'
        TEXT = 'alignment_text_indent_text_minus'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_indent_text_minus()

        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()
        element = self.main_page.letter_manager.letter_selector.get_indent_text()
        self.assertEqual(TEXT, element.text)

    def test_italic_letter(self):
        SUBJECT = 'Subject_italic_letter'
        TEXT = 'Text_italic_letter'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_italic_text()
        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()

        italic_element = self.main_page.letter_manager.letter_selector.get_italic()
        self.assertEqual(TEXT, italic_element.text)

    def test_underline_letter(self):
        SUBJECT = 'Subject_underline_letter'
        TEXT = 'Text_underline_letter'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_underline_text()
        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()

        underline_element = self.main_page.letter_manager.letter_selector.get_underline()
        self.assertEqual(TEXT, underline_element.text)

    def test_strike_through_letter(self):
        SUBJECT = 'Subject_strike_through_letter'
        TEXT = 'Text_strike_through_letter'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_strike_through_text()
        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()

        strike_through_element = self.main_page.letter_manager.letter_selector.get_strike_through()
        self.assertEqual(TEXT, strike_through_element.text)

    def test_text_color(self):
        SUBJECT = 'Subject_text_color'
        TEXT = 'Text_color'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_text_color_purple()
        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()
        element = self.main_page.letter_manager.letter_selector.get_text_color_purple()
        self.assertEqual(TEXT, element.text)
        style = 'color: rgb(231, 0, 145);'
        self.assertEqual(style, element.get_attribute(
            'style').encode('utf-8', errors='ignore'))

    def test_background_color(self):
        SUBJECT = 'Subject_background_color'
        TEXT = 'Background_color'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_background_color_blue()
        self.main_page.letter_manager.send_letter()
        self.main_page.letter_manager.letter_selector.open_first_letter()
        element = self.main_page.letter_manager.letter_selector.get_background_color_blue()
        self.assertEqual(TEXT, element.text)
        style = 'background-color: rgb(110, 228, 254);'
        self.assertEqual(style, element.get_attribute(
            'style').encode('utf-8', errors='ignore'))

    def test_back_formating(self):
        SUBJECT = 'Subject preview letter'
        TEXT = 'Teeeeext'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_bold_text()

        bold_text = self.main_page.letter_manager.letter_selector.get_bold_text()

        self.main_page.letter_manager.letter_writer.click_preview_button()

        not_bold_text = self.main_page.letter_manager.letter_selector.get_not_bold_text()
        self.assertEqual(TEXT, bold_text)
        self.assertEqual(TEXT, not_bold_text)

    def test_clear_formating(self):
        SUBJECT = 'Subject letter'
        TEXT = 'All_kind_formating'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.set_italic_text()
        self.main_page.letter_manager.letter_writer.set_underline_text()
        self.main_page.letter_manager.letter_writer.set_bold_text()
        self.main_page.letter_manager.letter_writer.set_strike_through_text()

        self.main_page.letter_manager.letter_writer.click_clear_all_button()
        unformating_text = self.main_page.letter_manager.letter_selector.get_unformating_text()
        self.assertEqual(TEXT, unformating_text)

    def test_insert_link(self):
        SUBJECT = "Hello"
        TEXT = 'Welcome to the 4th semester of Tehnopark MailRu\n'
        self.main_page.letter_manager.write_letter_without_sending(
            self.login, SUBJECT, TEXT)
        self.main_page.letter_manager.letter_writer.click_link_button()
        txt_link = self.main_page.letter_manager.letter_writer.text_link
        link = self.main_page.letter_manager.letter_writer.link
        self.main_page.letter_manager.letter_writer.enter_link(link)
        self.main_page.letter_manager.letter_writer.enter_text_link(txt_link)
        self.main_page.letter_manager.letter_writer.click_confirm_link()

        actual_text = self.main_page.letter_manager.letter_selector.get_link_text()
        self.assertEqual(txt_link, actual_text)
