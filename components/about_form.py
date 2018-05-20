# -*- coding: utf-8 -*-

from components.base_component import BaseComponent
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class AboutForm(BaseComponent):
    MARITAL_STATUS_SPECIFY = "//span[@id='ownProfileLSBtn' and text()='Указать']"
    EDIT_RELETIONSHIP = "//span[@id='ownProfileLSBtn' and text()='Редактировать']"
    RELETIONSHIP = "//span[@class='lp-t ml']"
    ADD_RELETIONSHIP = "//div[@class='popUp_select_name']"
    BREAK_RELETIONSHIP = "//i[@class='tico_img ic ic_break_relations']"
    SEARCH_FRIEND = "//input[@id='ifSQtext']"
    RELETIONSHIP_CANSEL_REQUEST = "//a[@class='user-profile_lk-o' and text()='Отменить']"
    ALREADY_RELETIONSHIP = "//a[@class='o user-profile_i_relation-t']"

    def marital_status_specify(self):
        return self.get_clickable_element(self.MARITAL_STATUS_SPECIFY)

    def reletionship(self):
        return self.get_clickable_element(self.RELETIONSHIP)

    def add_reletionship(self):
        return self.get_clickable_element(self.ADD_RELETIONSHIP)

    def break_reletionship(self):
        return self.get_clickable_element(self.BREAK_RELETIONSHIP)

    def search_friend(self):
        return self.get_visibility_element(self.SEARCH_FRIEND)

    def reletionship_cansel_request(self):
        return self.get_clickable_element(self.RELETIONSHIP_CANSEL_REQUEST)

    def already_reletionship(self):
        return self.get_visibility_element(self.ALREADY_RELETIONSHIP)

    def edit_reletionship(self):
        return self.get_clickable_element(self.EDIT_RELETIONSHIP) 