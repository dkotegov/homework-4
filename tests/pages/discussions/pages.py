from tests.pages.base import BasePage
from tests.elements.discussions.elements import Discussions
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.webdriver.common.by as by

class DiscPage(BasePage):
    url = 'http://ok.ru'

    def __init__(self, drv):
        super(DiscPage, self).__init__(drv)
        Discussions(drv).discussion_button().wait_for_clickable().get().click()

    def check_visible_user_info(self):
        achain = ActionChains(self.driver)
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        sleep(2)
        Discussions(self.driver).friends_selector().wait_for_clickable().get().click()
        Discussions(self.driver).scrollhead().wait_for_clickable().get().click()
        sleep(2)
        achain.move_to_element(Discussions(self.driver).comment_owner().wait_for_visible().get()).pause(2).perform()
        Discussions(self.driver).usercard().wait_for_visible().get()
        sleep(2)

    def downbutton_showed(self):
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        sleep(2)
        Discussions(self.driver).friends_selector().wait_for_clickable().get().click()
        Discussions(self.driver).scrollhead().wait_for_clickable().get().click()
        sleep(2)
        Discussions(self.driver).downbutton().wait_for_visible().get()
        sleep(2)

    def class_showed(self):
        achain = ActionChains(self.driver)
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        sleep(2)
        Discussions(self.driver).friends_selector().wait_for_clickable().get().click()
        sleep(2)
        achain.move_to_element(Discussions(self.driver).commentbody().wait_for_visible().get()).pause(2).perform()
        Discussions(self.driver).classpanel().wait_for_visible()

    def warn_showed(self):
        achain = ActionChains(self.driver)
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        sleep(2)
        Discussions(self.driver).friends_selector().wait_for_clickable().get().click()
        sleep(2)
        achain.move_to_element(Discussions(self.driver).commentbody().wait_for_visible().get()).pause(2).perform()
        Discussions(self.driver).warnpanel().wait_for_visible()

    def time_showed(self):
        achain = ActionChains(self.driver)
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        Discussions(self.driver).friends_disc().wait_for_clickable().get().click()
        sleep(2)
        Discussions(self.driver).friends_selector().wait_for_clickable().get().click()
        sleep(2)
        achain.move_to_element(Discussions(self.driver).commentbody().wait_for_visible().get()).pause(2).perform()
        Discussions(self.driver).timepanel().wait_for_visible()
