from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class MailPage(Page):
    def switch_to_ab(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                             '.widget__link.js-shortcut')))
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                             '.widget__link.js-shortcut'))).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.messagelist-wrapper')))
