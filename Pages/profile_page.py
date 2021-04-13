from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class ProfilePage(Page):
    USERNAME = '//span[@class="name__profile__default_margin--_Vkp5 name__profile_login--2W71f"]'

    def check_username(self, username):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.USERNAME)))
        username_in_profile = self.driver.find_element_by_xpath(self.USERNAME).text
        if username_in_profile == username:
            return True
        else:
            return False
