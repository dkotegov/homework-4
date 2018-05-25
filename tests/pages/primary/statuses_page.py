from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.primary.page import Page
from util import config


class StatusesPage(Page):
    LAST_SHARED_XPATH = '//div[@class="feed"][contains(@id, "status_")][@tsid="userStatusShares"]'

    DELETE_BUTTON_XPATH = '//a[@class="feed_close"][contains(@hrefattrs, "_aid=Shares_deleteButton")]'

    def unshare_last(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.LAST_SHARED_XPATH)))
        last_shared = self.driver.find_element_by_xpath(self.LAST_SHARED_XPATH)
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.DELETE_BUTTON_XPATH)))
        unshare_button = self.driver.find_element_by_xpath(self.DELETE_BUTTON_XPATH)
        hover = ActionChains(self.driver).move_to_element(last_shared)\
            .move_to_element(unshare_button).click(unshare_button)
        hover.perform()
