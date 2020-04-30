from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film
from tests.steps.search.steps import Steps as Search


class TestLinks:
    def test_same_film(self):

        Genre.open_genre_page()
        Genre.click_film()

        Film.wait_for_container()
        genres = Film.get_genres()
        Film.go_to_same_film()
        Film.wait_for_container()
        Film.check_genres(genres)

    def test_year(self):

        Genre.open_genre_page()
        Genre.click_film()

        Film.wait_for_container()
        year = Film.click_year()

        Search.check_all_search_result_year(year, year)


    def test_actor(self):
        Genre.open_genre_page()
        Genre.click_film()

        Film.wait_for_container()
        Film.check_actor()

    def test_country(self):
        Genre.open_genre_page()
        Genre.click_film()

        Film.wait_for_container()
        country = Film.click_country()
        Search.check_first_film_country(country)


    def test_genre(self):
        Genre.open_genre_page()
        Genre.click_film()
        Film.wait_for_container()
        genre = Film.click_genre()
        Search.check_all_search_result_genre(genre)

