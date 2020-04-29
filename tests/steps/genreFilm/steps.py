from tests.conftest import accessor as a
from tests.pages.genreFilms.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def open_genre_page():
        a.driver.get('https://cinsear.ru/search?films')

    @staticmethod
    def click_film():
        Pages.wait_for_container()
        Pages.click_film()

    def click_more_button():
        before = Pages.count_films()
        Pages.click_more()
        now = Pages.count_films()
        print(before)
        print(now)
        assert before < now

    def click_genre():
        Pages.wait_for_container()
        return Pages.click_genre()


    