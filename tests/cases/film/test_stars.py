
from tests.steps.auth.steps import Steps as Auth
from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film


class TestReview:
    def test_click_stars(self):
        number = 3

        Auth.auth()
        Genre.open_genre_page()
        Genre.click_film()

        Film.wait_for_container()
        Film.click_star(number)
        Film.check_stars(number)
    
    def test_change_rating(self):
        number = 5

        Auth.auth()
        Genre.open_genre_page()
        Genre.click_film()

        Film.wait_for_container()
        rating  = Film.get_rating()
        Film.click_star(number)
        Film.check_rating(rating)
    