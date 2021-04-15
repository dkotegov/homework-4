from cases.base_case import BaseTest
from steps.search_steps import SearchSteps


class SearchTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.search_steps = SearchSteps(self.driver)
        self.search_steps.open_page()

    def test_search_meetings(self):
        search_query = "meeting"
        expected = True

        self.search_steps.open_search_block()
        self.search_steps.enter_search_query(search_query)
        offers = self.search_steps.get_search_offers()
        actual = len(offers) > 0

        self.assertEqual(expected, actual, f'Value {actual} doesn\'t match {expected}')