from library.ok import LoggedInTestCase
from library.ok.pages import MainPage


class TestLibraryTestCase(LoggedInTestCase):
    def test_simple(self):
        self.assertEqual(self.driver.current_url, MainPage.get_url(), 'Opened base url')
        self.assertGreater(len(self.driver.find_elements_by_xpath(MainPage.AVATAR_ICON)), 0)
