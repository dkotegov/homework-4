from cases.base_case import BaseTest

from steps.meetings_steps import MeetingsSteps

from pages.login_form import LoginForm

class MeetingsTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.meetings_steps = MeetingsSteps(self.driver)
        self.meetings_steps.open_page()
        self.login_form = LoginForm(self.driver)

    def test_card_like_auth(self):
        self.auth()
        self.meetings_steps.like_card()
        self.meetings_steps.handle_like()

    def test_card_like_without_auth(self):
        self.meetings_steps.like_card()
        self.login_form.wait_until_visible()
        self.assert_(self.login_form.is_visible())
    
    def test_slide_like_without_auth(self):
        self.meetings_steps.like_slide()
        self.login_form.wait_until_visible()
        self.assert_(self.login_form.is_visible())

    def test_slide_go_button_without_auth(self):
        self.meetings_steps.go_button()
        self.login_form.wait_until_visible()
        self.assert_(self.login_form.is_visible())

    def test_slide_go_button_auth(self):
        self.auth()
        self.meetings_steps.go_button()
        self.meetings_steps.handle_go_button()

    def test_slide_like_auth(self):
        self.auth()
        self.meetings_steps.like_slide()
        self.meetings_steps.handle_like()

    def test_click_slide(self):
        self.meetings_steps.click_slide()
        self.meetings_steps.wait_page_load('https://onmeet.ru/meeting?meetId=29')
        self.assert_('https://onmeet.ru/meeting' in self.driver.current_url)

    def test_click_card(self):
        self.meetings_steps.click_card()
        self.meetings_steps.wait_page_load('https://onmeet.ru/meeting?meetId=29')
        self.assert_('https://onmeet.ru/meeting' in self.driver.current_url)

    def test_click_remove_filters(self):
        self.meetings_steps.click_remove_filters()
        self.meetings_steps.wait_page_load('https://onmeet.ru/meetings')
        self.assertEqual('https://onmeet.ru/meetings', self.driver.current_url)

    def test_click_my_meetings(self):
        self.meetings_steps.click_my_meetings()
        self.login_form.wait_until_visible()
        self.assert_(self.login_form.is_visible())

    def test_click_disguisht(self):
        self.meetings_steps.click_disguisht()
        self.login_form.wait_until_visible()
        self.assert_(self.login_form.is_visible())
        