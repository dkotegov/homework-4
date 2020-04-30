from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages


AUTH_MODAL = 'a[href="/login"]'
LOGIN_LOGIN = '#js-email-login'
LOGIN_PASSWODR = '#js-password-login'


REGISTER_NAME_INPUT = '#js-nickname-register'
REGISTER_NAME_ERROR = '#error-js-nickname-register'
REGISTER_LOGIN_INPUT = '#js-email-register'
REGISTER_LOGIN_ERROR = '#error-js-email-register'
REGISTER_PASSWORD_INPUT ='#js-password-register' 
REGISTER_PASSWORD_ERROR ='#error-js-password-register' 
REGISTER_PASSWORD_CHECK_INPUT = '#js-password-register-clone'
REGISTER_PASSWORD_CHECK_ERROR = '#error-js-password-register-clone'

REGISTER_BUTTON ='#js-register'
REGISTER_ERROR = '#error-js-register' 

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

    @staticmethod
    def set_register_name(name): 
        a.wait_for_load(css_locator=REGISTER_NAME_INPUT)
        element = a.find_element_by_css_selector(REGISTER_NAME_INPUT)
        element.click()
        element.send_keys(name)

    @staticmethod
    def set_register_email(email): 
        a.wait_for_load(css_locator=REGISTER_LOGIN_INPUT)
        element = a.find_element_by_css_selector(REGISTER_LOGIN_INPUT)
        element.click()
        element.send_keys(email)

    @staticmethod
    def set_register_password(password): 
        a.wait_for_load(css_locator=REGISTER_PASSWORD_INPUT)
        element = a.find_element_by_css_selector(REGISTER_PASSWORD_INPUT)
        element.click()
        element.send_keys(password)

    @staticmethod
    def set_register_password_clone(password):
        a.wait_for_load(css_locator=REGISTER_PASSWORD_CHECK_INPUT)
        element = a.find_element_by_css_selector(REGISTER_PASSWORD_CHECK_INPUT)
        element.click()
        element.send_keys(password)

    @staticmethod
    def click_reqister_button():
        a.wait_for_load(css_locator=REGISTER_BUTTON)
        element = a.find_element_by_css_selector(REGISTER_BUTTON)
        element.click()

    @staticmethod
    def find_register_name_error(): 
        a.wait_for_load(css_locator=REGISTER_NAME_ERROR)

    @staticmethod
    def find_register_email_error(): 
        a.wait_for_load(css_locator=REGISTER_LOGIN_ERROR)

    @staticmethod
    def find_register_password_error(): 
        a.wait_for_load(css_locator=REGISTER_PASSWORD_ERROR)

    @staticmethod
    def find_register_password_clone_error(): 
        a.wait_for_load(css_locator=REGISTER_PASSWORD_CHECK_ERROR)

    @staticmethod
    def find_register_error(): 
        a.wait_for_load(css_locator=REGISTER_ERROR)
