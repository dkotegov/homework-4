from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class MainHeader(Component):
    NICKNAME = '//div[@class="main-header-right__nickname"]'

    def get_nickname(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NICKNAME).text.replace('@', '', 1)
        )
