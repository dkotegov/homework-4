from tests.conftest import accessor as a
from tests.pages.film.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def wait_for_container():
        Pages.check_film_content()

    @staticmethod
    def create_review(title, body):
        Pages.set_review_title(title)
        Pages.set_review_body(body)
        Pages.submit_review()

    def check_review(title, body):
        a.driver.refresh()
        t = Pages.get_first_review_title()
        print(t)

        assert title.lower() == t.lower()
        assert body == Pages.get_first_review_body()

    def create_list(name):
        Pages.click_select()
        Pages.choose_new_list_option()
        Pages.set_list_name(name)
        Pages.submit_list_create()

    def check_list_name(name):
        print(Pages.get_current_list())
        assert name.lower() == Pages.get_current_list().lower()

    def cancel_create_window(self):
        Pages.click_select()
        current = Pages.get_current_list()
        Pages.choose_new_list_option()
        Pages.cancel_list_create()
        assert current == Pages.get_current_list().lower()

    def go_to_same_film():
        Pages.click_same_film()
        
    def check_actor():
        first = Pages.get_film_actor()
        print(first)
        Pages.click_actor()
        Pages.wait_for_actor()
        second = Pages.get_actor_name()
        print(second)
        assert first.lower() == second.lower()
        
    def click_year(): 
        year = Pages.click_year()
        return year

    def click_genre():
        genre = Pages.click_genre()
        return genre

    def check_genre(genre):
        assert genre == Pages.click_genre()

    def click_country(): 
        country = Pages.click_country()
        return country

    def get_genres(): 
        return Pages.get_film_genres()
    
    def check_genres(genres):
        new = Pages.get_film_genres()
        for g in genres:
            assert g in new
    
    def click_star(number):
        Pages.click_star(number)

    def check_stars(number):
        now = Pages.check_stars()
        print(now)
        assert str(number) == str(now)

    def get_rating():
        rating = Pages.get_film_rating()
        print(rating)
        return rating

    def check_rating(rating):
        a.driver.refresh()
        new = Pages.get_film_rating()
        print(new) 
        assert new != rating
