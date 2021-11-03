from tests.main.main_base_test import MainBaseTest
from tests.main.utils import _randomString, _randomMail

DEFAULT_FOLDER = "Общая"


class FoldersTest(MainBaseTest):
    def setUp(self) -> None:
        super().setUp()
        # folders drops dialogues so need to delete them first
        self.page.delete_all_folders()
        self.page.delete_all_dialogues()

    def test_open_folders(self):
        self.page.expandFolders()
        self.assertTrue(self.page.isFoldersExpanded(), "Folders not expanded")

    def test_creating_default_folder(self):
        self.page.expandFolders()
        self.assertTrue(self.page.isFolderExists(DEFAULT_FOLDER), "Default folder not created")

    def test_create_folder_positive(self):
        self.page.expandFolders()
        self._create_folder_with_name(_randomString(15))

    def test_create_folder_positive_long_name(self):
        self.page.expandFolders()
        self._create_folder_with_name(_randomString(250))

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
        self._create_folder_with_name("old_name", _randomString(250))

    def test_rename_folder_positive_special_symbols(self):
        self.page.expandFolders()
        self._create_folder_with_name("old_name", "!@##@$#*@#^_with_)(@#&%")

    def test_rename_folder_positive_HTML_tags(self):
        self.page.expandFolders()
        self._create_folder_with_name("old_name", "<p>No</p><img src='https://mail.liokor.ru/media/avatars/097f7a6103e61039a9dadac5e7d7eb65aa451121de8b30ad2a147c5aafb440c7.jpg'> it was image")

    def test_rename_folder_positive_cyrillic(self):
        self.page.expandFolders()
        self._create_folder_with_name("old_name", "Здесь лежит *three hundred bucks*")

    def test_open_many_folders(self):
        foldersNames = [_randomString(15) for _ in range(7)]
        self.page.expandFolders()
        for name in foldersNames:
            self._create_folder_with_name(name, delete=False)
        self.assertTrue(self.page.isFoldersExpanded(), "Can't expand folders")
        self.assertTrue(self.page.isFolderExists(foldersNames[-1]), "Can't open last folder")
        for name in foldersNames:
            self.page.clickDeleteFolder(name)
            self.page.submitOverlay()

    def test_add_dialogue_to_folder(self):
        mail = _randomMail(15)
        folder = _randomString(15)
        self._create_dialogue_with_name(mail, delete=False)
        self.page.expandFolders()
        self._create_folder_with_name(folder, delete=False)
        self.page.dragAndDropDialogueToFolder(mail, folder)
        self.assertTrue(self.page.is_popup_success())
        self.driver.refresh()
        self.page.expandFolders()
        self.assertEqual(self.page.getDialoguesCount(), 1, "Dialogue wasn't moved to folder")
        self.page.clickFolder(folder)
        self.assertTrue(self.page.isDialogueExists(mail), "Dialogue wasn't moved to folder")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()
        self.page.clickDeleteFolder(folder)
        self.page.submitOverlay()

    def test_move_dialogues_from_deleted_folder(self):
        dialoguesNames = [_randomMail(15) for _ in range(3)]
        for name in dialoguesNames:
            self._create_dialogue_with_name(name, delete=False)
        folder = _randomString(15)
        self.page.expandFolders()
        self._create_folder_with_name(folder, delete=False)
        self.page.dragAndDropDialogueToFolder(dialoguesNames[0], folder)
        self.page.dragAndDropDialogueToFolder(dialoguesNames[1], folder)
        self.driver.refresh()
        self.page.expandFolders()
        self.assertEqual(self.page.getDialoguesCount(), 2, "Dialogues wasn't moved to folder")
        self.page.clickFolder(folder)
        self.assertTrue(self.page.isDialogueExists(dialoguesNames[0]), "Dialogue wasn't moved to folder")
        self.assertTrue(self.page.isDialogueExists(dialoguesNames[1]), "Dialogue wasn't moved to folder")
        self.page.clickFolder(DEFAULT_FOLDER)
        self.page.clickDeleteFolder(folder)
        self.page.submitOverlay()
        self.assertEqual(self.page.getDialoguesCount(), 4, "Dialogues wasn't moved to default folder back")
        for name in dialoguesNames:
            self.page.clickDeleteDialogue(name)
            self.page.submitOverlay()
