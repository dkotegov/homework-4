from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class CreateColumnForm(Component):
    CONTAINER = '//div[@id="addNewColumnButton"]'
    TITLE_INPUT = '//input[@id="inputNewColumnTitle"]'
    CLOSE_BUTTON = '//div[@id="closeNewColumnFormButton"]'
    SUBMIT_BUTTON = '//div[@id="addColumnButton"]'

    CLOSED_FORM = '//div[@class="column-list-add-column-button js-addNewColumn"]'

    def open(self):
        self.driver.find_element_by_xpath(self.CONTAINER).click()

    def close(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

    def set_title(self, title: str):
        self.driver.find_element_by_xpath(self.TITLE_INPUT).send_keys(title)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def wait_for_closed(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_elements_by_xpath(self.CLOSED_FORM)
        )
