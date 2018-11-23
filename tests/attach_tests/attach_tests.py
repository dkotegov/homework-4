# coding=utf-8
# from selenium.webdriver import ActionChains

from tests.attach_tests.base_attach import BaseAttach


# Выбрать документ --> Получение сообщения с документом c возможностью просмотра из сообщения
class AttachTest_document(BaseAttach):
    TEST_FILE_XLSX = BaseAttach.TEST_FILE_DIR + 'АДАМОВА!.xlsx'

    def test(self):
        BaseAttach.test(self)
        # вложение документа из компьютера
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.set_file_attach_input()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_XLSX, 1)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertTrue(self.file_attaching_form.checkMessageSent())


# Выбрать медиафайл --> Получение сообщения с медиафайлом с возможностью воспроизведения по клику
class AttachTest_Media(BaseAttach):
    TEST_FILE_MEDIA = BaseAttach.TEST_FILE_DIR + 'Track01.mp3'

    def test(self):
        BaseAttach.test(self)

        # вложение медиафайла
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_MEDIA)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertTrue(self.file_attaching_form.checkMessageSent())


# Выбрать исполняемый файл --> Получение сообщения с исполняемым файлом. При попытке скачать файл должно появиться
# предупреждение о потенциальной вредоносности файла. Если речь идет о нескольких файлах, можно комбинировать форматы
class AttachTest_Executable(BaseAttach):
    TEST_FILE_EXECUTABLE = BaseAttach.TEST_FILE_DIR + 'hack.sh'

    def test(self):
        BaseAttach.test(self)

        # вложение исполняемого файла
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_EXECUTABLE)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertTrue(self.file_attaching_form.checkMessageSent())


# Тест под вопросом, нужно ли делать # вложение 99 изображений
class AttachTest99Photos(BaseAttach):
    TEST_FILE_IMG = BaseAttach.TEST_FILE_DIR + 'IMG__1.JPG'

    def test(self):
        BaseAttach.test(self)

        # вложение 99 изображений
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.set_file_attach_input()
        for _ in range(1, 99):
            self.file_attaching_form.send_keys_to_input(self.TEST_FILE_IMG, time_to_wait=1)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertTrue(self.file_attaching_form.checkMessageSent())


# Выбрать файл размером (1.99 Гб) ---> Файл должен быть прикреплен и успешно отправлен
class AttachTestAlmostTwoGigFile(BaseAttach):
    TEST_FILE_ALMOST_2_GIGS = BaseAttach.TEST_FILE_DIR + '1_99_GIG_FILE.txt'

    def test(self):
        BaseAttach.test(self)

        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.set_file_attach_input()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_ALMOST_2_GIGS)
        self.file_attaching_form.set_destionation_email()
        self.file_attaching_form.click_send_button()

        self.assertTrue(self.file_attaching_form.checkMessageSent())


# Выбрать файл размером (25 Мб) --> Файл должен быть прикреплен и успешно отправлен (через облако)
class AttachTest25MbAndMoreThroughCloud(BaseAttach):
    TEST_FILE_MORE_25_MB = BaseAttach.TEST_FILE_DIR + 'More_25_mb.png'

    def test(self):
        BaseAttach.test(self)

        # вложение файла размером больше 25 Мб (должен загрузиться через облако)
        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_MORE_25_MB, 10)

        self.assertIsNotNone(self.file_attaching_form.check_loaded_through_cloud())


class AttachTestLess25MbWithoutCloud(BaseAttach):
    TEST_FILE_LESS_25MB = BaseAttach.TEST_FILE_DIR + './pict.png'

    def test(self):
        BaseAttach.test(self)

        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.send_keys_to_input(self.TEST_FILE_LESS_25MB, 10)

        self.assertTrue(self.file_attaching_form.check_loaded_without_cloud())


# Выбрать документ из облака--> Получение сообщения с документом c возможностью просмотра из сообщения
class AttachCloudDocument(BaseAttach):
    TEST_FILE_XLSX = 'some_table.xlsx'

    def test(self):
        BaseAttach.test(self)

        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.click_cloud_button()
        self.file_attaching_form.select_cloud_file(self.TEST_FILE_XLSX)
        self.file_attaching_form.do_cloud_attach()

        self.assertTrue(self.file_attaching_form.check_loaded(filename=self.TEST_FILE_XLSX))


# Выбрать медиафайл --> Получение сообщения с медиафайлом с возможностью воспроизведения по клику
class AttachCloudMedia(BaseAttach):
    TEST_FILE_MEDIA = 'Track01.mp3'

    def test(self):
        BaseAttach.test(self)

        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.click_cloud_button()
        self.file_attaching_form.select_cloud_file(self.TEST_FILE_MEDIA)
        self.file_attaching_form.do_cloud_attach()

        self.assertTrue(self.file_attaching_form.check_loaded(filename=self.TEST_FILE_MEDIA))


# Выбрать исполняемый файл из облака --> Получение сообщения с исполняемым файлом. При попытке скачать файл должно
# появиться предупреждение о потенциальной вредоносности файла. Если речь идет о нескольких файлах,
# можно комбинировать форматы
class AttachCloudExecutable(BaseAttach):
    TEST_FILE_EXECUTABLE = 'hack.sh'

    def test(self):
        BaseAttach.test(self)

        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.click_cloud_button()
        self.file_attaching_form.select_cloud_file(self.TEST_FILE_EXECUTABLE)
        self.file_attaching_form.do_cloud_attach()

        self.assertTrue(self.file_attaching_form.check_loaded(filename=self.TEST_FILE_EXECUTABLE))


# Выбрать файл размером (1.99 Гб) из облака ---> Файл должен быть прикреплен и успешно отправлен
class AttachCloudAlmost2GigFile(BaseAttach):
    TEST_FILE_ALMOST_2_GIGS = '1_99_GIG_FILE.txt'

    def test(self):
        BaseAttach.test(self)

        self.file_attaching_form.open_writing_letter()
        self.file_attaching_form.click_cloud_button()
        self.file_attaching_form.select_cloud_file(filename=self.TEST_FILE_ALMOST_2_GIGS)
        self.file_attaching_form.do_cloud_attach()

        self.assertTrue(self.file_attaching_form.check_loaded(self.TEST_FILE_ALMOST_2_GIGS))

        #
        # Прикрепление файла из компьютера:
        # Выбрать документ --> Получение сообщения с документом c возможностью просмотра из сообщения – \/

        # Выбрать медиафайл --> Получение сообщения с медиафайлом с возможностью воспроизведения по клику – \/

        # Выбрать исполняемый файл --> Получение сообщения с исполняемым файлом. При попытке скачать файл должно появиться – \/
        # предупреждение о потенциальной вредоносности файла. Если речь идет о нескольких файлах, можно комбинировать форматы

        # Выбрать файл размером (1.99 Гб) ---> Файл должен быть прикреплен и успешно отправлен – \/

        # Выбрать файл размером (25 Мб) --> Файл должен быть прикреплен и успешно отправлен (через облако) – \/

        # Выбрать файл размером (24.99 Мб) --> Файл должен быть прикреплен и успешно отправлен (напрямую без облака) – \/

        # ––––––––––––––––––––
        # ––––––––––––––––––––


        # Выбрать исполняемый файл и отправить на gmail почту --> Со стороны отправителя: получение сообщения от
        # mailer-daemon@corp.mail.ru об ошибке | Со стороны получателя: никаких сообщений не должно быть получено

        # Выбрать более 99 файлов --> Появится сообщение о том, что отправятся только 100 файлов. Возможности прикрепить
        # новые файлы не будет. Ожидается отправка 99 файлов

        # Выбрать 99 изображений (размер не имеет значения) и прикрепить как изображение. --> Все изображения полноразмерно
        # вложатся в тело письма (при тестировании функции drag&drop)

        # Выбрать 99 изображений (размер не имеет значения) и прикрепить как файл. --> Все изображения вложатся в тело письма
        #  (при тестировании функции drag&drop)


        # Продублировать вышеперечисленные действия для файлов из облака

        # ––––––––––––––––––––
