from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.base import Page
from tests.pages.component import FormComponent


class CreatePinPage(Page):
    PATH = '/create_pin'

    ROOT = {
        'method': By.XPATH,
        'key': Page.get_xpath_visible('//div[@id="createpin-page"]')
    }

    def __init__(self, driver):
        Page.__init__(self, driver)
        self.open()

    @property
    def form_list(self):
        return FindCreatePinForm(self.driver)

    @property
    def form_concrete(self):
        return ConcreteUserMessagesForm(self.driver)


class FindCreatePinForm(FormComponent):
    pin_name = '//input[@id="pinname"]'
    pin_content = '//input[@id="pincontent"]'
    error_line = '//div[@id="createPinError"]'
    create_pin_button = '//input[@class="createpin__buttons__button-save createpin__buttons__button-save_pos"]'
    boards_list = '//select[@id="createPinBoardSelect"]'
    change_pin_button_click = '//div[@id="createPinBoardSelect"]'
    create_board_button = '//div[@id="createPinCreateBoard"]'
    load_file_button = '//input[@id="pinphoto"]'

    def set_pin_name(self, query):
        self.fill_input(self.driver.find_element_by_xpath(self.pin_name), query)

    def set_pin_content(self, query):
        self.fill_input(self.driver.find_element_by_xpath(self.pin_content), query)

    def go_to_create_board(self):
        self.driver.find_element_by_xpath(self.create_board_button).click()

    def create_pin(self):
        self.driver.find_element_by_xpath(self.create_pin_button).click()

    def get_error(self):
        return self.driver.find_element_by_xpath(self.error_line).text

    def load_file(self, path):
        self.driver.find_element(by=By.ID, value="pinphoto").send_keys(path)


class ConcreteUserMessagesForm(FormComponent):
    section_name = '//div[@id="profilePinsBoardsView"]'
    boards_list = '//div[@class="board-for-user-view__content"]'

    def wait_for_load(self):
        self.wait_for_presence(By.XPATH, self.section_name)

    def get_boards_list(self):
        return self.driver.find_elements_by_xpath(self.boards_list)
