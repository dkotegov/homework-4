from cases.base_case import BaseTest


class AuthTest(BaseTest):
    def test_auth(self):
        print('Auth test')
        # TODO: add validation
        self.auth()
