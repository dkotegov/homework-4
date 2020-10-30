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
