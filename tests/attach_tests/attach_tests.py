# coding=utf-8
from tests.attach_tests.base_attach import BaseAttach


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

        self.file_attaching_form.closeMessageSent()


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


class AttachTest99Photos(BaseAttach):
    TEST_FILE_IMG = BaseAttach.TEST_FILE_DIR + 'IMG__1.JPG'

    def test(self):
        BaseAttach.test(self)

        # вложение 99 изображений
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.set_file_attach_input()
        for _ in range(1, 99):
            self.file_attaching_form.send_keys_to_input(self.TEST_FILE_IMG)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertEqual(self.file_attaching_form.checkMessageSent(), True)


class AttachTestAlmostTwoGigFile(BaseAttach):
    TEST_FILE_ALMOST_2_GIGS = BaseAttach.TEST_FILE_DIR + '1_99_GIG_FILE.txt'

    def test(self):
        BaseAttach.test(self)

        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.set_file_attach_input()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_ALMOST_2_GIGS)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertEqual(self.file_attaching_form.checkMessageSent(), True)


class AttachTest25MbAndMoreThroughCloud(BaseAttach):
    TEST_FILE_MORE_25_MB = BaseAttach.TEST_FILE_DIR + 'More_25_mb.png'

    def test(self):
        BaseAttach.test(self)

        # вложение файла размером больше 25 Мб (должен загрузиться через облако)
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.set_file_attach_input()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_MORE_25_MB)

        self.assertEqual(self.file_attaching_form.check_loaded_through_cloud() is not None, True)
