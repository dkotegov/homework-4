from base_classes.page import Page
from components.boards.create_board_form import CreateBoardForm
from components.boards.boards_list import BoardsList


class BoardsPage(Page):
    PATH = 'boards'
    CONTAINER = '//div[@class="boards"]'

    @property
    def create_board_form(self):
        return CreateBoardForm(self.driver)

    @property
    def boards_list(self):
        return BoardsList(self.driver)

    def create_board(self, title: str):
        self.create_board_form.open()
        self.create_board_form.set_board_title(title)
        self.create_board_form.submit()

