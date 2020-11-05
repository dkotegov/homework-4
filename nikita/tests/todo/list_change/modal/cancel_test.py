from nikita.tests.todo.list_change.default import ListChangeTest
from nikita.pages.todo.list import ListPage
from nikita.constants import LIST_DESCRIPTION_PLACEHOLDER

class ListCancelChangeTest(ListChangeTest):
    NEW_LIST_NAME = 'kek'
    DESCRIPTION = 'topkek'

    def test(self):
        page = ListPage(self.driver)
        page.change_all_and_cancel_modal(self.NEW_LIST_NAME, self.DESCRIPTION)
        page.wait_for_name(self.LIST_NAME)
        page.wait_for_description(LIST_DESCRIPTION_PLACEHOLDER)
