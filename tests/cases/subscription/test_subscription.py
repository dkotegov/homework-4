from time import sleep

from tests.conftest import open_user_profile, unsubscribe
from tests.steps.subscription.steps import Steps
from tests.steps.profile.steps import Steps as ProfileSteps


class TestSubscription:
    def test_subscribe(self, user):
        actor_id = 1
        Steps.subscribe(actor_id)
        open_user_profile()
        ProfileSteps.open_subscription_tab()
        Steps.check_subscription_existence(actor_id)
        unsubscribe(actor_id)
        open_user_profile()
        ProfileSteps.open_subscription_tab()
        Steps.check_subscription_nonexistence(actor_id)
