# coding=utf-8
import time

from tests.elements.main import UserDropdown


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)
        self.wait()
        UserDropdown(self.driver).wait_for_presence()

    def wait(self):
        def page_has_loaded():
            page_state = self.driver.execute_script(
                'return document.readyState;'
            )
            return page_state == 'complete'

        start_time = time.time()
        while time.time() < start_time + 10:
            if page_has_loaded():
                return True
            else:
                time.sleep(0.1)
        raise Exception('Timeout waiting for page loaded')
