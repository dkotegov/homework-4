from pages.defaultPage import Page, Component
from selenium.webdriver.support.ui import WebDriverWait


class ProfilePage(Page):
    PATH = ''

    @property
    def profile_area(self):
        return ProfileArea(self.driver)


class ProfileArea(Component):
    DESK_PREVIEW = '//*[@class="deskPreview"]'

    ALL_USERS_LINK = '//*[@id="allUserPinsLink"]'

    def click_my_pins(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ALL_USERS_LINK)
        )
        self.driver.find_element_by_xpath(self.ALL_USERS_LINK).click()

    def click_my_desk(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DESK_PREVIEW)
        )
        self.driver.find_element_by_xpath(self.DESK_PREVIEW).click()
