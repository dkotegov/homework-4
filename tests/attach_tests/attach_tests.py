# coding=utf-8
from components.login_and_write import login_and_write

from pages.file_attaching_page import FileAttachingPage
from tests.attach_tests.base_attach import BaseAttach
from tests.base_test import BaseTest


class AttachTest_document(BaseAttach):

    TEST_FILE_XLSX = BaseAttach.TEST_FILE_DIR + 'АДАМОВА!.xlsx'

    def test(self):
        BaseAttach.test(self)

        # вложение документа из компьютера
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.set_file_attach_input()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_XLSX)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertEqual(self.file_attaching_form.checkMessageSent(), True)
        # file_attaching_form.closeMessageSent()


class AttachTest_Media(BaseAttach):
    TEST_FILE_MEDIA = BaseAttach.TEST_FILE_DIR + 'Track01.mp3'

    def test(self):
        BaseAttach.test(self)

        # вложение медиафайла
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.set_file_attach_input()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_MEDIA)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertEqual(self.file_attaching_form.checkMessageSent(), True)
        # file_attaching_form.closeMessageSent()


class AttachTest_Executable(BaseAttach):
    TEST_FILE_EXECUTABLE = BaseAttach.TEST_FILE_DIR + 'hack.sh'

    def test(self):
        BaseAttach.test(self)

        # вложение исполняемого файла
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.set_file_attach_input()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_EXECUTABLE)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertEqual(self.file_attaching_form.checkMessageSent(), True)
        # file_attaching_form.closeMessageSent()