from nikita.tests.todo.list_change.default import ListChangeTest
from nikita.pages.todo.list import ListPage

class ListSpacesNameChangeTest(ListChangeTest):
    NEW_LIST_NAME = '   '

    def test(self):
        page = ListPage(self.driver)
        page.change_name_modal(self.NEW_LIST_NAME)
        page.refresh()
        page.wait_for_name(self.NEW_LIST_NAME)
        self.LIST_NAME = self.NEW_LIST_NAME
