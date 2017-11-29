from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class Input(BaseElement):
    INPUT = (By.XPATH, '//*[@uid="uidClickSimpleInput"]')
    DIV = (By.XPATH, '//*[@class="ok-e js-ok-e add-placeholder add-caret __empty"]')
    DIV_NOT_EMPTY = (By.XPATH, '//*[@class="ok-e js-ok-e add-placeholder add-caret"]')
    BUTTON_SEND = (By.XPATH, '//*[@uid="sendComment"]')
    BUTTON_EDIT_SEND = (By.XPATH, '//*[@uid="editCommentSave"]')