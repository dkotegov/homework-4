from selenium.webdriver.support.ui import WebDriverWait
from tests.folder_tests.page_component import Page, Component


class MainPage(Page):
    PATH = ''

    @property
    def add_folder_form(self):
        return AddFolderForm(self.driver)

    @property
    def remove_folder_form(self):
        return RemoveFolderForm(self.driver)

    @property
    def main_form(self):
        return MainForm(self.driver)


class MainForm(Component):
    CREATE_BUTTON = '//span[text()="Добавить папку"]'
    REMOVE_BUTTON = '//*[@data-test-id="folder-delete"]'
    INBOX = '//a[@class="c01150 c01154"]'

    def add_folder_popup(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_BUTTON)
        )
        button.click()

    def remove_folder_popup(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.REMOVE_BUTTON)
        )
        button.click()

    def click_inbox(self):
        self.driver.find_element_by_class_name(self.INBOX).click()


class AddFolderForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = 'c01420'
    FOLDER_FRAME = '//input[@name="name"]'
    ADD_FOLDER_BUTTON = '//*[@data-test-id="submit"]'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_class_name(self.CROSS_BUTTON).click()

    def create_folder(self, folder_name):
        self.driver.find_element_by_xpath(self.FOLDER_FRAME).send_keys(folder_name)
        self.driver.find_element_by_xpath(self.ADD_FOLDER_BUTTON).click()


class RemoveFolderForm(Component):
    CLOSE_BUTTON = '//span[text()="Отменить"]'
    CROSS_BUTTON = 'c01420'
    DELETE_FOLDER_BUTTON = '//*[@data-test-id="submit"]'

    def close_folder_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def close_folder_popup_by_cross(self):
        self.driver.find_element_by_class_name(self.CROSS_BUTTON).click()

    def remove_folder(self, folder_name):
        self.driver.find_element_by_xpath(self.DELETE_FOLDER_BUTTON).click()
