from pages.auth_page import AuthPage


def setup_auth(t):
    auth_page = AuthPage(t.driver)
    auth_page.open()
    if auth_page.ads_page():
        auth_page.set_login(t.LOGIN)
        auth_page.open_window_sign_in()
        auth_page.set_password(t.PASSWORD)
        auth_page.submit()
    else:
        auth_page.set_login(t.LOGIN)
        auth_page.open_window_sign_in()
        auth_page.set_password(t.PASSWORD)
        auth_page.submit()
        auth_page.open_cloud()
