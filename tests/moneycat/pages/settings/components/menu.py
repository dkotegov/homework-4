from testutils import Component
from selenium.webdriver.common.by import By


class MenuForm(Component):
    container = '[data-test-id=control-panel]'

    class Selectors:
        pass_settings = 'div[class="action-btn"]:nth-child(2)'
        avatar_settings = 'div[class="action-btn"]:nth-child(1)'

    def click_pass(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.pass_settings).click()

    def click_avatar(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.avatar_settings).click()
