from Pages.auth_page import AuthPage
from check_profile_login import check_profile_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def setup_auth(t):
    auth_page = AuthPage(t.driver)
    auth_page.open()
    auth_page.set_login(t.LOGIN)
    auth_page.set_password(t.PASSWORD)
    auth_page.submit()
    WebDriverWait(auth_page.driver, 5).until(EC.presence_of_element_located((By.XPATH, auth_page.ICON)))
    return check_profile_login(t)
