from src.pages.base_page import BasePage
from src.components.elements.notes_element import NotesElement


class NotesPage(BasePage):

    def __init__(self, driver):
        super(NotesPage, self).__init__(driver)
        self.element = NotesElement(self.driver)

    def is_loaded(self):
        # TODO here you can add other logic
        is_marked = self.element.is_marked()
        return is_marked
