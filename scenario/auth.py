from pages.auth_page import AuthPage


def setup_auth(test, email=None, pswd=None) -> None:
    if email is None and pswd is None:
        email = test.EMAIL
        pswd = test.PASSWORD
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(email)
    auth_form.set_password(pswd)
    auth_form.submit()
    auth_form.wait_for_mainpage()


def auth_as_employer_has_comp(test):
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(test.EMAIL1)
    auth_form.set_password(test.PASSWORD1)
    auth_form.submit()
    auth_form.wait_for_mainpage()
