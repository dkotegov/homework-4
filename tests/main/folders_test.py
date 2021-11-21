from tests.main.main_base_test import MainBaseTest
from utils.random_strings import _randomString, _randomMail

DEFAULT_FOLDER = "Общая"


class FoldersTest(MainBaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        # folders drops dialogues so need to delete them first
        cls.page.delete_all_folders()
        cls.page.delete_all_dialogues()

    def tearDown(self) -> None:
        self.page.delete_all_folders()
        self.page.delete_all_dialogues()

    def test_creating_default_folder(self):
        self.page.expandFolders()
        self.assertTrue(self.page.isFolderExists(DEFAULT_FOLDER), "Default folder not created")

    def test_create_folder_positive(self):
        self.page.expandFolders()
        self._create_folder_with_name(_randomString(15))

    def test_create_folder_positive_long_name(self):
        self.page.expandFolders()
        self._create_folder_with_name(_randomString(150))

    def test_create_folder_positive_special_symbols(self):
        self.page.expandFolders()
        self._create_folder_with_name("!@##@$#*@#^_with_)(@#&%")

    def test_create_folder_positive_HTML_tags(self):
        self.page.expandFolders()
        self._create_folder_with_name("<p>No</p><img src='https://mail.liokor.ru/media/avatars/097f7a6103e61039a9dadac5e7d7eb65aa451121de8b30ad2a147c5aafb440c7.jpg'> it was image")

    def test_create_folder_positive_cyrillic(self):
        self.page.expandFolders()
        self._create_folder_with_name("Здесь лежит *three hundred bucks*")

    def test_create_folder_negative_empty(self):
        self.page.expandFolders()
        count = self.page.getFoldersCount()
        self.page.clickCreateFolder()
        self.page.submitOverlay()

        self.assertEqual(self.page.getFoldersCount(), count, "Folders count must be equal")

    def test_rename_folder_positive(self):
        self.page.expandFolders()
        self._create_folder_with_name("old_name", _randomString(15))

    def test_rename_folder_positive_long_name(self):
        self.page.expandFolders()
        self._create_folder_with_name("old_name", _randomString(150))

    def test_rename_folder_positive_special_symbols(self):
        self.page.expandFolders()
        self._create_folder_with_name("old_name", "!@##@$#*@#^_with_)(@#&%")

    def test_rename_folder_positive_HTML_tags(self):
        self.page.expandFolders()
        self._create_folder_with_name("old_name", "<p>No</p><img src='https://mail.liokor.ru/media/avatars/097f7a6103e61039a9dadac5e7d7eb65aa451121de8b30ad2a147c5aafb440c7.jpg'> it was image")

    def test_rename_folder_positive_cyrillic(self):
        self.page.expandFolders()
        self._create_folder_with_name("old_name", "Здесь лежит *three hundred bucks*")

    def test_create_many_folders(self):
        folders_count = 7
        foldersNames = [_randomString(15) for _ in range(folders_count)]
        self.page.expandFolders()
        for name in foldersNames:
            self._create_folder_with_name(name)

        self.assertTrue(self.page.getFoldersCount(), folders_count)
        self.assertTrue(self.page.isFoldersExpanded(), "Can't expand folders")
        self.assertTrue(self.page.isFolderExists(foldersNames[-1]), "Can't open last folder")

    def test_add_dialogue_to_folder(self):
        mail = _randomMail(15)
        folder = _randomString(15)

        self._create_dialogue_with_name(mail)
        self.page.expandFolders()
        self._create_folder_with_name(folder)

        self.page.dragAndDropDialogueToFolder(mail, folder)
        self.assertTrue(self.page.is_popup_success())

        self.assertEqual(self.page.getDialoguesCount(), 1, "Dialogue wasn't moved to folder")
        self.page.clickFolder(folder)
        self.assertTrue(self.page.isDialogueExists(mail), "Dialogue wasn't moved to folder")

    def test_move_dialogues_from_deleted_folder(self):
        dialoguesNames = [_randomMail(15) for _ in range(3)]
        for name in dialoguesNames:
            self._create_dialogue_with_name(name)

        folder = _randomString(15)
        self.page.expandFolders()
        self._create_folder_with_name(folder)

        self.page.dragAndDropDialogueToFolder(dialoguesNames[0], folder)
        self.page.dragAndDropDialogueToFolder(dialoguesNames[1], folder)

        self.driver.refresh()

        self.page.expandFolders()
        self.assertEqual(self.page.getDialoguesCount(), 2, "Dialogues weren't moved to folder")

        self.page.clickFolder(folder)
        self.assertTrue(self.page.isDialogueExists(dialoguesNames[0]), "Dialogue wasn't moved to folder")
        self.assertTrue(self.page.isDialogueExists(dialoguesNames[1]), "Dialogue wasn't moved to folder"
                                                                       "")
        self.page.clickFolder(DEFAULT_FOLDER)
        self.page.clickDeleteFolder(folder)
        self.page.submitOverlay()

        self.page.wait_until(lambda d: self.page.getDialoguesCount() == 4)
