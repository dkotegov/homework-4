from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class Input(BaseElement):
    INPUT = (By.XPATH, '//*[@uid="uidClickSimpleInput"]')
    DIV = (By.XPATH, '//*[@class="ok-e js-ok-e add-placeholder add-caret __empty"]')
    BUTTON_SEND = (By.XPATH, '//*[@uid="sendComment"]')