from tests.conftest import accessor as a
from tests.pages.film.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):

    @staticmethod
    def wait_for_container():
        Pages.check_film_content()

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
        


