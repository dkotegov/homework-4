from pages.main_page import MainPage
from pages.auth_page import AuthPage

from tests.base_test import BaseTest

import settings as s


class MainBaseTest(BaseTest):
    auth_page = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.page = MainPage(cls.driver)
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.auth()

    def setUp(self) -> None:
        self.driver.refresh()

    def _create_dialogue_with_name(self, name):
        self.page.clickCreateDialogue()
        self.page.setFindDialogue(name)
        self.page.clickCreateDialogue()

        self.assertTrue(self.page.is_popup_success())
        self.assertTrue(self.page.isDialogueExists(name), "Dialogue not created")
        self.assertEqual(self.page.getDialogueTitle(name), name, "Created dialogue real name is different")
        self.assertTrue(self.page.isDialogueOpened(name), "Dialogue not opened")

    def _create_dialogue_with_name_negative(self, name):
        self.page.clickCreateDialogue()
        self.page.setFindDialogue(name)
        self.page.clickCreateDialogue()
        self.assertTrue(self.page.isDialogueNotOpened(), "Dialogue opened")

    def _create_folder_with_name(self, name, renameTo=None):
        self.page.clickCreateFolder()
        self.page.fillOverlay(name)
        self.page.submitOverlay()
        self.assertTrue(self.page.is_popup_success())
        self.assertTrue(self.page.isFolderExists(name), "Folder not created")
        self.assertEqual(self.page.getFolderTitle(name), name, "Created folder real name is different")

        if renameTo is None:
            return

        self.page.renameFolder(name, renameTo)

        self.assertTrue(self.page.is_popup_success())
        self.assertEqual(self.page.getFolderTitle(renameTo), renameTo, "Renamed folder real name is different")

    def _send_message(self, title=None, body=None):
        if title is not None:
            self.page.setMessageTitle(title)
        if body is not None:
            self.page.setMessageBody(body)

        self.page.sendMessageByKeyboard()
