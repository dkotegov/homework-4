from selenium.webdriver import ActionChains

from Base import Component
from pathlib import Path


class Utils(Component):
    BANNER = '//div[@data-qa-modal]'
    MINI_BANNER = '//div[@class="PromoTooltip__root--2vPmD"]'
    BUY_CLOUD_BANNER = '//div[@class="b-tooltip__content"]'
    CLOSE_MINI_BANNER_BUTTON = '//div[@class="PromoTooltip__close--3zFr1 PromoTooltip__closeLight--JBMkK"]'
    CLOSE_BANNER_BUTTON = '//*[local-name() = "svg" and @class="Dialog__close--1rKyk"]'
    CLOSE_BUY_CLOUD_BANNER = '//div[@class="b-panel__close__icon"]'

    def close_banner_if_exists(self):
        banner_exists = self._check_if_element_exists_by_xpath(self.BANNER)
        if banner_exists:
            self.driver.find_element_by_xpath(self.CLOSE_BANNER_BUTTON).click()

    def close_mini_banner_if_exists(self):
        banner_exists = self._check_if_element_exists_by_xpath(self.MINI_BANNER)
        if banner_exists:
            self.driver.find_element_by_xpath(self.CLOSE_MINI_BANNER_BUTTON).click()

    def close_buy_cloud_banner_if_exists(self):
        banner_exists = self._check_if_element_exists_by_xpath(self.BUY_CLOUD_BANNER)
        if banner_exists:
            self.driver.find_element_by_xpath(self.BUY_CLOUD_BANNER).click()


class Folders(Component):
    CREATE_SELECTOR = '//div[@data-name="create"]'
    CREATE_NEW_FOLDER_BUTTON_IN_SELECTOR = '//div[@data-name="createFolder"]'
    FOLDER_NAME_INPUT = '//input[@placeholder="Введите имя папки"]'
    SUBMIT_CREATE_FOLDER_BUTTON = '//div[@class="CreateNewFolderDialog__button--7S1Hs"][1]/button'
    DELETE_FOLDER_BUTTON = '//div[@data-name="remove"]'
    CONFIRM_DELETE_FOLDER_BUTTON = '//div[@class="b-layer__controls__buttons"]/button[@data-name="remove"]'
    FOLDER_XPATH_BY_NAME = '//a[@data-qa-type="folder" and @data-qa-name="{}"]'

    def create_folder(self, folder_name):
        self._wait_until_and_get_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.CREATE_NEW_FOLDER_BUTTON_IN_SELECTOR).click()
        elem = self._wait_until_and_get_elem_by_xpath(self.FOLDER_NAME_INPUT)
        elem.clear()
        elem.send_keys(folder_name)
        self._wait_until_and_get_elem_by_xpath(self.SUBMIT_CREATE_FOLDER_BUTTON).click()

    def check_folder_exists(self, folder_name):
        return self._check_if_element_exists_by_xpath(self.FOLDER_XPATH_BY_NAME.format(folder_name))

    def open_folder(self, folder_url):
        self.driver.get(folder_url)

    def delete_folder(self):
        self._wait_until_and_get_elem_by_xpath(self.DELETE_FOLDER_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_DELETE_FOLDER_BUTTON).click()


class Files(Component):
    UPLOAD_BUTTON = '//div[@data-name="upload"]'
    FILE_INPUT = '//input[@type="file" and @class="layer_upload__controls__input"]'
    UPLOAD_POPUP = '//div[@class="layer_upload"]'
    UPLOAD_IN_PROGRESS = '//span[@data-bem="b-upload-status" and starts-with(text(),"Загрузка файлов")]'
    REWRITE_BUTTON = '//button[@data-id="rewrite"]'
    SUCCESS_UPLOAD = '//span[@data-bem="b-upload-status" and text()="Загрузка завершена"]'

    FILE_BY_NAME = '//a[@data-qa-name="{}"]'
    WORKSPACE = '//div[@class="VirtualList__root--2_JbO VirtualList__root_grid--TvMC0"]'
    UPLOAD_DROPZONE_INPUT = '//input[@class="UploadDropArea__input--lVhu-"]'

    DELETE_BUTTON = '//div[@data-name="remove"]'
    DELETE_CONTEXT_BUTTON = '//div[@id="dropdownList"]//div[@data-name="remove"]'
    CONFIRM_DELETE_BUTTON = '//div[@class="b-layer__controls__buttons"]/button[@data-name="remove"]'

    def upload_file(self, filepath):
        self._wait_until_and_get_elem_by_xpath(self.UPLOAD_BUTTON).click()
        self._wait_for_elem_by_xpath(self.UPLOAD_POPUP)
        self.driver.find_element_by_xpath(self.FILE_INPUT).send_keys(filepath)
        if self._check_if_element_exists_by_xpath(self.REWRITE_BUTTON):
            self.driver.find_element_by_xpath(self.REWRITE_BUTTON).click()
        while self._check_if_element_exists_by_xpath(self.UPLOAD_IN_PROGRESS):
            pass
        self._wait_for_elem_by_xpath(self.SUCCESS_UPLOAD)

    def drag_and_drop_file_upload(self, filepath):
        drop_input = self._wait_until_and_get_invisible_elem_by_xpath(self.UPLOAD_DROPZONE_INPUT)

        drop_input.send_keys(filepath)

        self._wait_for_elem_by_xpath(self.SUCCESS_UPLOAD)

    def check_if_file_exists(self, filename):
        return self._check_if_element_exists_by_xpath(self.FILE_BY_NAME.format(filename))

    def select_file(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.FILE_BY_NAME.format(filename)).click()

    def select_file_if_exists(self, filename):
        exists = self.check_if_file_exists(filename)
        if exists:
            self._wait_until_and_get_elem_by_xpath(self.FILE_BY_NAME.format(filename)).click()
        return exists

    def unselect_file(self):
        self._wait_until_and_get_elem_by_xpath(self.WORKSPACE).click()

    def open_context(self, filename):
        elem = self._wait_until_and_get_elem_by_xpath(self.FILE_BY_NAME.format(filename))
        ActionChains(self.driver).context_click(elem).perform()

    def hover_file(self, filename):
        elem = self._wait_until_and_get_elem_by_xpath(self.FILE_BY_NAME.format(filename))
        ActionChains(self.driver).move_to_element(elem).perform()

    def delete_file_from_toolbar(self):
        self._wait_until_and_get_elem_by_xpath(self.DELETE_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_DELETE_BUTTON).click()

    def delete_file_from_context(self):
        self._wait_until_and_get_elem_by_xpath(self.DELETE_CONTEXT_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_DELETE_BUTTON).click()


class FileHistory(Component):
    MORE_BUTTON = '//div[@data-name="more"]'
    HISTORY_BUTTON = '//div[@data-name="history"]'
    HISTORY_CONTEXT_BUTTON = '//div[@id="dropdownList"]//div[@data-name="viewHistory"]'
    HISTORY_POPUP = '//div[@data-bem="b-file-history"]'
    HISTORY_FILES = '//div[@class="b-collection__item b-collection__item_file-history b-collection__item_axis-y"]'
    CLOSE_HISTORY_BUTTON = '//div[@data-bem="b-file-history"]//button[@data-name="close"]'

    def open_history_from_toolbar(self):
        self._wait_until_and_get_elem_by_xpath(self.MORE_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.HISTORY_BUTTON).click()
        self._wait_for_elem_by_xpath(self.HISTORY_POPUP)
        self._wait_for_elem_by_xpath(self.HISTORY_FILES)

    def open_history_from_context(self):
        self._wait_until_and_get_elem_by_xpath(self.HISTORY_CONTEXT_BUTTON).click()
        self._wait_for_elem_by_xpath(self.HISTORY_POPUP)
        self._wait_for_elem_by_xpath(self.HISTORY_FILES)

    def check_if_history_open(self):
        return self._check_if_element_exists_by_xpath(self.HISTORY_POPUP)

    def count_history_files(self):
        files = self.driver.find_elements_by_xpath(self.HISTORY_FILES)
        return len(files)

    def close_history(self):
        self._wait_until_and_get_elem_by_xpath(self.CLOSE_HISTORY_BUTTON).click()


class Download(Component):
    DOWNLOAD_TOOLBAR_BUTTON = '//div[@data-name="download"]'
    DOWNLOAD_CONTEXT_BUTTON = '//div[@id="dropdownList"]//div[@data-name="download"]'
    DOWNLOAD_GRID_BUTTON = '//a[@data-qa-name="{}"]//div[@class="DataListItemThumb__pin--3amKK"]'

    def download_from_toolbar(self):
        self._wait_until_and_get_elem_by_xpath(self.DOWNLOAD_TOOLBAR_BUTTON).click()

    def download_from_context(self):
        self._wait_until_and_get_elem_by_xpath(self.DOWNLOAD_CONTEXT_BUTTON).click()

    def download_from_grid(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.DOWNLOAD_GRID_BUTTON.format(filename)).click()

    @staticmethod
    def _is_download_finished(temp_folder, filename):
        firefox_temp_file = sorted(Path(temp_folder).glob('*.part'))
        chrome_temp_file = sorted(Path(temp_folder).glob('*.crdownload'))
        downloaded_files = sorted(Path(temp_folder).glob('{}'.format(filename)))
        if (len(firefox_temp_file) == 0) and \
                (len(chrome_temp_file) == 0) and \
                (len(downloaded_files) == 1):
            return True
        else:
            return False

    def wait_for_download(self, temp_folder, filename):
        while not self._is_download_finished(temp_folder, filename):
            pass


class Favorites(Component):
    ADD_FAVORITE_TOOLBAR_BUTTON = '//div[@data-name="addToFavorites"]'
    REMOVE_FAVORITE_TOOLBAR_BUTTON = '//div[@data-name="removeFromFavorites"]'

    ADD_FAVORITE_CONTEXT_BUTTON = '//div[@id="dropdownList"]//div[@data-name="addToFavorite"]'
    REMOVE_FAVORITE_CONTEXT_BUTTON = '//div[@id="dropdownList"]//div[@data-name="removeFromFavorites"]'

    ADD_FAVORITE_GRID_BUTTON = '//a[@data-qa-name="{}"]//div[@class="FavoriteIcon__root--wzRgi"]'
    REMOVE_FAVORITE_GRID_BUTTON = '//a[@data-qa-name="{}"]//div[@class="FavoriteIcon__root--wzRgi ' \
                                  'FavoriteIcon__root_active--2Sjt6"]'

    def add_in_toolbar(self):
        self._wait_until_and_get_elem_by_xpath(self.ADD_FAVORITE_TOOLBAR_BUTTON).click()

    def remove_in_toolbar(self):
        self._wait_until_and_get_elem_by_xpath(self.REMOVE_FAVORITE_TOOLBAR_BUTTON).click()

    def add_in_context(self):
        self._wait_until_and_get_elem_by_xpath(self.ADD_FAVORITE_CONTEXT_BUTTON).click()

    def remove_in_context(self):
        self._wait_until_and_get_elem_by_xpath(self.REMOVE_FAVORITE_CONTEXT_BUTTON).click()

    def add_in_grid(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.ADD_FAVORITE_GRID_BUTTON.format(filename)).click()

    def remove_in_grid(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.REMOVE_FAVORITE_GRID_BUTTON.format(filename)).click()


class Copy(Component):
    MORE_BUTTON = '//div[@data-name="more"]'
    COPY_TOOLBAR_BUTTON = '//div[@data-name="copy"]'
    COPY_CONTEXT_BUTTON = '//div[@id="dropdownList"]//div[@data-name="copy"]'
    COPY_POPUP = '//div[@data-qa-modal="select-folder-dialog-copy"]'

    FOLDER_IN_POPUP = '//div[@data-name="/{}" and @class="TreeNode__root--22m4E TreeNode__root_selectDlg--cT_dx"]'
    CONFIRM_BUTTON = '//button[@data-name="action"]'

    def copy_from_toolbar(self, to_folder):
        self._wait_until_and_get_elem_by_xpath(self.MORE_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.COPY_TOOLBAR_BUTTON).click()
        self._wait_for_elem_by_xpath(self.COPY_POPUP)

        self._wait_until_and_get_elem_by_xpath(self.FOLDER_IN_POPUP.format(to_folder)).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_BUTTON).click()

    def copy_from_context(self, to_folder):
        self._wait_until_and_get_elem_by_xpath(self.COPY_CONTEXT_BUTTON).click()
        self._wait_for_elem_by_xpath(self.COPY_POPUP)

        self._wait_until_and_get_elem_by_xpath(self.FOLDER_IN_POPUP.format(to_folder)).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_BUTTON).click()


class Move(Component):
    MORE_BUTTON = '//div[@data-name="more"]'
    MOVE_TOOLBAR_BUTTON = '//div[@data-name="move"]'
    MOVE_CONTEXT_BUTTON = '//div[@id="dropdownList"]//div[@data-name="move"]'
    MOVE_POPUP = '//div[@data-qa-modal="select-folder-dialog-move"]'

    FOLDER_IN_POPUP = '//div[@data-name="/{}" and @class="TreeNode__root--22m4E TreeNode__root_selectDlg--cT_dx"]'
    CONFIRM_BUTTON = '//button[@data-name="action"]'

    def move_from_toolbar(self, to_folder):
        self._wait_until_and_get_elem_by_xpath(self.MORE_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.MOVE_TOOLBAR_BUTTON).click()
        self._wait_for_elem_by_xpath(self.MOVE_POPUP)

        self._wait_until_and_get_elem_by_xpath(self.FOLDER_IN_POPUP.format(to_folder)).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_BUTTON).click()

    def move_from_context(self, to_folder):
        self._wait_until_and_get_elem_by_xpath(self.MOVE_CONTEXT_BUTTON).click()
        self._wait_for_elem_by_xpath(self.MOVE_POPUP)

        self._wait_until_and_get_elem_by_xpath(self.FOLDER_IN_POPUP.format(to_folder)).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_BUTTON).click()


class Rename(Component):
    MORE_BUTTON = '//div[@data-name="more"]'
    RENAME_BUTTON_TOOLBAR = '//div[@data-name="rename"]'
    RENAME_CONTEXT_BUTTON = '//div[@id="dropdownList"]//div[@data-name="rename"]'

    RENAME_INPUT = '//input[@class="layer__input"]'
    SUBMIT_BUTTON = '//button[@data-name="rename"]'

    def rename_file_from_toolbar(self, new_name):
        self._wait_until_and_get_elem_by_xpath(self.MORE_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.RENAME_BUTTON_TOOLBAR).click()
        self._wait_until_and_get_elem_by_xpath(self.RENAME_INPUT).send_keys(new_name)
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def rename_file_from_context(self, new_name):
        self._wait_until_and_get_elem_by_xpath(self.RENAME_CONTEXT_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.RENAME_INPUT).send_keys(new_name)
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()


class Share(Component):
    SHARE_TOOLBAR_BUTTON = '//div[@data-name="publish"]'
    SHARE_CONTEXT_BUTTON = '//div[@id="dropdownList"]//div[@data-name="publish"]'
    SHARE_GRID_BUTTON = '//a[@data-qa-name="{}"]//div[@class="DataListItemThumb__weblink--30Uyy"]'

    SHARE_POPUP = '//div[@data-qa-modal="publish"]'
    GRID_SHARE_POPUP = '//div[@class="Tooltip__overlay--1cWLu"]'
    STOP_SHARE_BUTTON = '//div[@class="PublishNew__close--2iYOO"]'
    START_SHARE_BUTTON = '//div[@class="PublishNew__publish--2f0qP"]'

    def share_from_toolbar(self):
        self._wait_until_and_get_elem_by_xpath(self.SHARE_TOOLBAR_BUTTON).click()
        self._wait_for_elem_by_xpath(self.SHARE_POPUP)

    def share_from_context(self):
        self._wait_until_and_get_elem_by_xpath(self.SHARE_CONTEXT_BUTTON).click()
        self._wait_for_elem_by_xpath(self.SHARE_POPUP)

    def share_from_grid(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.SHARE_GRID_BUTTON.format(filename)).click()
        self._wait_for_elem_by_xpath(self.GRID_SHARE_POPUP)

    def check_if_shared(self):
        return self._check_if_element_exists_by_xpath(self.STOP_SHARE_BUTTON)

    def stop_share(self):
        self._wait_until_and_get_elem_by_xpath(self.STOP_SHARE_BUTTON).click()
        self._wait_for_elem_by_xpath(self.START_SHARE_BUTTON)


class TabsAtHome(Component):
    FROM_MAIL_SELECTOR = '//div[@data-name="/attaches"]'
    INBOX_SELECTOR = '//div[@data-name="0"]'
    TRASH_SELECTOR = '//div[@data-name="/trashbin"]'
    SELECT_ALL_SELECTOR = '//div[@data-name="selectAll"]'
    HELPER_SELECTOR = '//span[@data-icon="ph-icons-video-help"]'
    SHARE_SELECTOR = '//div[@data-name="share"]'

    def open_inbox(self):
        self._wait_until_and_get_elem_by_xpath(self.FROM_MAIL_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.INBOX_SELECTOR).click()

    def select_all_files(self):
        self._wait_until_and_get_elem_by_xpath(self.SELECT_ALL_SELECTOR).click()

    def open_trash(self):
        self._wait_until_and_get_elem_by_xpath(self.TRASH_SELECTOR)

    def open_helper(self):
        self._wait_until_and_get_elem_by_xpath(self.HELPER_SELECTOR)

    def open_share_button(self):
        self._wait_until_and_get_elem_by_xpath(self.SHARE_SELECTOR)


class Buttons(Component):
    VIEW_SELECTOR = '//div[@data-name="view"]'
    SORT_SELECTOR = '//div[@data-name="sort"]'
    LIST_VIEW_SELECTOR = '//div[@data-name="viewList"]'
    THUMBS_VIEW_SELECTOR = '//div[@data-name="viewThumbs"]'

    SORT_BY_ALPHABET_SELECTOR = '//div[@data-name="sortName"]'
    SORT_BY_SIZE_SELECTOR = '//div[@data-name="sortSize"]'
    SORT_BY_DATE_SELECTOR = '//div[@data-name="sortDate"]'

    FILTER_SELECTOR = '//span[@bem-id="69"]'
    FILTER_IMAGE_SELECTOR = '//span[@data-input-name="image"]'
    FILTER_FOLDER_SELECTOR = '//span[@bem-id="102"]'
    FILTER_ALL_SELECTOR = '//span[@data-input-name="all"]'

    def change_view(self):
        self._wait_until_and_get_elem_by_xpath(self.VIEW_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.LIST_VIEW_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.VIEW_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.THUMBS_VIEW_SELECTOR).click()

    def sort_by_alphabet(self):
        self._wait_until_and_get_elem_by_xpath(self.SORT_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.SORT_BY_ALPHABET_SELECTOR).click()

    def sort_by_size(self):
        self._wait_until_and_get_elem_by_xpath(self.SORT_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.SORT_BY_SIZE_SELECTOR).click()

    def sort_by_date(self):
        self._wait_until_and_get_elem_by_xpath(self.SORT_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.SORT_BY_DATE_SELECTOR).click()

    def filter_by_image(self):
        self._wait_until_and_get_elem_by_xpath(self.FILTER_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.FILTER_IMAGE_SELECTOR).click()

    def filter_by_all(self):
        self._wait_until_and_get_elem_by_xpath(self.FILTER_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.FILTER_ALL_SELECTOR).click()

class Directories(Component):
    CREATE_SELECTOR = '//div[@data-name="create"]'
    CREATE_NEW_FOLDER_BUTTON_IN_SELECTOR = '//div[@data-name="createFolder"]'
    FOLDER_NAME_INPUT = '//input[@placeholder="Введите имя папки"]'
    SUBMIT_CREATE_FOLDER_BUTTON = '//div[@class="CreateNewFolderDialog__button--7S1Hs"][1]/button'
    DELETE_FOLDER_BUTTON = '//div[@data-name="remove"]'
    CONFIRM_DELETE_FOLDER_BUTTON = '//div[@class="b-layer__controls__buttons"]/button[@data-name="remove"]'
    DIR_XPATH_BY_NAME = '//a[@data-qa-type="folder" and @data-qa-name="{}"]'

    def create_folder(self, folder_name):
        self._wait_until_and_get_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.CREATE_NEW_FOLDER_BUTTON_IN_SELECTOR).click()
        elem = self._wait_until_and_get_elem_by_xpath(self.FOLDER_NAME_INPUT)
        elem.clear()
        elem.send_keys(folder_name)
        self._wait_until_and_get_elem_by_xpath(self.SUBMIT_CREATE_FOLDER_BUTTON).click()

    def check_folder_exists(self, folder_name):
        return self._check_if_element_exists_by_xpath(self.DIR_XPATH_BY_NAME.format(folder_name))

    def open_folder(self, folder_url):
        self.driver.get(folder_url)

    def delete_folder(self):
        self._wait_until_and_get_elem_by_xpath(self.DELETE_FOLDER_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_DELETE_FOLDER_BUTTON).click()

class Documents(Component):
    CREATE_SELECTOR = '//div[@data-name="create"]'
    REMOVE_SELECTOR = '//div[@data-name="remove"]'
    CREATE_DOCUMENT_SELECTOR = '//div[@data-name="createDocx"]'
    CREATE_PRESENTATION_SELECTOR = '//div[@data-name="createPptx"]'
    CREATE_TABLE_SELECTOR = '//div[@data-name="createXlsx"]'
    DOC_XPATH_BY_NAME = '//a[@data-qa-type="file" and @data-qa-name="{}"]'
    CONFIRM_DELETE_DOC_BUTTON = '//div[@class="b-layer__controls__buttons"]/button[@data-name="remove"]'

    def create_simple_document(self):
        self._wait_until_and_get_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.CREATE_DOCUMENT_SELECTOR).click()

    def create_presentation(self):
        self._wait_until_and_get_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.CREATE_PRESENTATION_SELECTOR).click()

    def create_table(self):
        self._wait_until_and_get_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.CREATE_TABLE_SELECTOR).click()

    def check_document_exists(self, doc_name):
        return self._check_if_element_exists_by_xpath(self.DOC_XPATH_BY_NAME.format(doc_name))

    def delete_doc(self):
        self._wait_until_and_get_elem_by_xpath(self.REMOVE_SELECTOR).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_DELETE_DOC_BUTTON).click()

    def select_file(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.DOC_XPATH_BY_NAME.format(filename)).click()
