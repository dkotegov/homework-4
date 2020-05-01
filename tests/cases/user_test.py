from tests.cases.base import TestAuthorized
from tests.pages.pin import PinDetailsPage
from tests.pages.user_details import UserDetailsPage


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = UserDetailsPage(self.driver,  'testTest')

    def test_subscribe(self):
        self.page.form.subscribe()

    def test_unsubscribe(self):
        self.page.form.unsubscribe()

    def test_open_pin(self):
        name, link = self.page.form.open_pin(0)
        page = PinDetailsPage(self.driver, False)
        real_name = page.form.get_title()
        self.assertEqual(real_name, name, "Names are different")
        self.assertEqual(self.driver.current_url, link, 'Wrong page opened')

