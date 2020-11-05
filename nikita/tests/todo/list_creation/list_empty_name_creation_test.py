from nikita.tests.todo.default import Test
from nikita.pages.todo.main import MainPage

class ListEmptyNameCreationTest(Test):
    def test(self):
        page = MainPage(self.driver)
        lists = page.count_lists()
        page.create_list('')
        self.assertEqual(
            lists,
            page.count_lists()
        )
