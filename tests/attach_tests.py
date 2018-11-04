# coding=utf-8
from components.login_and_write import login_and_write

from pages.file_attaching_page import FileAttachingPage
from tests.base_test import BaseTest


class AttachTest_document(BaseTest):
    # ATTACH_FILE_BUTTON =

    TEST_FILE_XLSX = BaseTest.TEST_FILE_DIR + 'АДАМОВА!.xlsx'

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)

        file_attaching_page = FileAttachingPage(self.driver)
        file_attaching_form = file_attaching_page.form

        # вложение документа из компьютера
        file_attaching_form.open_writing_letter()
        file_attaching_form.set_file_attach_input()
        file_attaching_form.send_keys_to_input(self.TEST_FILE_XLSX)
        file_attaching_form.set_destionation_email()
        file_attaching_form.click_send_button()

        self.assertEqual(file_attaching_form.checkMessageSent(), True)
        # file_attaching_form.closeMessageSent()


class AttachTest_Media(BaseTest):
    TEST_FILE_MEDIA = BaseTest.TEST_FILE_DIR + 'Track01.mp3'

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)

        file_attaching_page = FileAttachingPage(self.driver)
        file_attaching_form = file_attaching_page.form

        # вложение медиафайла
        file_attaching_form.open_writing_letter()
        file_attaching_form.set_file_attach_input()
        file_attaching_form.send_keys_to_input(self.TEST_FILE_MEDIA)
        file_attaching_form.set_destionation_email()
        file_attaching_form.click_send_button()

        self.assertEqual(file_attaching_form.checkMessageSent(), True)
        # file_attaching_form.closeMessageSent()


class AttachTest_Executable(BaseTest):
    TEST_FILE_EXECUTABLE = BaseTest.TEST_FILE_DIR + 'hack.sh'

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)

        file_attaching_page = FileAttachingPage(self.driver)
        file_attaching_form = file_attaching_page.form

        # вложение исполняемого файла
        file_attaching_form.open_writing_letter()
        file_attaching_form.set_file_attach_input()
        file_attaching_form.send_keys_to_input(self.TEST_FILE_EXECUTABLE)
        file_attaching_form.set_destionation_email()
        file_attaching_form.click_send_button()

        self.assertEqual(file_attaching_form.checkMessageSent(), True)
        # file_attaching_form.closeMessageSent()