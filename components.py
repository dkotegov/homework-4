# -*- coding: utf-8 -*-
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '//*[@id="ph_login"]'
    PASSWORD = '//*[@id="ph_password"]'

    @property
    def submit(self):
        return SubmitLoginButton(self.driver)

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)


class UploadForm(Component):
    @property
    def close(self):
        return CloseUploadFormButton(self.driver)

    @property
    def input_file(self):
        return FileInput(self.driver)

    @property
    def drag_and_drop(self):
        return DragAndDrop(self.driver)


class UserName(Component):
    USERNAME = '//*[@id="PH_user-email"]'
    EXIT_BUTTON = '//*[@id="PH_logoutLink"]'

    def get(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )


class DeleteSubmitDialog(Component):
    @property
    def delete_submit(self):
        return DeleteSubmitButton(self.driver)


class FolderCreateWindow(Component):
    INPUT = '//input[@class="layer__input"]'

    @property
    def add(self):
        return AddFolderButton(self.driver)

    def set_name(self, name):
        self.driver.find_element_by_xpath(self.INPUT).send_keys(name)


class CreateDropdown(Component):
    @property
    def folder(self):
        return CreateFolderButton(self.driver)

    def folder_window(self):
        return FolderCreateWindow(self.driver)


class WindowWithCreateFolderButton(Component):
    @property
    def create_folder(self):
        return CreateFolderInCopyButton(self.driver)

    @property
    def folder_window(self):
        return FolderCreateWindow(self.driver)


class CopyWindow(WindowWithCreateFolderButton):
    @property
    def copy(self):
        return DoCopyButton(self.driver)

    def select_folder_for_copy(self, folder_name):
        if folder_name == 'CLOUD':
            FOLDER = '//div[@class="layer_copy__folder"]//div[@data-name="Облако"]//span[@class="b-nav__item__text"]'
        else:
            FOLDER = '//div[@class="layer_copy__folder"]//a[@href="/home/' + folder_name + '/"]'
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, FOLDER)))
        self.driver.find_element_by_xpath(FOLDER).click()


class MoveWindow(WindowWithCreateFolderButton):
    @property
    def move(self):
        return DoMoveButton(self.driver)

    def select_folder_for_move(self, folder_name):
        if folder_name == 'CLOUD':
            FOLDER = '//div[@class="layer_move__folder"]//div[@data-name="Облако"]//span[@class="b-nav__item__text"]'
        else:
            FOLDER = '//div[@class="layer_move__folder"]//a[@href="/home/' + folder_name + '/"]'
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, FOLDER)))
        self.driver.find_element_by_xpath(FOLDER).click()


class RenameWindow(Component):
    INPUT = '//input[@class="layer__input"]'

    @property
    def rename(self):
        return DoRenameButton(self.driver)

    def set_name(self, name):
        self.driver.find_element_by_xpath(self.INPUT).send_keys(name)


class MoreDropdown(Component):
    @property
    def copy(self):
        return CopyElementButton(self.driver)

    def copy_window(self):
        return CopyWindow(self.driver)

    @property
    def move(self):
        return MoveElementButton(self.driver)

    def move_window(self):
        return MoveWindow(self.driver)

    @property
    def rename(self):
        return RenameElementButton(self.driver)

    def rename_window(self):
        return RenameWindow(self.driver)


class ToolbarGroup(Component):
    @property
    def checkbox(self):
        return SelectAllCheckbox(self.driver)

    @property
    def delete(self):
        return DeleteButton(self.driver)

    @property
    def delete_window(self):
        return DeleteSubmitDialog(self.driver)

    LABEL_FOR_EMPTY = '//div[@class="b-datalist__empty__block"]'

    def cloud_is_empty(self):
        return EC.presence_of_element_located(self.LABEL_FOR_EMPTY)

    # Oleg
    @property
    def more(self):
        return MoreButton(self.driver)

    @property
    def more_dropdown(self):
        return MoreDropdown(self.driver)


class Button(Component):
    BUTTON = ''
    CHECK_ELEMENT = ''

    def go(self, invisible=None):
        self.is_clickable()
        self.do_click()
        if invisible:
            self.check_invisible()
        else:
            self.check_click()

    def is_clickable(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON))
            # EC.visibility_of_element_located((By.XPATH, self.BUTTON))
        )

    def do_click(self):
        self.driver.find_element_by_xpath(self.BUTTON).click()

    def check_click(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CHECK_ELEMENT))
        )

    def check_invisible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.CHECK_ELEMENT))
        )


class Input(Component):
    INPUT = ''
    DIR_NAME = os.path.dirname(__file__) + "/files_for_upload/"

    def go(self, file_name, path=None, invisible=None):
        self.send_file(file_name)
        if None == path:
            path = ''
        if invisible:
            self.check_file_not_located(file_name, path)
        else:
            self.check_file_located(file_name, path)

    def is_visibility(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.INPUT))
        )

    def send_file(self, filename):
        self.driver.find_element_by_xpath(self.INPUT).send_keys(self.DIR_NAME + filename)

    def check_file_located(self, filename, path):
        CHECK_UPLOAD = '//*[@data-id="/' + path + filename + '"]'
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, CHECK_UPLOAD))
        )

    def check_file_not_located(self, filename, path):
        CHECK_UPLOAD = '//*[@data-id="/' + path + filename + '"]'
        return WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, CHECK_UPLOAD))
        )


class InputName(Input):
    DIR_NAME = ''


class DragAndDrop(Input):
    INPUT = '//input[@class="drop-zone__input"]'


class FileInput(Input):
    INPUT = '//input[@class="layer_upload__controls__input"]'


class EnterButton(Button):
    BUTTON = '//*[@id="PH_authLink"]'
    CHECK_ELEMENT = '//*[@id="ph_login"]'


class SubmitLoginButton(Button):
    BUTTON = '//span[@data-action="login"]'
    CHECK_ELEMENT = '//span[@data-name="home"]'


class UploadButton(Button):
    BUTTON = '//*[@id="cloud_toolbars"]//*[@data-name="upload"]/span'
    CHECK_ELEMENT = '//div[@class="layer_upload"]'


class CloseUploadFormButton(Button):
    BUTTON = "//div[@class='b-layer__placeholder']/button[@data-name='close']"
    CHECK_ELEMENT = '//span[@data-name="home"]'


class SelectAllCheckbox(Button):
    BUTTON = '//div[@data-name="toggleBtn"]'
    CHECK_ELEMENT = '//div[@data-name="remove"]'


class DeleteButton(Button):
    BUTTON = '//div[@data-name="remove"]'
    CHECK_ELEMENT = '//div[@class="b-layer__container"]'


class DeleteSubmitButton(Button):
    BUTTON = '//button[@data-name="remove"]'
    CHECK_ELEMENT = '//div[@data-name="share"]'


# Oleg
class MoreButton(Button):
    BUTTON = '//div[@data-group="more"]'
    CHECK_ELEMENT = '//a[@data-name="copy"]'


class CopyElementButton(Button):
    BUTTON = '//a[@data-name="copy"]'
    CHECK_ELEMENT = '//div[@class="layer_copy"]'


class MoveElementButton(Button):
    BUTTON = '//a[@data-name="move"]'
    CHECK_ELEMENT = '//div[@class="layer_move"]'


class RenameElementButton(Button):
    BUTTON = '//a[@data-name="rename"]'
    CHECK_ELEMENT = '//div[@class="layer_rename"]'


class DoCopyButton(Button):
    BUTTON = '//button[@data-name="copy"]'
    CHECK_ELEMENT = '//div[@data-name="share"]'


class DoMoveButton(Button):
    BUTTON = '//button[@data-name="move"]'
    CHECK_ELEMENT = '//div[@data-name="share"]'


class DoRenameButton(Button):
    BUTTON = '//button[@data-name="rename"]'
    CHECK_ELEMENT = '//div[@data-name="share"]'


class CreateFolderInCopyButton(Button):
    BUTTON = '//button[@data-name="create-folder"]'
    CHECK_ELEMENT = '//div[@class="layer_add"]'


class CreateButton(Button):
    BUTTON = '//div[@data-group="create"]'
    CHECK_ELEMENT = '//a[@data-name="folder"]'


class CreateFolderButton(Button):
    BUTTON = '//a[@data-name="folder"]'
    CHECK_ELEMENT = '//div[@class="layer_add"]'


class AddFolderButton(Button):
    BUTTON = '//button[@data-name="add"]'
    CHECK_ELEMENT = '//div[@class="b-layer__root"]'
