from cases.base_case import BaseTest

from steps.meeting_steps import MeetingSteps

from pages.login_form import LoginForm

class MeetingTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.meeting_steps = MeetingSteps(self.driver)
        self.meeting_steps.open_page()
        self.login_form = LoginForm(self.driver)

    def test_click_like_without_auth(self):
        self.meeting_steps.click_like()
        self.login_form.wait_until_visible()
        self.assert_(self.login_form.is_visible())

    def test_click_go_button_without_auth(self):
        self.meeting_steps.click_go_button()
        self.login_form.wait_until_visible()
        self.assert_(self.login_form.is_visible())

    def test_click_meet_member(self):
        self.meeting_steps.click_meet_member()

    def test_click_go_button_with_auth(self):
        self.auth()
        self.meeting_steps.open_page()
        self.meeting_steps.click_go_button()
        self.meeting_steps.handle_go_button()

    def test_click_like_with_auth(self):
        self.auth()
        self.meeting_steps.open_page()
        self.meeting_steps.click_like()
        self.meeting_steps.handle_like()