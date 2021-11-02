import os
from random import choice
from string import ascii_letters

from pages.auth_page import AuthPage
from pages.main_page import MainPage

from tests.base_test import BaseTest

from selenium.webdriver import DesiredCapabilities, ChromeOptions, Remote
import settings as s

DEFAULT_AVATAR = "/images/default-avatar.jpg"
MAIL_AVATAR = "/images/mail.png"
YANDEX_AVATAR = "/images/yandex.png"
GMAIL_AVATAR = "/images/gmail.png"

DEFAULT_FOLDER = "Общая"
DEFAULT_DIALOGUE = "support@liokor.ru"


def _randomString(length):
    return ''.join(choice(ascii_letters) for _ in range(length))


def _randomMail(length, endsWith=None):
    mail = _randomString(length)
    if endsWith is not None:
        return mail + "@" + endsWith
    return mail + "@" + _randomString(4) + "." + _randomString(3)


class MainTest(BaseTest):
    driver2 = None
    auth_page2 = None
    auth_page = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        options = ChromeOptions()
        options.add_argument("--incognito")
        # cls.driver2 = Remote(
        #     command_executor=s.HUB_URL,
        #     desired_capabilities=getattr(DesiredCapabilities, 'CHROME').copy(),
        #     options=options
        # )
        #
        # cls.auth_page2 = AuthPage(cls.driver2)
        cls.auth_page = AuthPage(cls.driver)

    def setUp(self) -> None:
        self.auth_page.auth()
        #self.page2 = MainPage(self.driver2)
        self.page = MainPage(self.driver)
        self.page.driver.maximize_window()

    def tearDown(self):
        #self.driver2.delete_all_cookies()
        self.driver.delete_all_cookies()

    # -------- Folders --------
    def _create_folder_with_name(self, name, renameTo=None, delete=True):
        self.page.clickCreateFolder()
        self.page.fillOverlay(name)
        self.page.submitOverlay()
        self.assertTrue(self.page.is_popup_success())
        self.assertTrue(self.page.isFolderExists(name), "Folder not created")
        self.assertEqual(self.page.getFolderTitle(name), name, "Created folder real name is different")

        if renameTo is None:
            if delete:
                self.page.clickDeleteFolder(name)
                self.page.submitOverlay()
            return
        self.page.clickRenameFolder(name)
        self.page.setFolderTitle(name, renameTo)
        self.assertTrue(self.page.is_popup_success())
        self.assertEqual(self.page.getFolderTitle(renameTo), renameTo, "Renamed folder real name is different")
        if delete:
            self.page.clickDeleteFolder(renameTo)
            self.page.submitOverlay()

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
        self._create_folder_with_name(_randomString(500))

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
        self._create_folder_with_name("old_name", _randomString(500))

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
        foldersNames = [_randomString(15) for _ in range(30)]
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

    # -------- Dialogues --------
    def _create_dialogue_with_name(self, name, delete=True):
        self.page.clickCreateDialogue()
        self.page.setFindDialogue(name)
        self.page.clickCreateDialogue()
        self.assertTrue(self.page.is_popup_success())
        self.assertTrue(self.page.isDialogueExists(name), "Dialogue not created")
        self.assertEqual(self.page.getDialogueTitle(name), name, "Created dialogue real name is different")
        self.assertTrue(self.page.isDialogueOpened(name), "Dialogue not opened")
        if delete:
            self.page.clickDeleteDialogue(name)
            self.page.submitOverlay()

    def _create_dialogue_with_name_negative(self, name):
        self.page.clickCreateDialogue()
        self.page.setFindDialogue(name)
        self.page.clickCreateDialogue()
        self.assertTrue(self.page.isDialogueNotOpened(), "Dialogue opened")

    def test_open_dialogue(self):
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.assertTrue(self.page.isDialogueOpened(DEFAULT_DIALOGUE), "Dialogue not opened")

    def test_create_dialogue_positive(self):
        self._create_dialogue_with_name(_randomMail(15))

    def test_delete_dialogue(self):
        self._create_dialogue_with_name(_randomMail(15))
        self.assertTrue(self.page.isDialogueNotOpened(), "Deleted dialogue already opened")
         
    def test_create_dialogue_positive_long_name(self):
        self._create_dialogue_with_name(_randomMail(500))

    def test_create_dialogue_positive_HTML_tags(self):
        self._create_dialogue_with_name("<p>No</p><strong>Very_strong</strong>@mail.ru")

    def test_create_dialogue_positive_cyrillic(self):
        self._create_dialogue_with_name("Здесь_дают_*three_hundred_bucks*@mail.ru")

    def test_create_dialogue_negative_incorrect_email(self):
        self._create_dialogue_with_name_negative(_randomMail(15, "leo.o"))

    def test_create_dialogue_negative_spaces_in_name(self):
        mail = _randomMail(15)
        mail = mail[:5] + " " + mail[5:]
        self._create_dialogue_with_name_negative(mail)

    def test_create_dialogue_negative_empty_name(self):
        self._create_dialogue_with_name_negative("")

    def test_create_dialogue_negative_existed_name(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail, delete=False)
        self.page.clickCreateDialogue()
        self.page.setFindDialogue(mail)
        self.page.clickCreateDialogue()
        self.assertTrue(self.page.isDialogueOpened(mail), "Dialogue opened")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    def test_find_dialogue(self):
        dialoguesNames = ["no_way@yandex.ru", "no_way@mail.ru", "way@yandex.ru"]
        for name in dialoguesNames:
            self._create_dialogue_with_name(name, delete=False)
        self.driver.refresh()
        self.page.setFindDialogue("no")
        self.assertEqual(self.page.getDialoguesCount(), 2)
        self.page.setFindDialogue("yandex")
        self.assertEqual(self.page.getDialoguesCount(), 2)
        self.page.setFindDialogue("way")
        self.assertEqual(self.page.getDialoguesCount(), 3)
        self.page.setFindDialogue("liokor")
        self.assertEqual(self.page.getDialoguesCount(), 1)
        for name in dialoguesNames:
            self.page.clickDeleteDialogue(name)
            self.page.submitOverlay()
    
    def test_open_many_dialogues(self):
        dialoguesNames = [_randomMail(15) for _ in range(30)]
        for name in dialoguesNames:
            self._create_dialogue_with_name(name, delete=False)
        self.driver.refresh()
        self.page.clickDialogue(dialoguesNames[-1])
        self.assertTrue(self.page.isDialogueOpened(dialoguesNames[-1]), "Can't open last dialogue")
        for name in dialoguesNames:
            self.page.clickDeleteDialogue(name)
            self.page.submitOverlay()

    def test_open_previous_dialogue_after_refresh(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail, delete=False)
        self.driver.refresh()
        self.assertTrue(self.page.isDialogueOpened(mail), "Dialogue not opened")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    def _test_dialogue_image(self, mail, expectedUrl):
        self._create_dialogue_with_name(mail, delete=False)
        self.assertTrue(self.page.getDialogueImage(mail).endswith(expectedUrl), "Dialogue image is different")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    def test_dialogue_image_with_liokor(self):
        self._test_dialogue_image("liokor@liokor.ru", DEFAULT_AVATAR)

    def test_dialogue_image_with_yandex(self):
        self._test_dialogue_image("liokor@yandex.ru", YANDEX_AVATAR)
    
    def test_dialogue_image_with_ya(self):
        self._test_dialogue_image("liokor@ya.ru", YANDEX_AVATAR)
        
    def test_dialogue_image_with_mail(self):
        self._test_dialogue_image("liokor@mail.ru", MAIL_AVATAR)

    def test_dialogue_image_with_gmail(self):
        self._test_dialogue_image("liokor@gmail.com", GMAIL_AVATAR)
    
    # TODO: Send from second page test
    '''
    def test_get_message_without_refresh(self):
        self.auth_page2.auth(s.USERNAME2, s.PASSWORD2)
        self.page2.
    '''
    # -------- Messages --------
    def _send_message(self, title=None, body=None):
        if title is not None:
            self.page.setMessageTitle(title)
        if body is not None:
            self.page.setMessageBody(body)
        # self.page.clickSendMessage()
        self.page.sendMessageByKeyboard()

    def _send_message_positive(self, title, body, recipient=s.USERNAME2 + "@liokor.ru", delete=True):
        self._create_dialogue_with_name(recipient, delete=False)
        self._send_message(title, body)
        self.assertTrue(self.page.isLastMessageYours(), "Last message not yours")
        if delete:
            self.page.clickDeleteDialogue(recipient)
            self.page.submitOverlay()

    def test_send_message_positive(self):
        self._send_message_positive(_randomString(15), _randomString(100))

    def test_send_message_positive_special_symbols(self):
        self._send_message_positive("!@)(:?*!&cz@$^@(!*#)*(@&^", "(!@*#&*^&@$^(::;*!@#&%!(@^#%!@*#%^&#%*&!@#^&6IA")

    def test_send_message_positive_HTML_in_title(self):
        title = "<p>Title</p> <strong>STRONG TITLE</strong>"
        recipient = s.USERNAME2 + "@liokor.ru"
        self._send_message_positive(title, _randomString(10), recipient, delete=False)
        self.assertEqual(self.page.getLastYourMessageTitle(), "Title STRONG TITLE")
        self.page.clickDeleteDialogue(recipient)
        self.page.submitOverlay()

    def test_send_message_positive_HTML_in_body(self):
        body = "<p>body</p><strong>STRONG BODY</strong>normal body"
        recipient = s.USERNAME2 + "@liokor.ru"
        self._send_message_positive(_randomString(10), body, recipient, delete=False)
        self.assertEqual(self.page.getLastYourMessageBody(), body)
        self.page.clickDeleteDialogue(recipient)
        self.page.submitOverlay()

    def test_send_message_negative_empty_body(self):
        recipient = s.USERNAME2 + "@liokor.ru"
        self._create_dialogue_with_name(recipient, delete=False)
        messagesCount = self.page.getMessagesCount()
        self._send_message(_randomString(10), "")
        self.assertEqual(self.page.getMessagesCount(), messagesCount, "Messages count is not equal")
        self.page.clickDeleteDialogue(recipient)
        self.page.submitOverlay()

    def test_send_message_negative_recipient_not_exists(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail, delete=False)
        self._send_message(_randomString(10), _randomString(20))
        self.assertTrue(self.page.isMessageNotDelivered(), "Message delivered but mustn't be")
        self.assertFalse(self.page.is_popup_success(), "Message delivered but mustn't be")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    def test_delete_message(self):
        recipient = s.USERNAME2 + "@liokor.ru"
        self._send_message_positive(_randomString(15), _randomString(100), recipient, delete=False)
        messagesCount = self.page.getMessagesCount()
        self.page.clickDeleteLastMessage(your=True)
        self.page.submitOverlay()
        self.assertEqual(self.page.getMessagesCount(), messagesCount-1, "Message wasn't deleted")
        self.page.clickDeleteDialogue(recipient)
        self.page.submitOverlay()

    def test_load_message_body_after_refresh(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail, delete=False)
        body = "Message body\nWith one string break."
        self.page.setMessageBody(body)
        self.driver.refresh()
        self.assertEqual(self.page.getMessageBody(), body, "Message body was not loaded")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    def test_load_message_body_after_dialogues_checkout(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail, delete=False)
        body = "Message body\nWith one string break."
        self.page.setMessageBody(body)
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.assertEqual(self.page.getMessageBody(), "", "Can't checkout to default dialogue")
        self.page.clickDialogue(mail)
        self.assertEqual(self.page.getMessageBody(), body, "Message body was not loaded")
        self.page.clickDeleteDialogue(mail)
        self.page.submitOverlay()

    # TODO: autocomplete message theme (надо отправить сообщение себе и посмотреть, какая тема будет при открытии
    #  диалога. Там приколы с Re[number]: тема
