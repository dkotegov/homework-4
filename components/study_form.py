# -*- coding: utf-8 -*-

from components.base_component import BaseComponent


class StudyForm(BaseComponent):
    CITY = "//input[@name='st.layer.city']"
    JOB = "//input[@name='st.layer.schoolText']"

    CAREER_LIST = "//div[@class='sug_it_txt-div ellip']"
    JOB_LIST = "//div[@class='sug_it_txt-div ellip']"

    BUTTON_JOIN = "//input[@name='button_join']"

    CITY_ERROR = "//span[@id='st.layer.schoolCityValMess']"
    SCHOOL_ERROR = "//span[@id='st.layer.schoolValMess']"

    def add_city_school(self, city, unit):
        self.add_city(city)
        self.add_school(unit)

    def add_city(self, str):
        self.put_city(str)
        self.select_city()

    def put_city(self, str):
        city = self.get_visibility_element(self.CITY)
        city.clear()
        city.send_keys(str)

    def select_city(self):
        self.get_visibility_elements(self.CAREER_LIST)[0].click()

    def add_school(self, str):
        self.put_school(str)
        self.select_school()

    def put_school(self, str):
        unit = self.get_visibility_element(self.JOB)
        unit.send_keys(str)

    def select_school(self):
        self.get_visibility_elements(self.JOB_LIST)[0].click()

    def button_ok(self):
        self.get_clickable_element(self.BUTTON_JOIN).click()

    def city_error(self):
        return self.get_visibility_element(self.CITY_ERROR).text

    def school_error(self):
        return self.get_visibility_element(self.SCHOOL_ERROR).text
