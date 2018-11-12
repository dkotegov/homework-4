from Component import Component
from selenium.webdriver.support.ui import WebDriverWait

class Sidebar(Component):
    NEW_DIR = '//div[@class="new-folder-btn__button-wrapper"]'
    DIR_NAME = '//input[@class="c2146 c2148"]'
    ADD_DIR_BUTTON = '//button[@class="c2181 c2164 c2186 c2169 c2192 c2176"]'

    def create_new_dir(self):
        create_dir_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NEW_DIR)
        )
        create_dir_button.click()

    def set_dir_name(self, name):
        input_name = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DIR_NAME)
        )
        input_name.send_keys(name)

    def submit_new_dir(self):
        self.driver.find_element_by_xpath(self.ADD_DIR_BUTTON).click()
