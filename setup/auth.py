from pages.auth_page import AuthPage


def setup_auth(test) -> None:
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(test.EMAIL)
    auth_form.set_password(test.PASSWORD)
    auth_form.submit()
    auth_form.wait_for_mainpage()
