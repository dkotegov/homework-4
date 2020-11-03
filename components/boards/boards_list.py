from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class BoardsList(Component):
    BOARD_TITLE = '//div[@class="group-mini-board__title"]'

    def get_board(self, title: str):
        boards = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_elements_by_xpath(self.BOARD_TITLE)
        )

        for i in range(len(boards)):
            if boards[i].text == title:
                return boards[i]
        return None

    def open_board(self, title: str):
        board = self.get_board(title)
        if board is None:
            raise Exception('Board is  not found')

        board.click()
