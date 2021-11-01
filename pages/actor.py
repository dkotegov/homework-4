from pages.default import Page
from utils import wait_for_element_by_selector


class ActorPage(Page):
    PATH = 'actors/'
    NAME_OF_ACTOR = '.name-born__name'

    def __init__(self, driver, id):
        super().__init__(driver)
        self.PATH += id

    def get_name_of_actor(self):
        return wait_for_element_by_selector(self.driver, self.NAME_OF_ACTOR).text
