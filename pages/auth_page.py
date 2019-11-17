import os

from pages.default_page import DefaultPage

class AuthPage(DefaultPage):
    def getEmail(self):
        return os.getenv("EMAIL")

    def getPassword(self):
        return os.getenv("EMAILPASSWORD")

    def authorize(self):

        self.driver.get("https://e.mail.ru/settings/userinfo?afterReload=1")

        frame = self.wait_for_css_selector('#auth-form iframe')
        self.driver.switch_to.frame(frame)

        self.clear_and_send_keys_to_input('input[name=Login]', self.getEmail(), True, True)
        self.clear_and_send_keys_to_input('input[name=Password]', self.getPassword(), True, True)