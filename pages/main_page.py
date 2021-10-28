from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = '/'

    SELF_USERNAME = '#profile-link-username'

    FOLDER_BY_NAME = '.folder[data=%s]'
    FOLDER_BTN_DELETE_BY_NAME = '.folder[data="%s"] #delete-folder'
    FOLDER_BTN_RENAME_BY_NAME = '.folder[data="%s"] #rename-folder'
    FOLDER_INPUT_TITLE_BY_NAME = '.folder input'
    FOLDER_BTN_CREATE = '.new-folder-button'
    FOLDER_BTN_EXPAND = '.folders-button'
    FOLDER_CURRENT_TITLE = '#dialogues-listing-divider > div'

    DIALOGUE_BY_NAME = '#dialogues-listing li[data="%s"]:not(.folder)'
    DIALOGUE_BTN_DELETE_BY_NAME = DIALOGUE_BY_NAME + ' #delete-dialogue'
    DIALOGUE_INPUT_FIND = '.find-input'
    DIALOGUE_BTN_ADD = '#find-dialogue-button'

    MESSAGE_LAST_YOUR = '#messages-listing > div.right-block:last-child'
    MESSAGE_LAST_NOT_YOUR = '#messages-listing > div.left-block:last-child'
    MESSAGE_BTN_DELETE_LAST = '%s .delete-message'
    MESSAGE_INPUT_TITLE = '#theme-input'
    MESSAGE_INPUT_BODY = '#message-input'
    MESSAGE_BTN_SEND = '#message-send-button'

    OVERLAY_INPUT = '.modal input'
    OVERLAY_SUBMIT = '.modal .submit'

    def __init__(self, driver):
        super().__init__(driver, '#messages-page')

    def get_authenticated_user_email(self):
        return self.locate_el(self.SELF_USERNAME).text
