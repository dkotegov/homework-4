from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from base_classes.component import Component


class Column(Component):
    CONTAINER = '//div[@class="board-column"]'
    TITLE_INPUT = '//input[contains(@class, "js-updateColumn")]'

    def __init__(self, driver: WebDriver, column_id: int):
        Component.__init__(self, driver)
        self.CONTAINER = f'//div[@class="board-column" and @data-column-id="{column_id}"]'
        self.TITLE_INPUT = f'//input[contains(@class, "js-updateColumn") and @data-column-id="{column_id}"]'
        self.DELETE_BUTTON = f'//div[contains(@class, "js-deleteColumn") and @data-column-id="{column_id}"]'
        self.column_id = column_id

    def set_title(self, title: str):
        title_input = self.driver.find_element_by_xpath(self.TITLE_INPUT)
        title_input.clear()
        title_input.send_keys(title, Keys.ENTER)

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()

    def get_title(self) -> str:
        return self.driver.find_element_by_xpath(self.TITLE_INPUT).get_attribute('value')
