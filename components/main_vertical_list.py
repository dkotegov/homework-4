
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent


class MainVerticalList(BaseComponent):
    FRIENDS_BUTTON = "//i[contains(@class,'ic_nav_friends-v2')]"

    def get_friends(self):
        #return WebDriverWait(self.driver, 10).until(e.visibility_of_element_located((By.XPATH, self.FRIENDS_BUTTON)))
        return self.driver.find_element_by_xpath(self.FRIENDS_BUTTON)
