from cases.base_case import BaseTest

from steps.people_steps import PeopleSteps

from pages.login_form import LoginForm


class PeopleTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.people_steps = PeopleSteps(self.driver)
        self.people_steps.open_page()
        self.login_form = LoginForm(self.driver)

    def test_click_disguisht(self):
        self.people_steps.click_disguisht()
        self.login_form.wait_until_visible()
        self.assert_(self.login_form.is_visible())

    def test_click_like_icon(self):
        self.people_steps.click_like_icon()
        self.login_form.wait_until_visible()
        self.assert_(self.login_form.is_visible())

    def test_click_download_more(self):
        self.people_steps.click_download_more()
