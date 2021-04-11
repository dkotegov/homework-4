from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResumePopupLocators:
    def __init__(self):
        self.root = '//div[@class="popUp-main"]'
        self.vacancies = '//div[@class="list-row"]'


class ResumePopup(BaseComponent):
    def __init__(self, driver):
        super(ResumePopup, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = ResumePopupLocators()

    def click_on_resume(self) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.vacancies))
        )
        element.click()
