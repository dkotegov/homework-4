from src.pages.base_page import BasePage
from src.components.elements.groups_element import GroupsElement


class GroupsPage(BasePage):

    def __init__(self, driver):
        super(GroupsPage, self).__init__(driver)
        self.element = GroupsElement(self.driver)

    def is_loaded(self):
        # TODO here you can add other logic
        is_marked = self.element.is_marked()
        return is_marked
