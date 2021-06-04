from Pages.page import Page


class PeoplePage(Page):
    PATH = '/people/17'
    SUBSCRIBE_BUTTON = '//button[text()="Подписаться"]'
    UNSUBSCRIBE_BUTTON = '//button[text()="Отписаться"]'

    def subscribe(self):
        self.driver.find_element_by_xpath(self.SUBSCRIBE_BUTTON).click()
        self.driver.find_element_by_xpath(self.UNSUBSCRIBE_BUTTON)

    def unsubscribe(self):
        self.driver.find_element_by_xpath(self.UNSUBSCRIBE_BUTTON).click()
        self.driver.find_element_by_xpath(self.SUBSCRIBE_BUTTON)

