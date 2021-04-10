from pages.auth_page import AuthPage


def setup_auth(test, data=None) -> bool:
    if data is None:
        data = {
            'EMAIL': test.EMAIL,
            'PASSWORD': test.PASSWORD
        }
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(data['EMAIL'])
    auth_form.set_password(data['PASSWORD'])
    auth_form.submit()
    if data['EMAIL'] == test.EMAIL and data['PASSWORD'] == test.PASSWORD:
        auth_form.wait_for_mainpage()

