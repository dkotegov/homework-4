from tests.pages.auth_customer import CustomerAuthPage


def auth_setup(t):
    t.auth_page = CustomerAuthPage(t.driver)
    t.auth_page.open()
    t.auth_page.set_login(t.USER_LOGIN)
    t.auth_page.set_password(t.USER_PASSWORD)
    t.auth_page.submit()
    t.auth_page.wait_until_login()
