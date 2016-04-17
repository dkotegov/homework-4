# -*- coding: utf-8 -*-
import urlparse
from components import *
# from inputs import *

############
# Pages
############


class Page(object):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = ''
    PATH_TO_FILE = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def check_file_located(self, filename):
        CHECK_ELEMENT = '//*[@data-id="/' + self.PATH_TO_FILE + filename + '"]'
        self.open()
        print CHECK_ELEMENT
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, CHECK_ELEMENT))
        )

    def check_file_not_located(self, filename):
        CHECK_ELEMENT = '//*[@data-id="/' + self.PATH_TO_FILE + filename + '"]'
        self.open()
        print CHECK_ELEMENT
        return WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, CHECK_ELEMENT))
        )


class AuthPage(Page):
    PATH = ''
    PATH_TO_FILE = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def enter(self):
        return EnterButton(self.driver)


class HomePage(Page):
    PATH = 'home/'
    PATH_TO_FILE = ''

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)


    @property
    def form(self):
        return UploadForm(self.driver)

    @property
    def user_name(self):
        return UserName(self.driver)

    @property
    def upload(self):
        return UploadButton(self.driver)

    @property
    def create(self):
        return CreateButton(self.driver)

    @property
    def create_dropdown(self):
        return CreateDropdown(self.driver)

    @property
    def toolbar_buttons(self):
        return ToolbarGroup(self.driver)

    def select_file(self, full_path):
        CHECKBOX = "//span[@data-name='ctrl']/div[@data-id='/" + full_path + "']"
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, CHECKBOX)))
        self.driver.find_element_by_xpath(CHECKBOX).click()


class FolderPage(HomePage):
    def __init__(self, name, driver):
        super(FolderPage, self).__init__(driver)
        self.NAME = name
        self.PATH_TO_FILE = name + '/'
        self.PATH = HomePage.PATH + self.PATH_TO_FILE


class File(object):
    NAME = ''
    PATH = ''

    def __init__(self, name, path):
        self.NAME = name
        self.PATH = path
