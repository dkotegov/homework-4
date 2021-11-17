from tests.pages.auth_customer import CustomerAuthPage


def auth_setup(t):
    auth_page = CustomerAuthPage(t.driver)
    auth_page.open()
    auth_page.set_login(t.USER_LOGIN)
    auth_page.set_password(t.USER_PASSWORD)
    auth_page.submit()
    auth_page.wait_until_login()
    auth_page.set_address("Москва")
    auth_page.submit_address()
