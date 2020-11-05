from nikita.tests.todo.default import Test
from nikita.pages.todo.main import MainPage
from nikita.pages.todo.list import ListPage

class ListChangeTest(Test):
    LIST_NAME = 'lol'

    def setUp(self):
        super().setUp()
        page = MainPage(self.driver)
        page.create_list(self.LIST_NAME)
        page.wait_for_list(self.LIST_NAME)
        self.listId = page.open_list(self.LIST_NAME)

    def tearDown(self):
        page = MainPage(self.driver)
        lists = page.count_lists_by_name(self.LIST_NAME)
        page.open_list_by_id(self.listId)
        ListPage(self.driver).delete()
        page.refresh()
        page.wait_for_list_not_to_appear(self.LIST_NAME, lists)
        super().tearDown()
