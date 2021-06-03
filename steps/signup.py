from Pages.signup_page import SignupPage

def signup(t, login, password, email):
    signup_page = SignupPage(t.driver)
    signup_page.open()
    signup_page.set_login(login)
    signup_page.set_password(password)
    signup_page.set_mail(email)
    signup_page.submit()
    signup_page.wait_for_account()
