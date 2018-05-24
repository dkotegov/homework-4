# -*- coding: utf-8 -*-

from components.base_component import BaseComponent


class ArmyForm(BaseComponent):
    CITY = "//input[@name='st.layer.city']"
    UNIT = "//input[@name='st.layer.armyText']"
    UNIT_LIST = "//div[@class='sug_it_txt-div ellip']"
    BUTTON_JOIN = "//input[@name='button_join']"

    ARMY_ERROR = "//span[@id='st.layer.armyValMess']"

    def add_city_unit(self, city, unit):
        self.put_city(city)
        self.add_unit(unit)

    def put_city(self, str):
        city = self.get_clickable_element(self.CITY)
        city.clear()
        city.send_keys(str)

    def add_unit(self, str):
        self.put_unit(str)
        self.select_unit()

    def put_unit(self, str):
        unit = self.get_clickable_element(self.UNIT)
        unit.clear()
        unit.send_keys(str)

    def select_unit(self):
        self.get_clickable_element(self.UNIT_LIST).click()

    def button_ok(self):
        self.get_clickable_element(self.BUTTON_JOIN).click()

    def army_error(self):
        return self.get_visibility_element(self.ARMY_ERROR).text
