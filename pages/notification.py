from pages.defaultPage import Page, Component
from selenium.webdriver.support.ui import WebDriverWait


class Notification(Page):
    PATH = 'notifications'

    @property
    def notification_modal(self):
        return NotificationModal(self.driver)

    @property
    def top_menu(self):
        return TopMenu(self.driver)


class NotificationModal(Component):
    NOTIF_HELLO_MSG = '//*[@class="mini_title"]'
    NOTIF_LOAD_MSG = '//*[@id="content"]/h2'
    NOTIF_BLOCK = '//*[@id="notifBlock"]'


    def get_msg(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NOTIF_HELLO_MSG)
        )
        return self.driver.find_element_by_xpath(self.NOTIF_HELLO_MSG).get_attribute('innerText')

    def get_load_notif_msg(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NOTIF_LOAD_MSG)
        )
        return self.driver.find_element_by_xpath(self.NOTIF_LOAD_MSG).get_attribute('innerText')

    def get_last_notif_text(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NOTIF_BLOCK)
        )
        html = self.driver.find_element_by_xpath(self.NOTIF_BLOCK).get_attribute('innerHTML')
        return html.split('class="notif_text">')[1].split('</div>')[0]




class TopMenu(Component):
    PROFILE_LINK = '//*[@id="profileLink"]'

    def go_to_my_profile(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PROFILE_LINK)
        )
        self.driver.find_element_by_xpath(self.PROFILE_LINK).click()

    def go_to_sup_profile(self):
        self.driver.get('https://zinterest.ru/user/1')
