from src.pages.base_page import BasePage
from src.components.elements.photo_element import PhotoElement


class PhotoPage(BasePage):

    def __init__(self, driver):
        super(PhotoPage, self).__init__(driver)
        self.element = PhotoElement(self.driver)

    def is_loaded(self):
        # TODO here you can add other logic
        is_marked = self.element.is_marked()
        return is_marked
