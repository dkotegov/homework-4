# -*- coding: utf-8 -*-

from components.base_component import BaseComponent
from components.army_form import ArmyForm
from components.career_form import CareerForm
from components.study_form import StudyForm

class AboutForm(BaseComponent):
    REF = "//a[@class='user-profile_lk-o']"
    BUTTON_CLOSE_POPUP = "//a[@id='nohook_modal_close']"
    TOP_UNIT = "//span[@title='134523, Москва, Россия']"
    TOP_JOB = "//span[@title='\"Красное и белое\", Москва, Россия']"
    TOP_SCHOOL = "//span[@title='1 школа, Москва, Россия']"

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
