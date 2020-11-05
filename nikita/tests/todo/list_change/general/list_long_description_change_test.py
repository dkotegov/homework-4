from nikita.tests.todo.list_change.default import ListChangeTest
from nikita.pages.todo.list import ListPage
from nikita.constants import LIST_LONG_DESCRIPTION, LIST_DESCRIPTION_PLACEHOLDER

class ListLongDescriptionChangeTest(ListChangeTest):
    def test(self):
        page = ListPage(self.driver)
        page.change_description(LIST_LONG_DESCRIPTION)
        page.wait_for_description(LIST_DESCRIPTION_PLACEHOLDER)
