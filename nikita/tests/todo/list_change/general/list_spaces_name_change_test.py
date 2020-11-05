from nikita.tests.todo.list_change.default import ListChangeTest
from nikita.pages.todo.list import ListPage

class ListSpacesNameChangeTest(ListChangeTest):
    NEW_LIST_NAME = '   '

    def test(self):
        page = ListPage(self.driver)
        page.change_name(self.NEW_LIST_NAME)
        page.wait_for_name(self.NEW_LIST_NAME)
        self.LIST_NAME = self.NEW_LIST_NAME
