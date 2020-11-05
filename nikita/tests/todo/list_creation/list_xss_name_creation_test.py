from nikita.tests.todo.default import Test
from nikita.pages.todo.main import MainPage
from nikita.constants import LIST_XSS_NAME
from nikita.utils import wait_for_no_alert

class ListXssNameCreationTest(Test):
    def test(self):
        page = MainPage(self.driver)
        lists = page.count_lists()
        page.create_list(LIST_XSS_NAME)
        page.wait_for_list(LIST_XSS_NAME)
        self.assertEqual(
            lists + 1,
            page.count_lists()
        )
        page.refresh()
        wait_for_no_alert(self.driver)
        pass

    def tearDown(self):
        page = MainPage(self.driver)
        lists = page.count_lists_by_name(LIST_XSS_NAME)
        page.delete_list(LIST_XSS_NAME)
        page.refresh()
        page.wait_for_list_not_to_appear(LIST_XSS_NAME, lists)
        super().tearDown()
