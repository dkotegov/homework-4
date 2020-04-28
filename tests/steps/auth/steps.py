from tests.pages.auth.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def open_auth_page():
        Pages.click_auth_modal()
