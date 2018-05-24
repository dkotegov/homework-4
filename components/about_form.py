# -*- coding: utf-8 -*-

from components.base_component import BaseComponent
from components.army_form import ArmyForm
from components.career_form import CareerForm
from components.study_form import StudyForm
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
    REF = "//a[@class='user-profile_lk-o']"
    BUTTON_CLOSE_POPUP = "//a[@id='nohook_modal_close']"
    TOP_UNIT = "//span[@title='134523, Москва, Россия']"
    TOP_JOB = "//span[@title='\"Красное и белое\", Москва, Россия']"
    TOP_SCHOOL = "//span[@title='1 школа, Москва, Россия']"

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

    def career_form(self):
        self.get_visibility_elements(self.REF)[1].click()
        return CareerForm(self.driver)

    def study_form(self):
        self.get_visibility_elements(self.REF)[2].click()
        return StudyForm(self.driver)

    def army_form(self):
        self.get_visibility_elements(self.REF)[3].click()
        return ArmyForm(self.driver)

    def close_popup(self):
        self.get_clickable_element(self.BUTTON_CLOSE_POPUP).click()

    def get_top_job(self):
        return self.get_visibility_element(self.TOP_JOB)

    def get_top_school(self):
        return self.get_visibility_element(self.TOP_SCHOOL)

    def get_top_unit(self):
        return self.get_visibility_element(self.TOP_UNIT)
