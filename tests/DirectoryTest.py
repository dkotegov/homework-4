# -*- coding: utf-8 -*-
from BasicTest import BasicTest
from pages.DirectoryPage import DirectoryPage
from pages.main_page.letters.LetterSelector import LetterSelector
from pages.main_page.menu.navigation.NavigationManager import NavigationManager
from pages.MainPage import MainPage
from config import config


class DirectoryTest(BasicTest):
    def setUp(self):
        super(DirectoryTest, self).setUp()
        self.directory_page = DirectoryPage(self.driver)
        self.directory_page.open()
        self.auth()
        self.main_page = MainPage(self.driver)
        self.manager = self.main_page.letter_manager

    def test_move_to_archive(self):
        self.letter_subject = self.add_random_number('Mail for archive ')
        LETTER_TEXT = 'Lorem text for archive'
        self.manager.write_letter(config.DEFAULT_MAIL, self.letter_subject, LETTER_TEXT)
        self.manager.letter_selector.select_letter(self.letter_subject)
        self.directory_page.move_to_archive()
        self.directory_page.click_nav_archive_button()

        letter_selector = LetterSelector(self.driver)
        letter_selector.find_letter_subject_real(self.letter_subject)
        

    def test_move_to_inbox_from_archive(self):
        self.letter_subject = self.add_random_number('$$$ Archive ')
        LETTER_TEXT = 'Lorem text for archive'
        self.manager.write_letter(config.DEFAULT_MAIL, self.letter_subject, LETTER_TEXT)
        self.manager.letter_selector.select_letter(self.letter_subject)
        self.directory_page.move_to_archive()
        self.directory_page.click_nav_archive_button()
        self.manager.restore_letter(self.letter_subject)

        navigation_manager = NavigationManager(self.driver)
        navigation_manager.go_to_inbox()

        letter_selector = LetterSelector(self.driver)
        letter_selector.find_letter_subject_real(self.letter_subject)

    def test_set_important_letter(self):
        self.letter_subject = self.add_random_number('The IMPORTANT letter ')
        LETTER_TEXT = 'Lorem text lorem lorem lorem'
        self.manager.write_letter(config.DEFAULT_MAIL, self.letter_subject, LETTER_TEXT)
        self.directory_page.set_check_flag()
        self.assertTrue(self.directory_page.get_important_status())

    def test_unset_important_letter(self):
        self.letter_subject = self.add_random_number('The UNimportant letter ')
        LETTER_TEXT = 'Lorem text lorem lorem lorem'
        self.manager.write_letter(config.DEFAULT_MAIL, self.letter_subject, LETTER_TEXT)
        self.directory_page.set_check_flag()
        self.directory_page.unset_check_flag()
        self.assertFalse(self.directory_page.get_important_status())

    def test_move_to_social(self):
        self.letter_subject = self.add_random_number('The SOCIAL letter ')
        LETTER_TEXT = 'Lorem text lorem lorem lorem'
        self.manager.write_letter(config.DEFAULT_MAIL, self.letter_subject, LETTER_TEXT)
        self.manager.letter_selector.select_letter(self.letter_subject)

        self.directory_page.move_to_social()
        self.directory_page.go_to_social()

        letter_selector = LetterSelector(self.driver)
        letter_selector.find_letter_subject_real(self.letter_subject)

    def test_move_to_inbox_from_social(self):
        self.letter_subject = self.add_random_number('not SOCIAL letter ')
        LETTER_TEXT = 'Lorem text for archive'
        self.manager.write_letter(config.DEFAULT_MAIL, self.letter_subject, LETTER_TEXT)
        self.manager.letter_selector.select_letter(self.letter_subject)

        self.directory_page.move_to_social()
        self.directory_page.go_to_social()
        self.manager.restore_letter(self.letter_subject)

        navigation_manager = NavigationManager(self.driver)
        navigation_manager.go_to_inbox()
        letter_selector = LetterSelector(self.driver)

        letter_selector.find_letter_subject_real(self.letter_subject)

    def test_move_to_newsletters(self):
        self.letter_subject = self.add_random_number('The NewsLetter letter ')
        LETTER_TEXT = 'Lorem text lorem lorem lorem'
        self.manager.write_letter(config.DEFAULT_MAIL, self.letter_subject, LETTER_TEXT)
        self.manager.letter_selector.select_letter(self.letter_subject)

        self.directory_page.move_to_newsletters() 
        self.directory_page.go_to_newsletters()

        letter_selector = LetterSelector(self.driver)
        letter_selector.find_letter_subject_real(self.letter_subject)

    def test_send_empty_letter(self):
        self.manager.letter_writer.click_write_letter_button()
        self.manager.letter_writer.click_send_letter_button()
        self.letter_subject = ''
        EXPECTED_MESSAGE = u'Не указан адрес получателя'
        self.assertEqual(EXPECTED_MESSAGE, self.directory_page.error_message())

    def test_send_letter_without_subject(self):
        self.letter_subject = ''
        LETTER_TEXT = 'Lorem text lorem lorem lorem'
        self.manager.letter_writer.click_write_letter_button()
        self.manager.letter_writer.enter_email_receiver(config.DEFAULT_MAIL)
        self.manager.letter_writer.enter_textbox(LETTER_TEXT)
        self.manager.letter_writer.click_send_letter_button()
        self.manager.letter_writer.close_sent_window()

        letter_selector = LetterSelector(self.driver)
        self.letter_subject = self.directory_page.empty_subject_text
        actual_text = letter_selector.get_letter_text(self.letter_subject)
        self.assertEqual(LETTER_TEXT, actual_text)

    def test_send_letter_without_receiver(self):
        self.letter_subject = 'Subject letter'
        LETTER_TEXT = 'Lorem text lorem lorem lorem'
        self.manager.letter_writer.click_write_letter_button()
        self.manager.letter_writer.enter_subject(self.letter_subject)
        self.manager.letter_writer.enter_textbox(LETTER_TEXT)
        self.manager.letter_writer.click_send_letter_button()
        self.letter_subject = ''
        EXPECTED_MESSAGE = u'Не указан адрес получателя'
        self.assertEqual(EXPECTED_MESSAGE, self.directory_page.error_message())

    def test_save_draft_letter(self):
        self.letter_subject = self.add_random_number('Draft letter ')
        LETTER_TEXT = 'Lorem text lorem lorem lorem'
        self.manager.letter_writer.click_write_letter_button()
        self.manager.letter_writer.enter_subject(self.letter_subject)
        self.manager.letter_writer.enter_textbox(LETTER_TEXT)
        self.directory_page.click_save_mail()

        self.directory_page.close_writer_window()

        self.directory_page.go_to_drafts()

        letter_selector = LetterSelector(self.driver)
        actual_text = letter_selector.get_mini_letter_text(self.letter_subject)
        self.directory_page.close_writer_window()
        self.assertEqual(LETTER_TEXT, actual_text)

    def test_send_draft_letter(self):
        self.letter_subject = self.add_random_number('Send draft letter ')
        LETTER_TEXT = 'Lorem text lorem lorem lorem'
        self.manager.letter_writer.click_write_letter_button()
        self.manager.letter_writer.enter_email_receiver(config.DEFAULT_MAIL)
        self.manager.letter_writer.enter_subject(self.letter_subject)
        self.manager.letter_writer.enter_textbox(LETTER_TEXT)
        self.directory_page.click_save_mail()
        self.directory_page.close_writer_window()
        self.directory_page.go_to_drafts()
        self.directory_page.open_draft()
        self.manager.letter_writer.click_send_letter_button()
        self.manager.letter_writer.close_sent_window()

    def tearDown(self):
        if self.letter_subject != '':
            cond1 = 'Mail for archive' not in self.letter_subject
            cond2 = '$$$ Archive' not in self.letter_subject
            cond3 = 'The SOCIAL letter' not in self.letter_subject
            cond4 = 'not SOCIAL letter' not in self.letter_subject
            cond5 = 'The NewsLetter letter' not in self.letter_subject
            cond6 = 'Draft letter ' not in self.letter_subject

            if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
                self.main_page.navigation_manager.go_to_inbox()

            self.manager.remove_letter(self.letter_subject)

        self.driver.quit()
