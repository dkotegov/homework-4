from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.AuthPageComponents.AuthForm import AuthForm
from tests.Components.Component import Component


class QuitPopUp(Component):
    CONFIRM_POPUP_OPENED = '//div[@id="hook_Form_PopLayerLogoffUserModalForm"]'
    QUIT_BUTTON = '//input[@name="logoff.confirm_not_decorate"]'

    def definitely_quit_profile(self):
        self.driver.find_element_by_xpath(self.QUIT_BUTTON).click()
        WebDriverWait(self.driver, 4, 2).until(
            lambda d: d.find_element_by_xpath(AuthForm.CONFIRM_AUTH_PAGE)
        )
