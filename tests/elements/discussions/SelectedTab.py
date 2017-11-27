from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class SelectedTab(BaseElement):
    GET = (By.XPATH,"//div[@class=toggle-span-selected]")