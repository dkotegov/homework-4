from components.base_component import BaseComponent
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class AboutForm(BaseComponent):
    MARITAL_STATUS_SPECIFY = "//span[@id='ownProfileLSBtn']"
    RELETIONSHIP = "//span[@class='lp-t ml']"
    ADD_RELETIONSHIP = "//div[@class='popUp_select_name']"
    BREAK_RELETIONSHIP = "//i[@class='tico_img ic ic_break_relations']"
    SEARCH_FRIEND = "//input[@id='ifSQtext']"

    def marital_status_specify(self):
        return self.get_clickable_element(self.MARITAL_STATUS_SPECIFY)

    def rilationship(self):
        return self.get_clickable_element(self.RELETIONSHIP)

    def add_rilationship(self):
        return self.get_clickable_element(self.ADD_RELETIONSHIP)

    def break_rilationship(self):
        return self.get_clickable_element(self.BREAK_RILATIONSHIP)

    def search_friend(self):
        return self.get_visibility_element(self.SEARCH_FRIEND)