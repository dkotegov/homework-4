
from pages.defaultPage import Page, Component
from selenium.webdriver.support.ui import WebDriverWait

from tests.feed.commonUtils import get_names_from_sub_item_html
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProfilePage(Page):
    PATH = ''

    @property
    def profile_area(self):
        return ProfileArea(self.driver)


class ProfileArea(Component):
    DESK_PREVIEW = '//*[@class="deskPreview"]'

    ALL_USERS_LINK = '//*[@id="allUserPinsLink"]'

    SHOW_FOLLOW = '//*[@id="followBlock"]/a[2]/div'

    SHOW_LIST = '//*[@id="follow_7"]'

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

    def get_my_subs_names(self):

        show_foll_el = WebDriverWait(self.driver, 20, 0.1).until(EC.element_to_be_clickable((By.XPATH,
                                                                                   self.SHOW_FOLLOW)))
        show_foll_el.click()

        subs_list_html = WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SHOW_LIST).get_attribute('innerHTML')
        )
        return get_names_from_sub_item_html(subs_list_html)
