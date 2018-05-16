import config
from library.selenium import Page, SeleniumTestCase
from library.ok.components import AuthForm


class OkPage(Page):
    def login(self):
        main_page = self
        if self.driver.current_url != MainPage.get_url():
            main_page = MainPage(self.driver).open()
        main_page.auth_form.set_login(config.get('LOGIN')).set_password(config.get('PASSWORD')).submit()
        if self.driver.current_url != MainPage.get_url():
            self.open()
        return self


class MainPage(OkPage):
    PATH = '/'
    AVATAR_ICON = '//div[@id="hook_Block_ToolbarUserDropdown"]/div'

    @property
    def auth_form(self):
        return AuthForm(self.driver)


class LoggedInTestCase(SeleniumTestCase):
    @classmethod
    def setUpClass(cls):
        super(LoggedInTestCase, cls).setUpClass()
        MainPage(cls.driver).open().login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()
        super(LoggedInTestCase, cls).tearDownClass()
