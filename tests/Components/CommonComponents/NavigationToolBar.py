from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.CommonComponents.QuitPopUp import QuitPopUp
from tests.Components.Component import Component


class NavigationToolBar(Component):
    PROFILE_DROPDOWN_MENU = '//div[@data-module="Toolbar"]'
    QUIT_BUTTON = '//a[@data-l="t,logoutCurrentUser"]'

    def open_profile_menu(self):
        self.driver.find_element_by_xpath(self.PROFILE_DROPDOWN_MENU).click()

    def try_quit_profile(self):
        self.driver.find_element_by_xpath(self.QUIT_BUTTON).click()
        WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(QuitPopUp.CONFIRM_POPUP_OPENED)
        )