from base_classes.component import Component
from components.board.columns.column import Column
from components.board.columns.create_column_form import CreateColumnForm


class ColumnsList(Component):
    CONTAINER = '//div[@class="column-list"]'

    @property
    def create_column_form(self):
        return CreateColumnForm(self.driver)

    def create_column(self, title: str):
        self.create_column_form.open()
        self.create_column_form.set_title(title)
        self.create_column_form.submit()
        self.create_column_form.wait_for_closed()

    def get_column_by_title(self, title: str) -> [Column, None]:
        columns = self.driver.find_elements_by_xpath(Column.CONTAINER)

        column_id = None
        for i in range(len(columns)):
            raw_column = columns[i]
            column_title = raw_column.find_element_by_xpath(Column.TITLE_INPUT).get_attribute('value')
            if column_title == title:
                column_id = int(raw_column.get_attribute('data-column-id'))
                break

        if column_id is None:
            return None

        return Column(self.driver, column_id)
