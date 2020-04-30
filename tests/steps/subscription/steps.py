from selenium.common.exceptions import NoSuchElementException

from tests.pages.subscription.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def subscribe(actor_id):
        Pages.open_actor_page(actor_id)
        try:
            Pages.subscribe()
        except:
            Pages.subscribe()
        

    @staticmethod
    def check_subscription_existence(actor_id):
        Pages.find_actor_subscription(actor_id)

    @staticmethod
    def check_subscription_nonexistence(actor_id):
        try:
            Pages.find_actor_subscription_nowait(actor_id)
            raise AssertionError
        except NoSuchElementException:
            pass
        except:
            raise AssertionError

    @staticmethod
    def unsubscribe(actor_id):
        Pages.open_actor_page(actor_id)
        Pages.unsubscribe()
