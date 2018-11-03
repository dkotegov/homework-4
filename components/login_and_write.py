from pages.auth_page import AuthPage


def login_and_write(driver, login, password):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_form = auth_page.form
    auth_form.set_login(login)
    auth_form.set_password(password)
    auth_form.submit()