from nikita.tests.todo.default import Test
from nikita.pages.todo.main import MainPage

class ListDeletionLeftMenuTest(Test):
    LIST_NAME = 'lol'

    def setUp(self):
        super().setUp()
        page = MainPage(self.driver)
        page.create_list(self.LIST_NAME)
        page.wait_for_list(self.LIST_NAME)

    def test(self):
        page = MainPage(self.driver)
        lists = page.count_lists()
        page.delete_list(self.LIST_NAME)
        page.wait_for_list_to_disappear(self.LIST_NAME)
        self.assertEqual(
            lists - 1,
            page.count_lists()
        )
