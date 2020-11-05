from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.settings import SettingsPage
from nikita.utils import wait_for_element_value, wait_for_pop_up

class ValidNameChangeTest(Test):
    VALID_NAME = 'Лол'

    def test(self):
        page = SettingsPage(self.driver)
        self.name = page.get_name()
        page.change_name(self.VALID_NAME)
        wait_for_pop_up(self.driver)
        page.refresh()
        self.assertEqual(
            page.get_name(),
            self.VALID_NAME
        )

    def tearDown(self):
        page = SettingsPage(self.driver)
        page.change_name(self.name)
        wait_for_pop_up(self.driver)
        super().tearDown()
