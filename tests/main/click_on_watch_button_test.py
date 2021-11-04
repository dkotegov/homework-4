import utils
from pages.main import MainPage
from tests.default import Test

from constants import BASE_URL


class ClickOnWatchButtonTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        content_id, content_type = main_page.get_first_card_id_and_type()
        main_page.click_on_first_card_watch_button()
        needed_url = BASE_URL + content_type + '/' + str(content_id)
        utils.wait_for_url(self.driver, needed_url)
        self.assertEqual(self.driver.current_url, needed_url)
