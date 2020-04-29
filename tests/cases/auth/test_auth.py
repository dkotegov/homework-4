from time import sleep

from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.steps.auth.steps import Steps


class TestLogin:
    def test_success_login(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_credentials()
        Steps.login()