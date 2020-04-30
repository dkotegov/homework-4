import uuid

from tests.conftest import open_user_profile
from tests.steps.lists.steps import Steps

from tests.steps.review.steps import Steps as ReviewSteps

from tests.steps.profile.steps import Steps as ProfileSteps


class TestLists:
    def test_add_film_to_new_list(self, user):
        list_name = str(uuid.uuid4())
        film_id = 2
        ReviewSteps.get_film(film_id)
        Steps.create_list(list_name)
        open_user_profile()
        ProfileSteps.open_lists_tab()
        ProfileSteps.check_film_in_list(list_name, film_id)

    def test_add_film_to_existing_list(self, user):
        list_name = 'testlist'
        film_id = 12
        ReviewSteps.get_film(film_id)
        Steps.select_list(list_name)
        open_user_profile()
        ProfileSteps.open_lists_tab()
        ProfileSteps.check_film_in_list(list_name, film_id)
