from nikita.tests.virusmusic.default import Test
from nikita.pages.virusmusic.profile.settings import SettingsPage
from selenium.webdriver.support.wait import WebDriverWait

class LanguageChangeTest(Test):
    LANGUAGE = 'rus'

    def test(self):
        page = SettingsPage(self.driver)
        page.open_containers()
        self.language = page.get_language()
        page.change_language(self.LANGUAGE)
        page.open_containers()
        WebDriverWait(self.driver, 10, 0.1).until(lambda driver:
            page.get_language() == self.LANGUAGE
        )
        pass

    def tearDown(self):
        page = SettingsPage(self.driver)
        page.change_language(self.language)
        page.open_containers()
        WebDriverWait(self.driver, 10, 0.1).until(lambda driver:
            page.get_language() == self.language
        )
        super().tearDown()
