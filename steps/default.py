import os

from pages.default import Page


class DefaultSteps(object):
    def __init__(self, driver):
        self.driver = driver
        self.page = Page(driver)

    def authorize(self):
        self.page.open_authorize()
        self.page.set_login(os.environ.get('TEST_LOGIN'))
        self.page.continue_authorize()
        self.page.set_password(os.environ.get('TEST_PASSWORD'))
        self.page.submit()
        self.page.wait_for_authorize()

    def get_current_url(self):
        return self.driver.current_url

    def remove_all_files(self):
        self.page.open()
        self.page.close_bubble()
        self.page.select_all()
        if self.page.remove():
            self.page.remove_submit()

    def get_amount_of_files(self):
        self.page.open()
        self.page.close_bubble()
        self.page.select_all()
        res = self.page.get_amount_of_files()
        self.page.select_all()
        return res

    def switch_to_nth_tab(self, n):
        self.page.switch_to_nth_tab(n)

    def close_current_tab(self):
        self.page.close_current_tab()
