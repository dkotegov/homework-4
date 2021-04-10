from components.base_component import BaseComponent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegistrationFormLocators:
    def __init__(self):
        self.root = '//div[@class="main-page"]'
        self.page_title = '//div[@class="page-name page-name_small page-name_reg"]'


class RegistrationForm(BaseComponent):
    def __init__(self, driver):
        super(RegistrationForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)

        self.locators = RegistrationFormLocators()

    def is_open(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.page_title)))
            return True
        except:
            return False

