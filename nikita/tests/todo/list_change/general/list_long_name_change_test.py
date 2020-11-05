from nikita.tests.todo.list_change.default import ListChangeTest
from nikita.pages.todo.list import ListPage
from nikita.constants import LIST_LONG_NAME

class ListLongNameChangeTest(ListChangeTest):
    def test(self):
        page = ListPage(self.driver)
        page.change_name(LIST_LONG_NAME)
        page.refresh()
        page.wait_for_name(self.LIST_NAME)
