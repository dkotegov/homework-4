from selenium.webdriver.common.by import By

from tests.pages.base import Page
from tests.pages.component import FormComponent


class CreatePinPage(Page):
    PATH = "/create_pin"

    ROOT = {
        "method": By.XPATH,
        "key": Page.get_xpath_visible('//div[@id="createpin-page"]'),
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
    create_pin_button = '//input[@id="createpinViewButtonsOk"]'
    boards_list = '//select[@id="createPinBoardSelect"]'
    change_pin_button_click = '//div[@id="createPinBoardSelect"]'
    create_board_button = '//div[@id="createPinCreateBoard"]'
    load_file_button = '//input[@id="pinphoto"]'
    section_name = '//div[@id="createpin-page"]'
    profile_section_name = '//div[@id="profile-page"]'
    back_button = '//a[@id="createPinViewButtonsExit"]'

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

    def set_select_board(self, board_id):
        select = self.driver.find_element_by_id("createPinBoardSelect")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("value") == board_id:
                option.click()
                return

    def select_board(self, board_id):
        self.driver.find_element(by=By.ID, value="boardViewPins/board/" + board_id)

    def wait_for_load(self):
        self.wait_for_presence(By.XPATH, self.section_name)

    def wait_for_load_profile(self):
        self.wait_for_presence(By.XPATH, self.profile_section_name)

    def go_back(self):
        self.driver.find_element_by_xpath(self.back_button).click()


class ConcreteUserMessagesForm(FormComponent):
    section_name = '//div[@id="createpin-page"]'
    boards_list = '//div[@class="board-for-user-view__content"]'

    def wait_for_load(self):
        self.wait_for_presence(By.XPATH, self.section_name)

    def get_boards_list(self):
        return self.driver.find_elements_by_xpath(self.boards_list)
