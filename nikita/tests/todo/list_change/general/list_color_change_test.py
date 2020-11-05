from nikita.tests.todo.list_change.default import ListChangeTest
from nikita.pages.todo.list import ListPage

class ListColorChangeTest(ListChangeTest):
    def test(self):
        page = ListPage(self.driver)
        newColor = page.change_color()
        page.wait_for_color(newColor)
