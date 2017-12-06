from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class DiscussionOwner(BaseElement):
    A = (By.XPATH, '//a[@uid="goToOwnerHeader"]')
