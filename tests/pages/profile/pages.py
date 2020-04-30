from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages


class Pages(BasePages):
    @staticmethod
    def click_open_editing_page_button():
        a.wait_for_load(css_locator='a.button')
        button = a.find_element_by_css_selector('a.button')
        button.click()
        a.wait_for_load(css_locator='.js-profile-wall')
        a.sleep(1)

    @staticmethod
    def click_open_editing_modal_button():
        button = a.find_element_by_css_selector('.js-edit-button')
        button.wait_and_click()
        a.wait_for_load(css_locator='.js-edit-button')

    @staticmethod
    def upload_avatar(file: str):
        button = a.find_element_by_css_selector('.js-avatar-input')
        button.send_keys(file)

    @staticmethod
    def enter_name(name):
        form = a.find_element_by_id('js-username-input')
        form.wait_and_click()
        form.send_keys(name)

    @staticmethod
    def enter_description(description):
        form = a.find_element_by_id('js-description-textarea')
        form.wait_and_click()
        form.send_keys(description)

    @staticmethod
    def save_profile():
        button = a.find_element_by_id('js-save-button')
        button.click()
        a.wait_for_load(css_locator='.button_active')

    @staticmethod
    def open_subscription_tab():
        selector = '.js-events-button'
        a.wait_for_load(css_locator=selector)
        tab = a.find_element_by_css_selector(selector)
        tab.click()

    @staticmethod
    def save_profile_no_wait():
        button = a.find_element_by_id('js-save-button')
        button.click()
        # wait
        a.sleep(1)
