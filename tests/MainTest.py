from pages.MainPage import MainPage
from BasicTest import BasicTest

from user.User import User

import time

import random

class MainTest(BasicTest):

    def setUp(self):
        super(MainTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.auth()
        self.main_page.hide_app_loader()

    def test_receive_new_letter(self):
        self.subject = self.add_random_number('Subject_receive_new_letter ')
        TEXT = 'Text_receive_new_letter'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, self.subject, TEXT)
        letter_manager.letter_selector.find_letter_subject_real(self.subject)

    def test_receive_new_letter_from_another_account(self):
        self.subject = self.add_random_number('Subj_receive_from_another_account ')
        TEXT = 'Txt_receive_from_another_account'

        receiver = User(self.login2, self.password2)
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(receiver.login, self.subject, TEXT)
        self.main_page.relogin(receiver.login, receiver.password)

        letter_manager.letter_selector.find_letter_subject_real(self.subject)

    def test_reading_letter(self):
        self.subject = self.add_random_number('Subject_reading_letter ')
        TEXT = 'Text_reading_letter'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, self.subject, TEXT)
        letter_manager.letter_selector.set_letter_read_status(self.subject, True)
        self.assertTrue(letter_manager.letter_selector.get_letter_read_status(self.subject))

    def test_remove_letter(self):
        self.subject = self.add_random_number('Subject_remove_letter ')
        TEXT = 'Text_remove_letter'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, self.subject, TEXT)
        letter_manager.remove_letter(self.subject)

        self.main_page.navigation_manager.go_to_trash()
        letter_manager.letter_selector.find_letter_subject_real(self.subject)
        # tearDown shouldn't remove anything!
        self.subject = ''

    def test_restore_letter(self):
        self.subject = self.add_random_number('Subject_restore_letter ')
        TEXT = 'Text_restore_letter'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, self.subject, TEXT)
        letter_manager.remove_letter(self.subject)

        self.main_page.navigation_manager.go_to_trash()
        letter_manager.restore_letter(self.subject)
        # Go back (to check for a letter in the inbox folder)
        self.main_page.navigation_manager.go_to_inbox()

        letter_manager.letter_selector.find_letter_subject_real(self.subject)

    def test_check_sent_new_letter(self):
        self.subject = self.add_random_number('Subject_check_sent_new_letter ')
        TEXT = 'Text_check_sent_new_letter'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, self.subject, TEXT)
        self.main_page.navigation_manager.go_to_sent_letters_folder()
        letter_manager.letter_selector.find_letter_subject_real(self.subject)

    def test_open_letter(self):
        self.subject = self.add_random_number('Subject_opened_letter ')
        TEXT = self.add_random_number('Text_opened_letter_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, self.subject, TEXT)
        letter_manager.letter_selector.open_letter(self.subject)
        actual_subject = self.main_page.letter_manager.letter_selector.get_opened_letter_subject()
        actual_text = self.main_page.letter_manager.letter_selector.get_opened_letter_text()
        self.assertEqual(self.subject, actual_subject)
        self.assertEqual(TEXT, actual_text)

    def test_reply_letter(self):
        self.subject = self.add_random_number('Subject_reply_letter ')
        text = 'Text_reply_letter'
        replied_text = self.add_random_number('Replied text ')

        first_user = User(self.login, self.password)
        receiver = User(self.login2, self.password2)
        letter_manager = self.main_page.letter_manager
    
        letter_manager.write_letter(receiver.login, self.subject, text)

        self.main_page.relogin(receiver.login, receiver.password)
        letter_manager.reply_letter(self.subject, replied_text)

        self.main_page.relogin(first_user.login, first_user.password)
        letter_manager.letter_selector.open_letter(self.subject)
        actual_replied_text = self.main_page.letter_manager.letter_selector.get_replied_letter_text()
        self.assertEqual(replied_text, actual_replied_text)
        
        self.main_page.navigation_manager.go_to_inbox()
        self.main_page.letter_manager.remove_letter(self.subject)
        
        self.main_page.relogin(receiver.login, receiver.password)

    def test_write_many_receivers(self):
        self.subject = self.add_random_number('Subject_write_many_receivers ')
        text = 'Text_write_many_receivers'
        receivers = [
            User(self.login, self.password),
            User(self.login2, self.password2),
        ]
        receivers_emails = [receiver.login for receiver in receivers]
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_many_receivers(
            receivers_emails, self.subject, text)
        for receiver in receivers:
            self.main_page.relogin(receiver.login, receiver.password)
            letter_manager.letter_selector.find_letter_subject_real(self.subject)
            # For the last receiver we use tearDown
            if receiver != receivers[-1]:
                self.main_page.letter_manager.remove_letter(self.subject)

    def test_bold_letter(self):
        self.subject = self.add_random_number('Subject_bold_letter ')
        TEXT = self.add_random_number('Text_bold_letter_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_bold_text()
        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)

        bold_element = letter_manager.letter_selector.get_bold()
        self.assertEqual(TEXT, bold_element.text)

    def test_font_title1_letter(self):
        self.subject = self.add_random_number('Subject_font_title1_letter_letter_')
        TEXT = self.add_random_number('font title1 letter ')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_font_text_title1()

        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)
        element = letter_manager.letter_selector.get_font_text_title1()
        self.assertEqual(TEXT, element.text)

    def test_alignment_text_center(self):
        self.subject = self.add_random_number('Subject_alignment_text_center_')
        TEXT = self.add_random_number('alignment_text_center_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_alignment_text_center()

        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)
        element = letter_manager.letter_selector.get_alignment_text_center()
        self.assertEqual(TEXT, element.text)

    def test_indent_text_plus(self):
        self.subject = self.add_random_number('Subject_alignment_text_center_')
        TEXT = self.add_random_number('alignment_text_indent_text_plus_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_indent_text_plus()

        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)
        element = letter_manager.letter_selector.get_indent_text()
        self.assertEqual(TEXT, element.text)

    def test_indent_text_minus(self):
        self.subject = self.add_random_number('Subject_alignment_indent_text_minus_')
        TEXT = self.add_random_number('alignment_text_indent_text_minus_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_indent_text_minus()

        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)
        element = letter_manager.letter_selector.get_indent_text()
        self.assertEqual(TEXT, element.text)

    def test_italic_letter(self):
        self.subject = self.add_random_number('Subject_italic_letter_')
        TEXT = self.add_random_number('Text_italic_letter_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_italic_text()
        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)

        italic_element = letter_manager.letter_selector.get_italic()
        self.assertEqual(TEXT, italic_element.text)

    def test_underline_letter(self):
        self.subject = self.add_random_number('Subject_underline_letter_')
        TEXT = self.add_random_number('Text_underline_letter_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_underline_text()
        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)

        underline_element = letter_manager.letter_selector.get_underline()
        self.assertEqual(TEXT, underline_element.text)

    def test_strike_through_letter(self):
        self.subject = self.add_random_number('Subject_strike_through_letter_')
        TEXT = self.add_random_number('Text_strike_through_letter_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_strike_through_text()
        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)

        strike_through_element = letter_manager.letter_selector.get_strike_through()
        self.assertEqual(TEXT, strike_through_element.text)

    def test_text_color(self):
        self.subject = self.add_random_number('Subject_text_color_')
        TEXT = self.add_random_number('Text_color_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_text_color_purple()
        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)
        element = letter_manager.letter_selector.get_text_color_purple()
        self.assertEqual(TEXT, element.text)
        STYLE = 'color: rgb(231, 0, 145);'
        self.assertEqual(STYLE, element.get_attribute('style').encode('utf-8', errors='ignore'))

    def test_background_color(self):
        self.subject = self.add_random_number('Subject_background_color_')
        TEXT = self.add_random_number('Background_color_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_background_color_blue()
        letter_manager.send_letter()
        letter_manager.letter_selector.open_letter(self.subject)
        element = letter_manager.letter_selector.get_background_color_blue()
        self.assertEqual(TEXT, element.text)
        STYLE = 'background-color: rgb(110, 228, 254);'
        self.assertEqual(STYLE, element.get_attribute('style').encode('utf-8', errors='ignore'))
        

    def test_back_formating(self):
        self.subject = self.add_random_number('Subject preview letter ')
        TEXT = self.add_random_number('Teeeeext_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_bold_text()

        bold_text = letter_manager.letter_selector.get_bold_text()
        self.assertEqual(TEXT, bold_text)

        letter_manager.letter_writer.click_preview_button()
        not_bold_text = letter_manager.letter_selector.get_not_bold_text()
        self.assertEqual(TEXT, not_bold_text)
        self.subject = ''

    def test_clear_formating(self):
        self.subject = self.add_random_number('Subject letter ')
        TEXT = self.add_random_number('All_kind_formating_')
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.set_italic_text()
        letter_manager.letter_writer.set_underline_text()
        letter_manager.letter_writer.set_bold_text()
        letter_manager.letter_writer.set_strike_through_text()

        letter_manager.letter_writer.click_clear_all_button()
        unformating_text = letter_manager.letter_selector.get_unformating_text()
        self.assertEqual(TEXT, unformating_text)
        self.subject = ''

    def test_insert_link(self):
        self.subject = self.add_random_number('Hello ')
        TEXT = self.add_random_number('Welcome to the 4th semester of Tehnopark MailRu ') + '\n'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter_without_sending(self.login, self.subject, TEXT)
        letter_manager.letter_writer.click_link_button()
        txt_link = self.main_page.letter_manager.letter_writer.text_link
        link = self.main_page.letter_manager.letter_writer.link
        letter_manager.letter_writer.enter_link(link)
        letter_manager.letter_writer.enter_text_link(txt_link)
        letter_manager.letter_writer.click_confirm_link()

        actual_text = letter_manager.letter_selector.get_link_text()
        self.assertEqual(txt_link, actual_text)
        self.subject = ''
        
        
    def tearDown(self):
        if self.subject != '':
            if 'restore' not in self.subject:
                self.main_page.navigation_manager.go_to_inbox()
            self.main_page.letter_manager.remove_letter(self.subject)
        super(MainTest, self).tearDown()
    