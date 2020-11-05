import os

from egogoger.todo_mail.pages.main_page import MainPage
from egogoger.todo_mail.pages.auth_page import AuthPage
from egogoger.base_test import Test
from egogoger.utils import set_input


def auth_test(test):
    main_page = MainPage(test.driver)
    main_page.open()

    auth_page = AuthPage(test.driver)
    auth_page.check_for_self(test)

    set_input(test.driver, auth_page.EMAIL_INPUT, os.environ.get('LOGIN'))
    auth_page.next()
    set_input(test.driver, auth_page.PASSWORD_INPUT,os.environ.get('PASSWORD'))
    auth_page.submit()

    main_page.check_for_self(test)


class AuthTest(Test):
    def test(self):
        auth_test(self)
