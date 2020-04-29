from tests.steps.search.steps import Steps


class TestSearch:
    FULL_TITLE_CORRECT_CASE = 'Матрица'
    FULL_TITLE_CUSTOM_CASE = 'МатРиЦА'
    TRUNCATED_TITLE_CORRECT_CASE = 'Матр'
    TRUNCATED_TITLE_CUSTOM_CASE = 'МАтрИ'
    NONEXISTENT_TITLE = 'ааааааа'

    def test_search_full_title_correct_case(self):
        Steps.open_site()
        Steps.enter_search_query(self.FULL_TITLE_CORRECT_CASE)
        Steps.check_search_result_title(self.FULL_TITLE_CORRECT_CASE)

    def test_search_full_title_custom_case(self):
        Steps.open_site()
        Steps.enter_search_query(self.FULL_TITLE_CUSTOM_CASE)
        Steps.check_search_result_title(self.FULL_TITLE_CUSTOM_CASE)

    def test_search_truncated_title_correct_case(self):
        Steps.open_site()
        Steps.enter_search_query(self.TRUNCATED_TITLE_CORRECT_CASE)
        Steps.check_search_result_title(self.TRUNCATED_TITLE_CORRECT_CASE)

    def test_search_truncated_title_custom_case(self):
        Steps.open_site()
        Steps.enter_search_query(self.TRUNCATED_TITLE_CUSTOM_CASE)
        Steps.check_search_result_title(self.TRUNCATED_TITLE_CUSTOM_CASE)

    def test_search_empty_title(self):
        Steps.open_site()
        Steps.enter_search_query('')
        Steps.check_search_result_not_found()

    def test_search_nonexistent_title(self):
        Steps.open_site()
        Steps.enter_search_query(self.NONEXISTENT_TITLE)
        Steps.check_search_result_not_found()
