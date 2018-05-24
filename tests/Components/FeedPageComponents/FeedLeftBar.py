from tests.Components.Component import Component
from selenium.webdriver.support.ui import WebDriverWait


class FeedLeftBar(Component):
    PHOTO_LINK = '//a[@data-l="t,userPhotos"]'
    PHOTO_REDIRECT_CONFIRM = '//div[@class="photo-stream"]'

    def click_on_link_to_photo_section(self):
        self.driver.find_element_by_xpath(self.PHOTO_LINK).click()
        WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(self.PHOTO_REDIRECT_CONFIRM)
        )
