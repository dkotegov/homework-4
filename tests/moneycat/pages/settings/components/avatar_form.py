from testutils import Component
from selenium.webdriver.common.by import By


class AvatarForm(Component):
    container = '[data-test-id=settings__window]'

    class Selectors:
        email = 'p[id="username"]'
        submit = 'input[type="submit"]'
        error = 'div[id="message"]'

    def upload_file(self, path_to_file: str) -> None:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.submit)
        self.driver.find_element_by_css_selector(self.Selectors.submit).click().sendKeys(path_to_file)

    @property
    def email(self):
        return self.driver.find_element_by_css_selector(self.Selectors.email)

    @property
    def errors(self):
        return self.driver.find_element_by_css_selector(self.Selectors.error)
