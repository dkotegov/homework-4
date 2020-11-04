from base_classes.component import Component
from components.board.columns.column import Column
from components.board.columns.new_column_form import NewColumnForm


class ColumnsList(Component):
    CONTAINER = '//div[@class="column-list"]'

    @property
    def new_column_form(self):
        return NewColumnForm(self.driver)

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
