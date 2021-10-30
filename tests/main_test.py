from random import randrange, choice
from string import ascii_letters

from pages.auth_page import AuthPage
from pages.main_page import MainPage

from tests.base_test import BaseTest


def _randomString(length):
    return ''.join(choice(ascii_letters) for _ in range(length))


def _randomMail(length, endsWith=None):
    mail = _randomString(length)
    if endsWith is not None:
        return mail + "@" + endsWith
    return mail + "@" + _randomString(4) + "." + _randomString(3)


class MainTest(BaseTest):
    auth_page = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.auth_page = AuthPage(cls.driver)

    def setUp(self) -> None:
        self.auth_page.auth()
        self.page = MainPage(self.driver)
        self.page.driver.maximize_window()

    def tearDown(self):
        self.driver.delete_all_cookies()

    # -------- Folders --------
    def _create_folder_with_name(self, name, renameTo=None):
        self.page.expandFolders()
        self.page.clickCreateFolder()
        self.page.fillOverlay(name)
        self.page.submitOverlay()
        self.assertTrue(self.page.is_popup_success())
        self.assertTrue(self.page.isFolderExists(name), f"Folder not created")
        self.assertEqual(self.page.getFolderTitle(name), name, f"Created folder real name is different")

        if renameTo is None:
            self.page.clickDeleteFolder(name)
            self.page.submitOverlay()
            return
        self.page.clickRenameFolder(name)
        self.page.setFolderTitle(name, renameTo)
        self.assertTrue(self.page.is_popup_success())
        self.assertEqual(self.page.getFolderTitle(renameTo), renameTo, f"Renamed folder real name is different")
        self.page.clickDeleteFolder(renameTo)
        self.page.submitOverlay()

    '''
    def test_open_folders(self):
        self.page.expandFolders()
        self.assertTrue(self.page.isFoldersExpanded(), "Folders not expanded")

    def test_creating_default_folder(self):
        self.page.expandFolders()
        self.assertTrue(self.page.isFolderExists("Общая"), "Default folder not created")

    def test_create_folder_positive(self):
        self._create_folder_with_name(_randomString(15))

    def test_create_folder_positive_long_name(self):
        self._create_folder_with_name(_randomString(500))

    def test_create_folder_positive_special_symbols(self):
        self._create_folder_with_name("!@##@$#*@#^_with_)(@#&%")

    def test_create_folder_positive_HTML_tags(self):
        self._create_folder_with_name("<p>No</p><img src='https://mail.liokor.ru/media/avatars/097f7a6103e61039a9dadac5e7d7eb65aa451121de8b30ad2a147c5aafb440c7.jpg'> it was image")

    def test_create_folder_positive_cyrillic(self):
        self._create_folder_with_name("Здесь лежит *three hundred bucks*")

    def test_create_folder_negative_empty(self):
        self.page.expandFolders()
        count = self.page.getFoldersCount()
        self.page.clickCreateFolder()
        self.page.submitOverlay()
        self.assertEqual(self.page.getFoldersCount(), count, f"Folders count must be equal")
    
    def test_rename_folder_positive(self):
        self._create_folder_with_name("old_name", _randomString(15))

    def test_rename_folder_positive_long_name(self):
        self._create_folder_with_name("old_name", _randomString(500))

    def test_rename_folder_positive_special_symbols(self):
        self._create_folder_with_name("old_name", "!@##@$#*@#^_with_)(@#&%")

    def test_rename_folder_positive_HTML_tags(self):
        self._create_folder_with_name("old_name", "<p>No</p><img src='https://mail.liokor.ru/media/avatars/097f7a6103e61039a9dadac5e7d7eb65aa451121de8b30ad2a147c5aafb440c7.jpg'> it was image")

    def test_rename_folder_positive_cyrillic(self):
        self._create_folder_with_name("old_name", "Здесь лежит *three hundred bucks*")
    '''

    # -------- Dialogues --------
    def _create_dialogue_with_name(self, name):
        self.page.expandFolders()
        self.page.clickCreateFolder()
        self.page.fillOverlay(name)
        self.page.submitOverlay()
        self.assertTrue(self.page.is_popup_success())
        self.assertTrue(self.page.isFolderExists(name), f"Folder not created")
        self.assertEqual(self.page.getFolderTitle(name), name, f"Created folder real name is different")

    def test_open_folders(self):
        self.page.expandFolders()
        self.assertTrue(self.page.isFoldersExpanded(), "Folders not expanded")
