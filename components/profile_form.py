from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_component import BaseComponent


class ProfileFormLocators:
    def __init__(self):
        self.root = '//div[@class="main-page"]'
        self.page_title = '//div[@class="profile-title"]'
        self.personal_info_btn = '//div[@class="btn-href"][0]'
        self.my_res_or_vac_btn = '//div[@class="btn-href"][1]'
        self.chosen_btn = '//div[@class="btn-href"][2]'
        self.responses_btn = '//div[@class="btn-href"][3]'

        self.personal_name = '//div[@id="name"]'
        self.personal_surname = '//div[@id="surname"]'
        self.personal_email = '//div[@id="email"]'


class ProfileForm(BaseComponent):
    def __init__(self, driver):
        super(ProfileForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)

        self.locators = ProfileFormLocators()

    def is_open(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.page_title)))
            return True
        except:
            return False


    def check_profile_email(self) -> bool:
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.personal_email)))
        return element.text


