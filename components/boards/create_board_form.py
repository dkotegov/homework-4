from base_classes.component import Component


class CreateBoardForm(Component):
    FORM = '//div[@class="group-board-create"]'
    OPEN_FORM_BUTTON = '//div[@id="addBoard"]'
    CLOSE_FORM_BUTTON = '//div[@id="closeForm"]'
    BOARD_TITLE_INPUT = '//input[@id="inputNewBoardTitle"]'
    SUBMIT_BUTTON = '//div[@id="submitAddBoard"]'

    def open(self):
        self.driver.find_element_by_xpath(self.OPEN_FORM_BUTTON).click()

    def close(self):
        self.driver.find_element_by_xpath(self.CLOSE_FORM_BUTTON).click()

    def set_board_title(self, title: str):
        self.driver.find_element_by_xpath(self.BOARD_TITLE_INPUT).send_keys(title)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()
