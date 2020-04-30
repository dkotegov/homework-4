from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film


class TestFilmGenre:
    def test(self):

        Genre.open_genre_page()
        genre = Genre.click_genre()
        Genre.click_film()
        Film.wait_for_container()
        Film.check_genre(genre)
