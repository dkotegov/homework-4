from component import Component
from selenium.webdriver.support.ui import WebDriverWait

class Sidebar(Component):
    BASE = '//div[@data-qa-id="full"] '
    BASE_WITHOUT_QA_ID = '//div[contains(@class,"sidebar__full")]'

    INBOX_BUTTON = BASE + '//a[@data-qa-id="0"]'
    NEW_DIR =  BASE + '//div[@class="new-folder-btn__button-wrapper"]'

    def create_new_dir(self):
        create_dir_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NEW_DIR)
        )
        create_dir_button.click()
    
    def click_to_inbox(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INBOX_BUTTON)
        ).click()

    def waitForVisible(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE_WITHOUT_QA_ID))
