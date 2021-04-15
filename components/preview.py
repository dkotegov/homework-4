from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent
from selenium.common.exceptions import StaleElementReferenceException


class PreviewLocators:
    def __init__(self):
        self.info_btn = '//a[@class="preview__btn info-btn"]'
        self.play_btn = '//button[@class="preview__btn play-btn"]'


class Preview(BaseComponent):
    def __init__(self, driver):
        super(Preview, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = PreviewLocators()
    
    def click_info_button(self):
        """
        Кликает на кнопку "Подробнее"
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.info_btn))
        )
        submit.click()
    
    def click_play_button(self):
        """
        Кликает на кнопку "Воспроизвести"
        """
        for i in range(4):
            try:
                submit = WebDriverWait(self.driver, 30, 0.1).until(
                    EC.visibility_of_element_located((By.XPATH, self.locators.play_btn))
                )
                submit.click()
                return True
            except StaleElementReferenceException as e:
                pass
        return False
