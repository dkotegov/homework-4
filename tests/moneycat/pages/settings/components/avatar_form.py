from testutils import Component
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AvatarForm(Component):
    container = '[data-test-id=settings__window]'

    class Selectors:
        email = 'p[id="username"]'
        upload_file = 'input[id="upload-file"]'
        success_msg = 'div[class="message-content"]'
        submit = 'input[type="submit"]'

    def upload_file(self, path_to_file: str) -> None:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.submit)
        self._find(self.Selectors.upload_file).send_keys(path_to_file)

    @property
    def email(self):
        return self._wait_visible(By.CSS_SELECTOR, self.Selectors.email)

    @property
    def success_msg(self):
        return self._wait_visible(By.CSS_SELECTOR, self.Selectors.success_msg)

    @property
    def errors(self):
        return self._wait_visible(By.CSS_SELECTOR, self.Selectors.success_msg)
