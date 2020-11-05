from selenium.webdriver.support.ui import WebDriverWait

from base_classes.component import Component


class BoardsForm(Component):
    CONTAINER = '//div[@class="boards"]'
