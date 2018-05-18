# -*- coding: utf-8 -*-

from components.base_component import BaseComponent
import selenium
import time


class WarForm(BaseComponent):
    CITY = "//input[@name='st.layer.city']"
    def city(self):
        city = self.get_visibility_element(self.CITY)
        self.driver.execute_script("arguments[0].value='Москва'", city)
    UNIT = "//input[@name='st.layer.armyText']"
    UNIT2 = "//div[@class='sug_it_txt-div ellip']"
    BUTTON_OK = "//input[@id='hook_FormButton_button_join']"

    def unit(self):
        unit = self.driver.find_element_by_xpath(self.UNIT)
        unit.send_keys("83536")
        self.get_clickable_element(self.UNIT2).click()
        # self.get_clickable_element(self.UNIT2).click()
        # unit = self.get_visibility_element(self.UNIT)
        # self.driver.execute_script("arguments[0].value='83536'", unit)
        # time.sleep(1)
        # self.driver.execute_script("arguments[0].value+='6'", unit)

        # self.driver.execute_script("keyPressAndWait('83536')", unit)
        # self.get_clickable_element(self.UNIT2).click()

    def button_ok(self):
        self.get_clickable_element(self.BUTTON_OK).click()


class AboutForm(BaseComponent):
    REF = "//a[@class='user-profile_lk-o']"
    def war_data(self):
        self.get_visibility_elements(self.REF)[3].click()
        return WarForm(self.driver)

