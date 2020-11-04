import unittest
import utils

from Recommend import RecommendationLink, RecommendationsPage


class RecommendTests(unittest.TestCase):
    screenshoter = RecommendationLink(
        "//a[starts-with(@href, 'https://apps.apple.com/ru/app/screenshoter-mail-ru/')]",
        "https://apps.apple.com/ru/app/screenshoter-mail-ru/id1144027175?mt=12"
    )
    isq = RecommendationLink(
        "//a[@href='https://trk.mail.ru/c/lmg5u5']",
        "https://icq.com/"
    )
    diskO = RecommendationLink(
        "//a[starts-with(@href, 'https://trk.mail.ru/c/oea2r0')]",
        "https://apps.apple.com/ru/app/disk-o-all-clouds-one-place/id1322465647?l=ru&mt=12"
    )

    def _clickWaitCheck(self, recommendation: RecommendationLink):
        recommend_page = RecommendationsPage(self.driver)
        recommend_page.open()

        rec = recommend_page.recommendations

        rec.click_on_recommendation(recommendation)

        old_tab = rec.select_other_tab()

        rec.wait_result_url(recommendation)

        rec.close_window_and_switch_to_other(old_tab)

    def setUp(self) -> None:
        self.driver = utils.standard_set_up_auth()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_screenshoter_recommendation(self):
        self._clickWaitCheck(self.screenshoter)

    def test_isq_recommendation(self):
        self._clickWaitCheck(self.isq)

    def test_diskO_recommendation(self):
        self._clickWaitCheck(self.diskO)
