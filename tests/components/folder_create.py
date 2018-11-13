from component import Component
from selenium.webdriver.support.ui import WebDriverWait

class FolderCreate(Component):
    BASE = '//div[@data-qa-id="layer-window-block"] '

    INPUT_FOLDER_NAME = BASE + '//input[@data-test-id="name"]'
    SUBMIT = BASE + '//button[@data-test-id="submit"]'

    def set_name(self, name):
        name_input = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_FOLDER_NAME)
        )
        name_input.send_keys(name)
    
    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()