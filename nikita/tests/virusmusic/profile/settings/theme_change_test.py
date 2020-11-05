from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.settings import SettingsPage
from nikita.utils import wait_for_pop_up, wait_for_element_attribute_change

class ThemeChangeTest(Test):
    THEME = 'special lsd'

    def test(self):
        page = SettingsPage(self.driver)
        self.theme = page.get_theme()
        page.change_theme(self.THEME)
        wait_for_pop_up(self.driver)
        wait_for_element_attribute_change(
            self.driver,
            'html',
            'theme',
            self.THEME.split()[0]
        )

    def tearDown(self):
        page = SettingsPage(self.driver)
        page.change_theme(self.theme)
        wait_for_pop_up(self.driver)
        wait_for_element_attribute_change(
            self.driver,
            'html',
            'theme',
            self.theme.split()[0]
        )
        super().tearDown()
