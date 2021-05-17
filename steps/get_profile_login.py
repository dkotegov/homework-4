from Pages.profile_page import ProfilePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_profile_login(t):
    profile_page = ProfilePage(t.driver)
    profile_page.open()
    return profile_page.get_username()
