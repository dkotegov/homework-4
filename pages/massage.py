
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.default_page import DefaultPage


class MassagePage(DefaultPage):
    PATH = ""
    TITLE = ".chat-message-head-info-user__name"

    def get_title(self):
        self.wait(until=EC.presence_of_element_located((By.CSS_SELECTOR, self.TITLE)))
        return self.driver.find_element(By.CSS_SELECTOR, self.TITLE).text
