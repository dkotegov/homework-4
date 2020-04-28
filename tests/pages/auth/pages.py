from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages


class Pages(BasePages):
    @staticmethod
    def click_auth_modal():
        btn = a.find_element_by_css_selector('a[href="/login"]')
        btn.click()
