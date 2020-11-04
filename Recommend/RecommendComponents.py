from time import sleep

from Base import Component
from collections import namedtuple

RecommendationLink = namedtuple('Recommendation', 'locator resultUrl')


class Recommendations(Component):
    def click_on_recommendation(self, recommendation: RecommendationLink):
        recommendation = self._wait_until_and_get_elem_by_xpath(recommendation.locator)
        recommendation.click()

    def select_other_tab(self, window_handle=None):
        if window_handle is not None:
            old = self.driver.current_window_handle
            self.driver.switch_to.window(window_handle)
            return old

        # nickeskov: wait other window/tab
        for _ in range(10):
            if len(self.driver.window_handles) < 2:
                # nickeskov: i know this is "bad" idea, but i have no ideas how to do this "right"
                sleep(0.1)
            else:
                break

        for handle in self.driver.window_handles:
            if handle != self.driver.current_window_handle:
                old = self.driver.current_window_handle
                self.driver.switch_to.window(handle)
                return old

    def wait_result_url(self, recommendation: RecommendationLink):
        self._wait_for_url(recommendation.resultUrl)

    def close_window_and_switch_to_other(self, window_handle):
        self.driver.close()
        self.driver.switch_to.window(window_handle)
