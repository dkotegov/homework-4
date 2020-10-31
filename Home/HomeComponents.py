from Base import Component


class Utils(Component):
    BANNER = '//div[@data-qa-modal]'
    CLOSE_BANNER_BUTTON = '//*[local-name() = "svg" and @class="Dialog__close--1rKyk"]'

    def close_banner_if_exists(self):
        banner_exists = self._check_if_element_exists_by_xpath(self.BANNER)
        if banner_exists:
            self.driver.find_element_by_xpath(self.CLOSE_BANNER_BUTTON).click()


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
        self._wait_until_and_get_elem_by_xpath(self.FOLDER_NAME_INPUT).send_keys(folder_name)
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

    DELETE_BUTTON = '//div[@data-name="remove"]'
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

    def select_file(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.FILE_BY_NAME.format(filename)).click()

    def unselect_file(self):
        self._wait_until_and_get_elem_by_xpath(self.WORKSPACE).click()

    def delete_file(self):
        self._wait_until_and_get_elem_by_xpath(self.DELETE_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.CONFIRM_DELETE_BUTTON).click()


class FileHistory(Component):
    MORE_BUTTON = '//div[@data-name="more"]'
    HISTORY_BUTTON = '//div[@data-name="history"]'
    HISTORY_POPUP = '//div[@data-bem="b-file-history"]'
    HISTORY_FILES = '//div[@class="b-collection__item b-collection__item_file-history b-collection__item_axis-y"]'
    CLOSE_HISTORY_BUTTON = '//div[@data-bem="b-file-history"]//button[@data-name="close"]'

    def open_history(self):
        self._wait_until_and_get_elem_by_xpath(self.MORE_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.HISTORY_BUTTON).click()
        self._wait_for_elem_by_xpath(self.HISTORY_POPUP)
        self._wait_for_elem_by_xpath(self.HISTORY_FILES)

    def count_history_files(self):
        files = self.driver.find_elements_by_xpath(self.HISTORY_FILES)
        return len(files)

    def close_history(self):
        self._wait_until_and_get_elem_by_xpath(self.CLOSE_HISTORY_BUTTON).click()
