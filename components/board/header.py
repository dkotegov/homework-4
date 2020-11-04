from base_classes.component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Header(Component):
    BOARD_TITLE = '//div[@class="board-header-left__title"]'
    BOARD_SETTINGS_BUTTON = '//div[contains(@class, "js-openBoardSettings")]'

    def check_title(self, title):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: d.find_element_by_xpath(self.BOARD_TITLE).text == title
            )
        except TimeoutException:
            return False
        return True

    def open_settings(self):
        self.driver.find_element_by_xpath(self.BOARD_SETTINGS_BUTTON).click()
