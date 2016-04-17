# -*- coding: utf-8 -*-
from pages import *
from components import *
import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote


class TestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


class BaseTestCase(TestCase):
    REMOVED_NOTHING = False

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.login()
        self.home_page = HomePage(self.driver)

    def login(self):
        USEREMAIL = 'selenium.panichkina'
        PASSWORD = os.environ['HW4PASSWORD']

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.enter.go()
        auth_form = auth_page.form
        auth_form.set_login(USEREMAIL)
        auth_form.set_password(PASSWORD)
        auth_form.submit.go()

    def click(self, btn):
        btn.is_clickable(self)
        btn.do_click(self)
        btn.check_click(self)

    def delete_file(self, filename):
        self.home_page.select_file(filename)
        self.home_page.toolbar_buttons.delete.go()
        self.home_page.toolbar_buttons.delete_window.delete_submit.go()

    def delete_all(self):
        if self.REMOVED_NOTHING:
            return
        self.home_page.open()
        self.home_page.toolbar_buttons.checkbox.go()
        self.home_page.toolbar_buttons.delete.go()
        self.home_page.toolbar_buttons.delete_window.delete_submit.go()

    def init(self):
        self.home_page.upload.go()
        self.upload_form = self.home_page.form

    def tearDown(self):
        self.delete_all()
        super(BaseTestCase, self).tearDown()


class AuthTest(BaseTestCase):
    USEREMAIL = 'selenium.panichkina'
    USERDOMAIN = '@mail.ru'
    USERNAME = USEREMAIL + USERDOMAIN

    def test(self):
        user_name = self.home_page.user_name.get()
        self.assertEqual(self.USERNAME, user_name)


class CloseTest(BaseTestCase):

    def test_for_X(self):
        self.init()
        self.REMOVED_NOTHING = True
        # Действия теста
        self.upload_form.close.go()


class UploadTest(BaseTestCase):
    file1 = "test.png"
    file2 = "test2.png"

    def setUp(self):
        super(UploadTest, self).setUp()
        self.init()

    def test_for_select(self):
        file = self.file1
        self.upload_form.input_file.go(file)

    def test_for_drop(self):
        file = self.file2
        self.upload_form.drag_and_drop.go(file)


class UploadAnyFormats(BaseTestCase):
    file_docx = "docx.docx"
    file_pdf = "pdf.pdf"
    file_jpg = "jpeg.jpg"
    file_exe = "exe.exe"
    folder = "folder"
    file_without = "without"

    def setUp(self):
        super(UploadAnyFormats, self).setUp()
        self.init()

    def test_docx(self):
        file = self.file_docx
        self.upload_form.input_file.go(file)

    def test_pdf(self):
        file = self.file_pdf
        self.upload_form.input_file.go(file)

    def test_jpg(self):
        file = self.file_jpg
        self.upload_form.input_file.go(file)

    def test_exe(self):
        file = self.file_exe
        self.upload_form.input_file.go(file)

    def test_without_format(self):
        file = self.file_without
        self.upload_form.input_file.go(file)

    def folder(self):
        file = self.folder
        self.upload_form.drag_and_drop.go(file)


class UploadAnyNamesCyrillic(BaseTestCase):
    file_10symbols = 'ДЕСЯТЬЫЫЫЫ'
    file_100symbols = 'СТОкрпрпаапрорвкрнкыеоыенонпротпртыеркеыркерапиапипаперурфкрукекуЕУКФЕПЫКПАЫИАЫПРКУКФПУФКПВ' \
                      'АМИАИлллл'
    file_127symbols = 'СТОДВАДЦАТЬСЕМЬкрпрпаапрорвкрнкыеоыенонпротпртыеркеыркерапиапипаперурфкрукекуЕУКФЕПЫКПАЫИАЫПР' \
                      'КУКФПУФКПВАМИАИВЫАПВАвапавамуупппп'
    file_255symbols = 'ДВЕСТИПЯТЬДЕСЯТПЯТЬкрпрпаапрорвкрнкыеоыенонпротпртыеркеыркерапиапипаперурфкрукекуЕУКФЕПЫКПАЫИ' \
                      'АЫПРКУКФПУФКПВАМИАИВЫАПВАвапавамууфвыапркфцаупыкывмпеамаквампирвпеыаявпаккпквпврпкпкпуыкрпукпк' \
                      'екраптимявчапнаоврыфеуцнугклньавтыпцФУРЦКОУЕТВАИЦФУРЕАОКЦУуекрекпппп'

    def setUp(self):
        super(UploadAnyNamesCyrillic, self).setUp()
        self.init()

    def test_10(self):
        file = self.file_10symbols
        self.upload_form.input_file.go(file)

    def test_100(self):
        file = self.file_100symbols
        self.upload_form.input_file.go(file)

    def test_127(self):
        file = self.file_127symbols
        self.upload_form.input_file.go(file)

    def test_255(self):
        file = self.file_255symbols
        self.REMOVED_NOTHING = True
        self.upload_form.input_file.go(file, invisible=True)


class UploadAnyNamesLatin(BaseTestCase):
    file_10symbols = 'TENsymbols'
    file_100symbols = 'ONEHUNDREDsymbolsrefettferffrerfergtgfdfgfdserftgvcxsedrfcxswedSDFVBDFGBVCXSAasdfdfwerfgt' \
                      'hredwsedrdf'
    file_127symbols = 'ONEHUNDREDTWENTYSEVENsymbolsrefettferffrerfergtgfdfgfdserftgvcxsedrfcxswedSDFVBDFGBVCXSAasdf' \
                      'dfwerfggtggrgrgthredwsedrdffsdfggtf'
    file_255symbols = 'TWOHUNDREDFIFTYFIVEsymbolsrefettferffrerfergtgfdfgfdserftgvcxsedrfcxswedSDFVBDFGBVCXgdvdfnkvfw' \
                      'kdpkdpkwdpkdep;kdmdnfbjkdmnbhjkfmnbhjknskndbjkaSAasdfdfwerfggtggrgrgthredwsedrdffsdfggtffrefer' \
                      'gtgkkoihjoklmknmqwertyrfdfgfgfdfcdfgvcrtrfdefrgtfdertgdfgdsadfgfdsd'

    def setUp(self):
        super(UploadAnyNamesLatin, self).setUp()
        self.init()

    def test_10(self):
        file = self.file_10symbols
        self.upload_form.input_file.go(file)

    def test_100(self):
        file = self.file_100symbols
        self.upload_form.input_file.go(file)

    def test_127(self):
        file = self.file_127symbols
        self.upload_form.input_file.go(file)

    def test_255(self):
        file = self.file_255symbols
        self.upload_form.input_file.go(file)


class UploadAnySizes(BaseTestCase):
    file_0b = '0bytes.txt'
    file_1Mb = '1Mb.jpg'
    file_2030Mb = 'over_2Gb.zip'

    def setUp(self):
        super(UploadAnySizes, self).setUp()
        self.init()

    def test_small(self):
        file = self.file_0b
        self.upload_form.input_file.go(file)

    def test_medium(self):
        file = self.file_1Mb
        self.upload_form.input_file.go(file)

    # Слишком большой файл чтобы заливать в Git
    def extra_large(self):
        file = self.file_2030Mb
        self.upload_form.input_file.go(file)


class CopyAndMovementBase(BaseTestCase):
    file_names = ['test.png', 'test2.png', 'test3.png', 'test4.png', 'test5.png', 'test6.png', 'test7.png',
                  'test8.png', 'test9.png', 'test10.png']
    folder_names = ['folder', 'folder1']

    def preloading_files(self):
        for file in self.file_names:
            self.init()
            self.upload_form.input_file.go(file)

    def create_folder(self, name):
        self.home_page.create.go()
        create_dropdown = self.home_page.create_dropdown
        create_dropdown.folder.go()
        create_dropdown.folder_window().set_name(name)
        create_dropdown.folder_window().add.go(invisible=1)
        return FolderPage(name, self.driver)

    def copy(self, folder_from, folder_name_to, full_file_name):
        folder_from.select_file(full_file_name)
        toolbar_buttons = folder_from.toolbar_buttons
        toolbar_buttons.more.go()
        toolbar_buttons.more_dropdown.copy.go()
        toolbar_buttons.more_dropdown.copy_window().select_folder_for_copy(folder_name_to)
        toolbar_buttons.more_dropdown.copy_window().copy.go()

    def move(self, folder_from, folder_name_to, full_file_name):
        folder_from.select_file(full_file_name)
        toolbar_buttons = folder_from.toolbar_buttons
        toolbar_buttons.more.go()
        toolbar_buttons.more_dropdown.move.go()
        toolbar_buttons.more_dropdown.move_window().select_folder_for_move(folder_name_to)
        toolbar_buttons.more_dropdown.move_window().move.go()


class CopyTests(CopyAndMovementBase):
    def test_from_cloud_to_folder(self):
        # Подготовка
        file_name = self.file_names[0]
        folder = self.create_folder(self.folder_names[0])
        self.init()
        self.upload_form.input_file.go(file_name)
        # Действия теста
        self.copy(self.home_page, folder.NAME, file_name)
        # Проверка
        self.home_page.check_file_located(file_name)
        folder.check_file_located(file_name)

    def test_from_folder_to_cloud(self):
        # Подготовка
        folder = self.create_folder(self.folder_names[0])
        folder.open()
        folder.upload.go()
        file = File(self.file_names[0], folder.PATH_TO_FILE)
        folder.form.input_file.go(file.NAME, file.PATH)
        # #Действия теста
        self.copy(folder, 'CLOUD', file.PATH + file.NAME)
        # Проверка
        folder.check_file_located(file.NAME)
        self.home_page.check_file_located(file.NAME)

    def test_from_folder_to_folder(self):
        # Подготовка
        folder1 = self.create_folder(self.folder_names[0])
        folder2 = self.create_folder(self.folder_names[1])
        folder1.open()
        folder1.upload.go()
        file = File(self.file_names[0], folder1.PATH_TO_FILE)
        folder1.form.input_file.go(file.NAME, file.PATH)
        # #Действия теста
        self.copy(folder1, folder2.NAME, file.PATH + file.NAME)
        # Проверка
        folder1.check_file_located(file.NAME)
        folder2.check_file_located(file.NAME)

    def test_from_cloud_to_new_folder(self):
        # Подготовка
        folder_name = self.folder_names[0]
        file_name = self.file_names[0]
        self.init()
        self.upload_form.input_file.go(file_name)

        self.home_page.select_file(file_name)
        toolbar_buttons = self.home_page.toolbar_buttons
        toolbar_buttons.more.go()
        toolbar_buttons.more_dropdown.copy.go()
        # Действия теста
        copy_window = self.home_page.toolbar_buttons.more_dropdown.copy_window()
        copy_window.create_folder.go()
        create_folder_window = copy_window.folder_window

        create_folder_window.set_name(folder_name)
        create_folder_window.add.go(invisible=1)
        folder = FolderPage(folder_name, self.driver)

        toolbar_buttons.more_dropdown.copy_window().select_folder_for_copy(folder_name)
        toolbar_buttons.more_dropdown.copy_window().copy.go()
        # Проверка
        self.home_page.check_file_located(file_name)
        folder.check_file_located(file_name)


class MovementTests(CopyAndMovementBase):
    def test_from_cloud_to_folder(self):
        # Подготовка
        file_name = self.file_names[0]
        folder = self.create_folder(self.folder_names[0])
        self.init()
        self.upload_form.input_file.go(file_name)
        # Действия теста
        self.move(self.home_page, folder.NAME, file_name)
        # Проверка
        self.home_page.check_file_not_located(file_name)
        folder.check_file_located(file_name)

    def test_from_folder_to_cloud(self):
        # Подготовка
        folder = self.create_folder(self.folder_names[0])
        folder.open()
        folder.upload.go()
        file = File(self.file_names[0], folder.PATH_TO_FILE)
        folder.form.input_file.go(file.NAME, file.PATH)
        # #Действия теста
        self.move(folder, 'CLOUD', file.PATH + file.NAME)
        # Проверка
        folder.check_file_not_located(file.NAME)
        self.home_page.check_file_located(file.NAME)

    def test_from_folder_to_folder(self):
        # Подготовка
        folder1 = self.create_folder(self.folder_names[0])

        folder2 = self.create_folder(self.folder_names[1])
        folder1.open()
        folder1.upload.go()
        file = File(self.file_names[0], folder1.PATH_TO_FILE)
        folder1.form.input_file.go(file.NAME, file.PATH)
        # #Действия теста
        self.move(folder1, folder2.NAME, file.PATH + file.NAME)
        # Проверка
        folder1.check_file_not_located(file.NAME)
        folder2.check_file_located(file.NAME)

    def test_from_cloud_to_new_folder(self):
        # Подготовка
        folder_name = self.folder_names[0]
        file_name = self.file_names[0]
        self.init()
        self.upload_form.input_file.go(file_name)

        self.home_page.select_file(file_name)
        toolbar_buttons = self.home_page.toolbar_buttons
        toolbar_buttons.more.go()
        toolbar_buttons.more_dropdown.move.go()

        move_window = self.home_page.toolbar_buttons.more_dropdown.move_window()
        move_window.create_folder.go()
        create_folder_window = move_window.folder_window

        create_folder_window.set_name(folder_name)
        create_folder_window.add.go(invisible=1)
        folder = FolderPage(folder_name, self.driver)

        toolbar_buttons.more_dropdown.move_window().select_folder_for_move(folder_name)
        toolbar_buttons.more_dropdown.move_window().move.go()
        # Проверка
        self.home_page.check_file_not_located(file_name)
        folder.check_file_located(file_name)


class RenameTests(BaseTestCase):
    base_file = 'without'

    def setUp(self):
        super(RenameTests, self).setUp()
        self.init()
        self.upload_form.input_file.go(self.base_file)

    def rename(self, file_name):
        self.home_page.select_file(self.base_file)
        toolbar_buttons = self.home_page.toolbar_buttons
        toolbar_buttons.more.go()
        toolbar_buttons.more_dropdown.rename.go()

        rename_window = toolbar_buttons.more_dropdown.rename_window()
        rename_window.set_name(file_name)
        rename_window.rename.go()

    def test_all_latin(self):
        file_name = 'name'
        self.rename(file_name)
        self.home_page.check_file_located(file_name)
        self.home_page.check_file_not_located(self.base_file)

    def test_all_cyrillic(self):
        file_name = u'имя'
        self.rename(file_name)
        self.home_page.check_file_located(file_name)
        self.home_page.check_file_not_located(self.base_file)

    def test_all_number(self):
        file_name = '1234'
        self.rename(file_name)
        self.home_page.check_file_located(file_name)
        self.home_page.check_file_not_located(self.base_file)

    def test_with_acceptable_symbols(self):
        file_name = u'name%$#@!±§~`,;№'
        self.rename(file_name)
        self.home_page.check_file_located(file_name)
        self.home_page.check_file_not_located(self.base_file)

    def test_with_unacceptable_symbols(self):
        file_name = u'name"*/:<>?|'
        self.rename(file_name)
        self.home_page.check_file_not_located(file_name)
        self.home_page.check_file_located(self.base_file)

    def test_with_extensions(self):
        file_name = 'name.jpg.png.js'
        self.rename(file_name)
        self.home_page.check_file_located(file_name)
        self.home_page.check_file_not_located(self.base_file)

    def test_with_www_and_ru(self):
        file_name = 'www.ru'
        self.rename(file_name)
        self.home_page.check_file_located(file_name)
        self.home_page.check_file_not_located(self.base_file)

    def test_with_one_symbol(self):
        file_name = 'f'
        self.rename(file_name)
        self.home_page.check_file_located(file_name)
        self.home_page.check_file_not_located(self.base_file)

    def test_with_255_latin(self):
        file_name = 'TWOHUNDREDFIFTYFIVEsymbolsertghgfdfrtgyhujhgfdrftgyhujnbvcdxswertrweyujnbvcdxertikmnbvcdxrftyuikmnbvc' \
                    'dxsdertyujnbvfasgdhfdgsfddtyfgjfhdgsraestdyfjfhdgsfhfgfdjgjjtjwryhwrhrwhwrjhrhwthwtrhwrthjwrtjwthwrhwr' \
                    'thjrtwjtjgjgjjyhrhrthrthrheygshdjfhthtgfghyuytrfghgf'
        self.rename(file_name)
        self.home_page.check_file_located(file_name)
        self.home_page.check_file_not_located(self.base_file)

    def test_with_256_latin(self):
        file_name = 'TWOHUNDREDFIFTYSIXsymbolssffrwgethrwqetytuyrstesyryklgkjsyteasdkfhfjhgtayskflgjeryrjrstysvhmchgdtyu' \
                    'jiknhgfrdertyujhrtyrtttththththrththfhgjhgghjhghnbcvbbvbdfggfdfggfdfgfdfggfggfghnhgfgfgfujhgfdertyuikm' \
                    'nbgvfdswderftghjkjhgfdsdfghjgfdsasdfghgfdfghgfdfghjhgfd'
        self.rename(file_name)
        self.home_page.check_file_not_located(file_name)
        self.home_page.check_file_located(self.base_file)
