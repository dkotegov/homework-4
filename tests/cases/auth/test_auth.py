from tests.steps.auth.steps import Steps


class TestLogin:
    def test_success_login(self):
        Steps.open_site()
        Steps.open_auth_page()
