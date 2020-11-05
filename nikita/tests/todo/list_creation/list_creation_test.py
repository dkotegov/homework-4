from nikita.tests.todo.default import Test
from nikita.pages.todo.main import MainPage

class ListCreationTest(Test):
    LIST_NAME = 'lol'

    def test(self):
        page = MainPage(self.driver)
        lists = page.count_lists()
        page.create_list(self.LIST_NAME)
        page.wait_for_list(self.LIST_NAME)
        self.assertEqual(
            lists + 1,
            page.count_lists()
        )

    def tearDown(self):
        page = MainPage(self.driver)
        lists = page.count_lists_by_name(self.LIST_NAME)
        page.delete_list(self.LIST_NAME)
        page.refresh()
        page.wait_for_list_not_to_appear(self.LIST_NAME, lists)
        super().tearDown()
