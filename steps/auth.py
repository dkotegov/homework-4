from Pages.auth_page import AuthPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def setup_auth(t):
    auth_page = AuthPage(t.driver)
    auth_page.open()
    auth_page.set_login(t.LOGIN)
    auth_page.set_password(t.PASSWORD)
    auth_page.submit()
    auth_page.wait_auth()
