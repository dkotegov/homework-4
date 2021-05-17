from Pages.auth_page import AuthPage

def logout(t):
    auth_page = AuthPage(t.driver)
    auth_page.logout()

