from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = '/'

    BASE_FOLDER_NAME = 'Общая'
    BASE_DIALOGUE_NAME = 'support@liokor.ru'

    SELF_USERNAME = '#profile-link-username'

    LISTING = '#dialogues-listing'
    MESSAGES_LISTING = '#messages-listing'

    FOLDER_ANY = '#dialogues-listing > li.folder'
    FOLDER_ALL = '#dialogues-listing > div.folder'
    FOLDER_BY_NAME = '#dialogues-listing > .folder[data=\"%s\"]'
    FOLDER_BTN_DELETE_BY_NAME = FOLDER_BY_NAME + ' #delete-folder'
    FOLDER_BTN_RENAME_BY_NAME = FOLDER_BY_NAME + ' #rename-folder'
    FOLDER_INPUT_TITLE_BY_NAME = FOLDER_BY_NAME + ' input'
    FOLDER_BTN_CREATE = '.new-folder-button'
    FOLDER_BTN_EXPAND = '.folders-button'
    FOLDER_CURRENT_TITLE = '#dialogues-listing-divider > div'
    FOLDER_NAME_INPUT = 'input[placeholder="Название папки"]'

    DIALOGUE_ANY = '#dialogues-listing > li:not(.folder)'
    DIALOGUE_BY_NAME = '#dialogues-listing li[data=\"%s\"]:not(.folder)'
    DIALOGUE_TITLE_BY_NAME = DIALOGUE_BY_NAME + ' .dialogue-title'
    DIALOGUE_IMAGE_BY_NAME = DIALOGUE_BY_NAME + ' > img'
    DIALOGUE_BTN_DELETE_BY_NAME = DIALOGUE_BY_NAME + ' #delete-dialogue'
    DIALOGUE_INPUT_FIND = '.find-input'
    DIALOGUE_BTN_ADD = '#find-dialogue-button'

    MESSAGE_ANY = '#messages-listing > div:not(.fullheight)'
    MESSAGE_LAST_ANY = MESSAGE_ANY + ':last-child'
    MESSAGE_LAST_YOUR = '#messages-listing > div.right-block:last-child'
    MESSAGE_LAST_NOT_YOUR = '#messages-listing > div.left-block:last-child'
    MESSAGE_TITLE = '%s .message-block-title'  # %s must be on of first four MESSAGE_... constants
    MESSAGE_BODY = '%s .message-body'
    MESSAGE_BTN_DELETE = '%s .delete-message'
    MESSAGE_INPUT_TITLE = '#theme-input'
    MESSAGE_INPUT_BODY = '#message-input'
    MESSAGE_BTN_SEND = '#message-send-button'
    MESSAGE_NOT_OPENED_PLUG = '#messages-listing > div.fullheight.table-rows'
    MESSAGE_NOT_DELIVERED = '%s .status-warning-svg'

    REDACTOR_BOLD = '#bold-markdown'
    REDACTOR_ITALIC = '#italic-markdown'
    REDACTOR_STRIKETHROUGH = '#strikethrough-markdown'
    REDACTOR_CODE = '#code-markdown'
    REDACTOR_H1 = '#H1-markdown'
    REDACTOR_H2 = '#H2-markdown'
    REDACTOR_H3 = '#H3-markdown'
    REDACTOR_BLOCKQUOTE = '#blockquote-markdown'
    REDACTOR_LIST = '#list-markdown'
    REDACTOR_LINK = '#link-markdown'
    REDACTOR_PHOTO = '#photo-markdown'

    OVERLAY_INPUT = '.modal input'
    OVERLAY_SUBMIT = '.modal .submit'
    OVERLAY_NO = '.modal button.close'
    OVERLAY_CROSS = '.modal span.close'

    def __init__(self, driver):
        super().__init__(driver, '#messages-page')

    # --------- Folders ---------
    def expandFolders(self):
        if not self.isFoldersExpanded():
            self.click(self.FOLDER_BTN_EXPAND)
            self.wait_until(lambda e: self.isFoldersExpanded())

    def hideFolders(self):
        if self.isFoldersExpanded():
            self.click(self.FOLDER_BTN_EXPAND)
            self.wait_until(lambda e: not self.isFoldersExpanded())

    def clickFolder(self, folderName):
        self.click(self.FOLDER_BY_NAME % folderName)

    def clickDeleteFolder(self, folderName):
        self.click_hidden(self.FOLDER_BTN_DELETE_BY_NAME % folderName)

    def clickRenameFolder(self, folderName):
        self.click_hidden(self.FOLDER_BTN_RENAME_BY_NAME % folderName)

    def renameFolder(self, folderName, newName):
        self.clickRenameFolder(folderName)
        el = self.locate_el(self.FOLDER_NAME_INPUT)
        el.clear()

        # todo: remove second click when bug would be fixed
        # empty folder name should not be permitted
        # bug: folder edit becomes inactive after clear
        self.clickRenameFolder(folderName)
        el.send_keys(newName)
        el.send_keys(Keys.ENTER)

    def clickCreateFolder(self):
        self.click(self.FOLDER_BTN_CREATE)

    def getFolderTitle(self, folderName):
        return self.locate_el(self.FOLDER_INPUT_TITLE_BY_NAME % folderName).get_attribute("value")

    def getFoldersCount(self):
        return len(self.locate_el(self.LISTING).find_elements(By.CLASS_NAME, "folder"))

    def isFoldersExpanded(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.FOLDER_ANY)

    def isFolderExists(self, folderName) -> bool:
        return bool(self.locate_el(self.FOLDER_BY_NAME % folderName))

    # -------- Dialogues --------
    def clickDialogue(self, dialogueName):
        self.click(self.DIALOGUE_BY_NAME % dialogueName)

    def clickCreateDialogue(self):
        self.click(self.DIALOGUE_BTN_ADD)

    def setFindDialogue(self, value):
        self.set_field(self.DIALOGUE_INPUT_FIND, value)

    def clickDeleteDialogue(self, dialogueName):
        self.click_hidden(self.DIALOGUE_BTN_DELETE_BY_NAME % dialogueName)

    def dragAndDropDialogueToFolder(self, dialogueName, folderName):
        self.drag_and_drop(self.DIALOGUE_BY_NAME % dialogueName, self.FOLDER_BY_NAME % folderName)

    def isDialogueOpened(self, dialogueName):
        return self.locate_el(self.MESSAGE_ANY).is_displayed() and \
               self.locate_el(self.DIALOGUE_BY_NAME % dialogueName).get_attribute("class").find("active") != -1

    def isDialogueNotOpened(self):
        return self.locate_el(self.MESSAGE_NOT_OPENED_PLUG).is_displayed()

    def isDialogueExists(self, dialogueName):
        return self.locate_el(self.DIALOGUE_BY_NAME % dialogueName).is_displayed()

    def getDialogueTitle(self, dialogueName):
        return self.locate_el(self.DIALOGUE_TITLE_BY_NAME % dialogueName).text

    def getDialogueImage(self, dialogueName):
        return self.locate_el(self.DIALOGUE_IMAGE_BY_NAME % dialogueName).get_attribute("src")

    def getDialoguesCount(self):
        # waiting for dialogues to appear
        self.locate_el(self.DIALOGUE_ANY)
        return len(self.locate_el(self.LISTING).find_elements(By.CSS_SELECTOR, "li:not(.folder)"))

    # -------- Messages --------
    def clickSendMessage(self):
        self.click(self.MESSAGE_BTN_SEND)

    def sendMessageByKeyboard(self):
        el = self.locate_el(self.MESSAGE_INPUT_BODY)
        el.send_keys(Keys.CONTROL + Keys.ENTER)

    def editorSelectAll(self):
        el = self.locate_el(self.MESSAGE_INPUT_BODY)
        el.click()
        self.select_all(el)

    def clickDeleteLastMessage(self, your: bool = None):
        if your is None:
            self.click_hidden(self.MESSAGE_BTN_DELETE % self.MESSAGE_LAST_ANY)
        elif your:
            self.click_hidden(self.MESSAGE_BTN_DELETE % self.MESSAGE_LAST_YOUR)
        else:
            self.click_hidden(self.MESSAGE_BTN_DELETE % self.MESSAGE_LAST_NOT_YOUR)

    def setMessageTitle(self, value):
        self.set_field(self.MESSAGE_INPUT_TITLE, value)

    def setMessageBody(self, value):
        self.set_field(self.MESSAGE_INPUT_BODY, value)

    def getMessageTitle(self):
        return self.locate_el(self.MESSAGE_INPUT_TITLE).get_attribute('value')

    def getMessageBody(self):
        return self.locate_el(self.MESSAGE_INPUT_BODY).get_attribute('value')

    def getLastMessage(self):
        return self.locate_el(self.MESSAGE_LAST_ANY)

    def getLastMessageTitle(self):
        return self.locate_el(self.MESSAGE_TITLE % self.MESSAGE_LAST_ANY).text

    def getLastMessageBody(self):
        return self.locate_el(self.MESSAGE_BODY % self.MESSAGE_LAST_ANY).text

    def isLastMessageYours(self):
        return self.locate_el(self.MESSAGE_LAST_YOUR).is_displayed()

    def getLastYourMessageTitle(self):
        return self.locate_el(self.MESSAGE_TITLE % self.MESSAGE_LAST_YOUR).text

    def getLastYourMessageBody(self):
        return self.locate_el(self.MESSAGE_BODY % self.MESSAGE_LAST_YOUR).text

    def isLastMessageNotYours(self):
        return self.click(self.MESSAGE_BTN_DELETE % self.MESSAGE_LAST_NOT_YOUR)

    def isMessageNotDelivered(self):
        return self.locate_el(self.MESSAGE_NOT_DELIVERED % self.MESSAGE_LAST_YOUR).is_displayed()

    def getMessagesCount(self):
        return len(self.locate_el(self.MESSAGES_LISTING).find_elements(By.CSS_SELECTOR, "div.message-block[title]"))

    # --------- Redactor ----------
    def clickRedactorBold(self):
        self.click(self.REDACTOR_BOLD)

    def clickRedactorItalic(self):
        self.click(self.REDACTOR_ITALIC)

    def clickRedactorStrikethrough(self):
        self.click(self.REDACTOR_STRIKETHROUGH)

    def clickRedactorCode(self):
        self.click(self.REDACTOR_CODE)

    def clickRedactorH1(self):
        self.click(self.REDACTOR_H1)

    def clickRedactorH2(self):
        self.click(self.REDACTOR_H2)

    def clickRedactorH3(self):
        self.click(self.REDACTOR_H3)

    def clickRedactorBlockquote(self):
        self.click(self.REDACTOR_BLOCKQUOTE)

    def clickRedactorList(self):
        self.click(self.REDACTOR_LIST)

    def clickRedactorLink(self):
        self.click(self.REDACTOR_LINK)

    def clickRedactorPhoto(self):
        self.click(self.REDACTOR_PHOTO)

    # --------- Overlay ----------
    def _overlayClick(self, locator: str):
        el = self.locate_el(locator)
        el.click()
        try:
            self.wait_until(lambda d: not el.is_displayed())
        except StaleElementReferenceException:
            pass


    def submitOverlay(self):
        self._overlayClick(self.OVERLAY_SUBMIT)

    def discardOverlayByNo(self):
        self._overlayClick(self.OVERLAY_NO)

    def discardOverlayByCross(self):
        self._overlayClick(self.OVERLAY_CROSS)

    def fillOverlay(self, value):
        self.set_field(self.OVERLAY_INPUT, value)

    # --------- Others ---------
    def get_authenticated_user_email(self):
        return self.locate_el(self.SELF_USERNAME).text

    def delete_all_folders(self):
        self.expandFolders()

        folders = self.driver.find_elements(By.CSS_SELECTOR, self.FOLDER_ALL)
        for folder in folders:
            name = folder.get_attribute('data')
            if name != self.BASE_FOLDER_NAME:
                self.clickDeleteFolder(name)
                self.submitOverlay()

        self.hideFolders()

    def delete_dialogue(self, name):
        self.clickDeleteDialogue(name)
        self.submitOverlay()

    def delete_all_dialogues(self):
        self.setFindDialogue('')
        # waiting for dialogues to load
        self.locate_el(self.DIALOGUE_ANY)

        dialogues = self.driver.find_elements(By.CSS_SELECTOR, self.DIALOGUE_ANY)
        for dialogue in dialogues:
            try:
                name = dialogue.get_attribute('data')
                if name != self.BASE_DIALOGUE_NAME:
                    self.delete_dialogue(name)
            except StaleElementReferenceException:
                pass
