from base_classes.component import Component


class NewColumnForm(Component):
    CONTAINER = '//div[@id="addNewColumnButton"]'
    TITLE_INPUT = '//input[@id="inputNewColumnTitle"]'
    CLOSE_BUTTON = '//div[@id="closeNewColumnFormButton"]'
    SUBMIT_BUTTON = '//div[@id="addColumnButton"]'

    def open(self):
        self.driver.find_element_by_xpath(self.CONTAINER).click()

    def close(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def set_title(self, title: str):
        self.driver.find_element_by_xpath(self.TITLE_INPUT).send_keys(title)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()
