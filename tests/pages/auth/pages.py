from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages


class Pages(BasePages):
    @staticmethod
    def click_auth_modal():
        a.wait_for_load(css_locator='a[href="/login"]')
        btn = a.find_element_by_css_selector('a[href="/login"]')
        btn.wait_and_click()

    @staticmethod
    def enter_username():
        element = a.find_element_by_id('js-email-login')
        element.wait_and_click()
        element.send_keys(a.username)

    @staticmethod
    def enter_password():
        element = a.find_element_by_id('js-password-login')
        element.wait_and_click()
        element.send_keys(a.password)

    @staticmethod
    def click_login_button():
        element = a.find_element_by_id('js-login')
        element.click()

    @staticmethod
    def wait_until_page_load():
        a.wait_for_load(css_locator='div.trailers-bar')
        assert a.current_url == PROJECT_URL
