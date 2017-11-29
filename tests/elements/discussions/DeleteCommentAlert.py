from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class DeleteCommentAlert(BaseElement):
    OK_BUTTON = (By.CSS_SELECTOR,'#ntfPopLayerArchiveConversation > div.panelLayer_b > div > div.formButtonContainer > input')