from base_classes.page import Page
from components.board.columns.columns_list import ColumnsList
from components.board.header import Header
from components.board.settings_popup import SettingsPopup


class BoardPage(Page):
    CONTAINER = '//div[@class="board"]'

    @property
    def header(self):
        return Header(self.driver)

    @property
    def settings_popup(self) -> SettingsPopup:
        return SettingsPopup(self.driver)

    @property
    def columns_list(self) -> ColumnsList:
        return ColumnsList(self.driver)

    def open(self):
        raise NotImplementedError('You have to open board from boards page')
