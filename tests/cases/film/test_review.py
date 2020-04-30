
from tests.steps.auth.steps import Steps as Auth
from tests.steps.genreFilm.steps import Steps as Genre
from tests.steps.film.steps import Steps as Film


class TestReview:
    def test_eng(self):
        title = "testreview1review"
        body = "testtestetstesttestest"

        Auth.auth()
        Genre.open_genre_page()
        Genre.click_film()

        Film.wait_for_container()
        Film.create_review(title, body)
        Film.check_review(title, body)

    def test_ru(self):
        title = "Тестовое название"
        body = "текстекстекстектст текст текст текст"

        Auth.auth()

        Genre.open_genre_page()
        Genre.click_film()

        Film.wait_for_container()
        Film.create_review(title, body)
        Film.check_review(title, body)




        