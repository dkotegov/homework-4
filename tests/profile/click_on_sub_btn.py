from pages.profile import ProfilePage
from tests.default_authorized import TestAuthorized


class ClickOnSubscriptionBtnTest(TestAuthorized):
    def test(self):
        profile_page = ProfilePage(self.driver)
        profile_page.open()

        profile_page.click_on_subscription_btn()

        self.assertTrue(profile_page.is_umoney_url())
