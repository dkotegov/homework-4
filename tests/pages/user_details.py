from selenium.webdriver.common.by import By

from tests.pages.base import Page
from tests.pages.component import FormComponent


class UserDetailsPage(Page):
    PATH = "/users/{0}"

    ROOT = {"method": By.XPATH, "key": Page.get_xpath_visible('//div[@id="user-page"]')}

    def __init__(self, driver, nickname):
        Page.__init__(self, driver)
        self.open(nickname)

    @property
    def form(self):
        return UserDetailsSubscribeForm(self.driver)


class UserDetailsSubscribeForm(FormComponent):
    subscribe_button = '//input[@class="button-subscribe"]'
    unsubscribe_button = '//input[@class="button-already-subscribe"]'
    pin = '//div[@class="pin-for-index-view"]'
    pin_name = '//a[@class="pin-for-index__content"]'

    def subscribe(self):
        self.driver.find_element_by_xpath(self.subscribe_button).click()

    def unsubscribe(self):
        self.driver.find_element_by_xpath(self.unsubscribe_button).click()

    # True if subscribed, False if not
    # TimeoutError if no button at all
    def check_subscription(self, estimated=True):
        checks = [
            {"target": self.unsubscribe_button, "result": True},
            {"target": self.subscribe_button, "result": False},
        ]
        plan = [0, 1]
        if not estimated:
            plan = [1, 0]

        for i in plan:
            try:
                self.wait_for_presence(By.XPATH, checks[i]["target"])
                return checks[i]["result"]
            except TimeoutError:
                pass
        else:
            raise TimeoutError

    def open_pin(self, index=0):
        pins = self.driver.find_elements_by_xpath(self.pin)
        assert len(pins) != 0
        pin = pins[index]

        pin_clickable = pin.find_element_by_xpath(self.pin_name)
        pin_name = pin_clickable.text
        pin_link = pin.find_element_by_tag_name("a").get_attribute("href")

        pin_clickable.click()

        return pin_name, pin_link
