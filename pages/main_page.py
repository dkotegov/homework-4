from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = '/'

    SELF_USERNAME = '#profile-link-username'

    LISTING = '#dialogues-listing'

    FOLDER_ANY = '#dialogues-listing > .folder'
    FOLDER_BY_NAME = '.folder[data=\"%s\"]'
    FOLDER_BTN_DELETE_BY_NAME = FOLDER_BY_NAME + ' #delete-folder'
    FOLDER_BTN_RENAME_BY_NAME = FOLDER_BY_NAME + ' #rename-folder'
    FOLDER_INPUT_TITLE_BY_NAME = FOLDER_BY_NAME + ' input'
    FOLDER_BTN_CREATE = '.new-folder-button'
    FOLDER_BTN_EXPAND = '.folders-button'
    FOLDER_CURRENT_TITLE = '#dialogues-listing-divider > div'

    DIALOGUE_BY_NAME = '#dialogues-listing li[data=\"%s\"]:not(.folder)'
    DIALOGUE_BTN_DELETE_BY_NAME = DIALOGUE_BY_NAME + ' #delete-dialogue'
    DIALOGUE_INPUT_FIND = '.find-input'
    DIALOGUE_BTN_ADD = '#find-dialogue-button'

    MESSAGE_ANY = '#messages-listing > div:not(.fullheight)'
    MESSAGE_LAST_YOUR = '#messages-listing > div.right-block:last-child'
    MESSAGE_LAST_NOT_YOUR = '#messages-listing > div.left-block:last-child'
    MESSAGE_BTN_DELETE_LAST = '%s .delete-message'  # in %s must be MESSAGE_LAST_YOUR or MESSAGE_LAST_NOT_YOUR
    MESSAGE_INPUT_TITLE = '#theme-input'
    MESSAGE_INPUT_BODY = '#message-input'
    MESSAGE_BTN_SEND = '#message-send-button'

    OVERLAY_INPUT = '.modal input'
    OVERLAY_SUBMIT = '.modal .submit'

    def __init__(self, driver):
        super().__init__(driver, '#messages-page')

    # --------- Folders ---------
    def expandFolders(self):
        self.click(self.FOLDER_BTN_EXPAND)

    def clickFolder(self, folderName):
        self.click(self.FOLDER_BY_NAME % folderName)

    def clickDeleteFolder(self, folderName):
        self.click_hidden(self.FOLDER_BTN_DELETE_BY_NAME % folderName)

    def clickRenameFolder(self, folderName):
        self.click_hidden(self.FOLDER_BTN_RENAME_BY_NAME % folderName)

    def clickCreateFolder(self):
        self.click(self.FOLDER_BTN_CREATE)

    def setFolderTitle(self, folderName, newTitle):
        el = self.locate_el(self.FOLDER_INPUT_TITLE_BY_NAME % folderName)
        el.send_keys(Keys.SHIFT + Keys.END)
        el.send_keys(newTitle)
        el.send_keys(Keys.ENTER)

    def getFolderTitle(self, folderName):
        return self.locate_el(self.FOLDER_INPUT_TITLE_BY_NAME % folderName).get_attribute("value")

    def getFoldersCount(self):
        return len(self.locate_el(self.LISTING).find_elements(By.CLASS_NAME, "folder"))

    def isFoldersExpanded(self):
        return self.locate_el(self.FOLDER_ANY).is_displayed()

    def isFolderExists(self, folderName):
        return self.locate_el(self.FOLDER_BY_NAME % folderName).is_displayed()

    # -------- Dialogues --------
    def clickDialogue(self, dialogueName):
        self.click(self.DIALOGUE_BY_NAME % dialogueName)

    def clickDeleteDialogue(self, dialogueName):
        self.click(self.DIALOGUE_BY_NAME % dialogueName)

    def isDialogueOpened(self):
        return self.locate_el(self.MESSAGE_ANY).is_displayed()

    # --------- Overlay ----------
    def submitOverlay(self):
        self.click(self.OVERLAY_SUBMIT)

    def fillOverlay(self, value):
        self.set_field(self.OVERLAY_INPUT, value)

    # --------- Others ---------
    def get_authenticated_user_email(self):
        return self.locate_el(self.SELF_USERNAME).text
