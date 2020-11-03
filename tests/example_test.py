# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def _wait_until_and_click_elem_by_xpath(self, elem):
        return WebDriverWait(self.driver, 120, 0.1).until(EC.visibility_of_element_located((By.XPATH, elem)))

    def _wait_for_url(self, url):
        return WebDriverWait(self.driver, 120, 0.1).until(EC.url_to_be(url))

    def _check_if_element_exists_by_xpath(self, elem):
        try:
            WebDriverWait(self.driver, 1, 0.1).until(EC.visibility_of_all_elements_located((By.XPATH, elem)))
        except TimeoutException:
            return False
        return True


class Page(object):
    BASE_URL = 'https://account.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthForm(Component):
    LOGIN = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[@data-test-id="submit-button"]'
    NEXT_BUTTON = '//button[@data-test-id="next-button"]'
    LOGIN_BUTTON = '//a[text()="Войти"]'

    def set_login(self, login):
        self._wait_until_and_click_elem_by_xpath(self.LOGIN).send_keys(login)

    def click_next(self):
        self._wait_until_and_click_elem_by_xpath(self.NEXT_BUTTON).click()

    def set_password(self, pwd):
        self._wait_until_and_click_elem_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self._wait_until_and_click_elem_by_xpath(self.SUBMIT).click()

    def wait_for_cookie(self):
        self._wait_for_url('https://e.mail.ru/inbox/?afterReload=1')


class Directories(Component):
    CREATE_SELECTOR = '//div[@data-name="create"]'
    CREATE_NEW_FOLDER_BUTTON_IN_SELECTOR = '//div[@data-name="createFolder"]'
    FOLDER_NAME_INPUT = '//input[@placeholder="Введите имя папки"]'
    SUBMIT_CREATE_FOLDER_BUTTON = '//div[@class="CreateNewFolderDialog__button--7S1Hs"][1]/button'
    DELETE_FOLDER_BUTTON = '//div[@data-name="remove"]'
    CONFIRM_DELETE_FOLDER_BUTTON = '//div[@class="b-layer__controls__buttons"]/button[@data-name="remove"]'
    DIR_XPATH_BY_NAME = '//a[@data-qa-type="folder" and @data-qa-name="{}"]'

    def create_folder(self, folder_name):
        self._wait_until_and_click_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.CREATE_NEW_FOLDER_BUTTON_IN_SELECTOR).click()
        elem = self._wait_until_and_click_elem_by_xpath(self.FOLDER_NAME_INPUT)
        elem.clear()
        elem.send_keys(folder_name)
        self._wait_until_and_click_elem_by_xpath(self.SUBMIT_CREATE_FOLDER_BUTTON).click()

    def check_folder_exists(self, folder_name):
        return self._check_if_element_exists_by_xpath(self.DIR_XPATH_BY_NAME.format(folder_name))

    def open_folder(self, folder_url):
        self.driver.get(folder_url)

    def delete_folder(self):
        self._wait_until_and_click_elem_by_xpath(self.DELETE_FOLDER_BUTTON).click()
        self._wait_until_and_click_elem_by_xpath(self.CONFIRM_DELETE_FOLDER_BUTTON).click()


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
        self._wait_until_and_click_elem_by_xpath(self.VIEW_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.LIST_VIEW_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.VIEW_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.THUMBS_VIEW_SELECTOR).click()

    def sort_by_alphabet(self):
        self._wait_until_and_click_elem_by_xpath(self.SORT_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.SORT_BY_ALPHABET_SELECTOR).click()

    def sort_by_size(self):
        self._wait_until_and_click_elem_by_xpath(self.SORT_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.SORT_BY_SIZE_SELECTOR).click()

    def sort_by_date(self):
        self._wait_until_and_click_elem_by_xpath(self.SORT_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.SORT_BY_DATE_SELECTOR).click()

    def filter_by_image(self):
        self._wait_until_and_click_elem_by_xpath(self.FILTER_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.FILTER_IMAGE_SELECTOR).click()

    def filter_by_all(self):
        self._wait_until_and_click_elem_by_xpath(self.FILTER_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.FILTER_ALL_SELECTOR).click()


class CreatingDocuments(Component):
    CREATE_SELECTOR = '//div[@data-name="create"]'
    REMOVE_SELECTOR = '//div[@data-name="remove"]'
    CREATE_DOCUMENT_SELECTOR = '//div[@data-name="createDocx"]'
    CREATE_PRESENTATION_SELECTOR = '//div[@data-name="createPptx"]'
    CREATE_TABLE_SELECTOR = '//div[@data-name="createXlsx"]'
    DOC_XPATH_BY_NAME = '//a[@data-qa-type="file" and @data-qa-name="{}"]'
    CONFIRM_DELETE_DOC_BUTTON = '//div[@class="b-layer__controls__buttons"]/button[@data-name="remove"]'

    def create_simple_document(self):
        self._wait_until_and_click_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.CREATE_DOCUMENT_SELECTOR).click()

    def create_presentation(self):
        self._wait_until_and_click_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.CREATE_PRESENTATION_SELECTOR).click()

    def create_table(self):
        self._wait_until_and_click_elem_by_xpath(self.CREATE_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.CREATE_TABLE_SELECTOR).click()

    def check_document_exists(self, doc_name):
        return self._check_if_element_exists_by_xpath(self.DOC_XPATH_BY_NAME.format(doc_name))

    def delete_doc(self):
        self._wait_until_and_click_elem_by_xpath(self.REMOVE_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.CONFIRM_DELETE_DOC_BUTTON).click()

    def select_file(self, filename):
        self._wait_until_and_click_elem_by_xpath(self.DOC_XPATH_BY_NAME.format(filename)).click()


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    def auth(self, login, password):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.form.set_login(login)
        auth_page.form.click_next()
        auth_page.form.set_password(password)
        auth_page.form.submit()
        auth_page.form.wait_for_cookie()


class Banners(Component):
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


class TabsAtHomePage(Component):
    FROM_MAIL_SELECTOR = '//div[@data-name="/attaches"]'
    INBOX_SELECTOR = '//div[@data-name="0"]'
    TRASH_SELECTOR = '//div[@data-name="/trashbin"]'
    SELECT_ALL_SELECTOR = '//div[@data-name="selectAll"]'
    HELPER_SELECTOR = '//span[@data-icon="ph-icons-video-help"]'
    SHARE_SELECTOR = '//div[@data-name="share"]'

    def open_inbox(self):
        self._wait_until_and_click_elem_by_xpath(self.FROM_MAIL_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.INBOX_SELECTOR).click()

    def select_all_files(self):
        self._wait_until_and_click_elem_by_xpath(self.SELECT_ALL_SELECTOR).click()

    def open_trash(self):
        self._wait_until_and_click_elem_by_xpath(self.TRASH_SELECTOR)

    def open_helper(self):
        self._wait_until_and_click_elem_by_xpath(self.HELPER_SELECTOR)

    def open_share_button(self):
        self._wait_until_and_click_elem_by_xpath(self.SHARE_SELECTOR)


class HomePage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home/'

    @property
    def folders(self):
        return Directories(self.driver)

    @property
    def tabs_at_home_p(self):
        return TabsAtHomePage(self.driver)

    @property
    def banners(self):
        return Banners(self.driver)

    @property
    def buttons(self):
        return Buttons(self.driver)

    @property
    def creating_documents(self):
        return CreatingDocuments(self.driver)

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class DirectoryTest(unittest.TestCase):
    USEREMAIL = 'adolgavintest@mail.ru'
    PASSWORD = 'homework1234'

    def setUp(self):
        browser = 'CHROME'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.USEREMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_create_directory(self):
        dir_name = "directory_test"

        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()

        home_page.folders.create_folder(dir_name)

        home_page.open()
        self.assertTrue(home_page.folders.check_folder_exists(dir_name))

        home_page.banners.close_mini_banner_if_exists()
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)

        home_page.folders.delete_folder()
        home_page.open()

    def test_create_subdirectory(self):
        dir_name = "directory_test"
        subdir_name = "subdirectory_test"
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()
        home_page.folders.create_folder(dir_name)
        home_page.open()
        self.assertTrue(home_page.folders.check_folder_exists(dir_name))
        home_page.banners.close_mini_banner_if_exists()
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)

        home_page.folders.create_folder(subdir_name)
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)
        self.assertTrue(home_page.folders.check_folder_exists(subdir_name))
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name + "/" + subdir_name)
        home_page.folders.delete_folder()
        home_page.folders.open_folder(home_page.BASE_URL + home_page.PATH + dir_name)
        home_page.folders.delete_folder()


class SortAndFilterTest(unittest.TestCase):
    USEREMAIL = 'adolgavintest@mail.ru'
    PASSWORD = 'homework1234'

    def setUp(self):
        browser = 'CHROME'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.USEREMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_buttons(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()
        home_page.buttons.change_view()

        home_page.buttons.sort_by_alphabet()
        home_page.buttons.sort_by_size()
        home_page.buttons.sort_by_date()

        home_page.buttons.filter_by_image()
        home_page.buttons.filter_by_all()


class CreatingDocumentsTest(unittest.TestCase):
    USEREMAIL = 'adolgavintest@mail.ru'
    PASSWORD = 'homework1234'

    DOC_NAME = 'Новый документ.docx'
    PRES_NAME = 'Новая презентация.pptx'
    TABLE_NAME = 'Новая таблица.xlsx'

    def setUp(self):
        browser = 'CHROME'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.USEREMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_create_doc(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()

        home_page.creating_documents.create_simple_document()

        self.driver.switch_to_window(self.driver.window_handles[0])

        home_page.creating_documents.select_file(self.DOC_NAME)
        self.assertTrue(home_page.creating_documents.check_document_exists(self.DOC_NAME))
        home_page.banners.close_buy_cloud_banner_if_exists()
        home_page.creating_documents.delete_doc()

    def test_create_pres(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()
        home_page.banners.close_mini_banner_if_exists()
        home_page.creating_documents.create_presentation()

        self.driver.switch_to_window(self.driver.window_handles[0])

        home_page.creating_documents.select_file(self.PRES_NAME)
        self.assertTrue(home_page.creating_documents.check_document_exists(self.PRES_NAME))
        home_page.banners.close_buy_cloud_banner_if_exists()
        home_page.creating_documents.delete_doc()

    def test_create_table(self):
        home_page = HomePage(self.driver)
        home_page.open()

        home_page.banners.close_banner_if_exists()
        home_page.creating_documents.create_table()

        self.driver.switch_to_window(self.driver.window_handles[0])

        home_page.creating_documents.select_file(self.TABLE_NAME)
        self.assertTrue(home_page.creating_documents.check_document_exists(self.TABLE_NAME))
        home_page.banners.close_buy_cloud_banner_if_exists()
        home_page.creating_documents.delete_doc()


class TabsAtHomePageTest(unittest.TestCase):
    USEREMAIL = 'adolgavintest@mail.ru'
    PASSWORD = 'homework1234'

    DOC_NAME = 'Новый документ.docx'
    PRES_NAME = 'Новая презентация.pptx'
    TABLE_NAME = 'Новая таблица.xlsx'

    def setUp(self):
        browser = 'CHROME'

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.auth(self.USEREMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_box(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_inbox()

    def test_select_files(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.select_all_files()

    def test_open_trash(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_trash()

    def test_open_trash(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_trash()

    def test_open_helper(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_helper()

    def test_open_share(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.banners.close_banner_if_exists()
        home_page.tabs_at_home_p.open_share_button()
