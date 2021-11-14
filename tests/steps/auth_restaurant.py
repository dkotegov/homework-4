from tests.pages.auth_customer import CustomerAuthPage


def auth_setup(t):
    auth_page = CustomerAuthPage(t.driver)
    auth_page.open()
    auth_page.go_to_restaurant_auth()
    auth_page.set_login(t.RESTAURANT_LOGIN)
    auth_page.set_password(t.RESTAURANT_PASSWORD)
    auth_page.submit()
    auth_page.wait_until_login()
