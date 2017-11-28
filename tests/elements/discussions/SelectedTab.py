from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class SelectedTab(BaseElement):
    SELECTED_TAB = (By.XPATH,"//div[@class=toggle-span-selected]")