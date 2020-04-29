from tests.steps.search.steps import Steps


class TestSearch:
    VALID_GENRE = 'комедия'
    INVALID_GENRE = 'ааааа'
    VALID_RATING_FROM = '1'
    INVALID_RATING_FROM = '1000'
    VALID_COUNTRY = 'Россия'
    INVALID_COUNTRY = 'ааааа'
    VALID_YEAR_FROM = '2000'
    VALID_YEAR_TO = '2009'
    INVALID_YEAR_FROM = '10000'
    INVALID_YEAR_TO = '20000'

    def test_search_valid_genre(self):
        Steps.open_advanced_search_page()
        Steps.enter_genre(self.VALID_GENRE)
        Steps.click_advance_search()
        Steps.check_all_search_result_genre(self.VALID_GENRE)

    def test_search_invalid_genre(self):
        Steps.open_advanced_search_page()
        Steps.enter_genre(self.INVALID_GENRE)
        Steps.click_advance_search()
        Steps.check_search_result_not_found()

    def test_search_valid_rating(self):
        Steps.open_advanced_search_page()
        Steps.enter_rating(self.VALID_RATING_FROM)
        Steps.click_advance_search()
        Steps.check_first_film_rating(self.VALID_RATING_FROM)

    def test_search_invalid_rating(self):
        Steps.open_advanced_search_page()
        Steps.enter_rating(self.INVALID_RATING_FROM)
        Steps.click_advance_search()
        Steps.check_search_result_not_found()

    def test_search_valid_country(self):
        Steps.open_advanced_search_page()
        Steps.enter_country(self.VALID_COUNTRY)
        Steps.click_advance_search()
        Steps.check_first_film_country(self.VALID_COUNTRY)

    def test_search_invalid_country(self):
        Steps.open_advanced_search_page()
        Steps.enter_country(self.INVALID_COUNTRY)
        Steps.click_advance_search()
        Steps.check_search_result_not_found()

    def test_search_valid_years(self):
        Steps.open_advanced_search_page()
        Steps.enter_years(self.VALID_YEAR_FROM, self.VALID_YEAR_TO)
        Steps.click_advance_search()
        Steps.check_all_search_result_year(self.VALID_YEAR_FROM, self.VALID_YEAR_TO)

    def test_search_invalid_years(self):
        Steps.open_advanced_search_page()
        Steps.enter_years(self.INVALID_YEAR_FROM, self.INVALID_YEAR_TO)
        Steps.click_advance_search()
        Steps.check_search_result_not_found()
