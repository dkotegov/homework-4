from components.base_component import BaseComponent

class PersonalDataForm(BaseComponent):
    NAME = "//input[@name='fr.name']"
    SURNAME = "//input[@name='fr.surname']"
    SAVE_BUTTON = "//input[@id='hook_FormButton_button_savePopLayerEditUserProfileNew']"
    CLOSE_BUTTON = "//input[@id='buttonId_button_close']"

    def name_surname(self, my_name, my_surname):
        name = self.get_visibility_element(self.NAME)
        self.driver.execute_script("arguments[0].value='" + my_name +"'", name)
        surname = self.get_visibility_element(self.SURNAME)
        self.driver.execute_script("arguments[0].value='" + my_surname +"'", surname)

    def save(self):
        self.get_clickable_element(self.SAVE_BUTTON).click()

    def close_save(self):
        self.get_clickable_element(self.CLOSE_BUTTON).click()

    ERROR_NAME_SURNAME = "//span[@class='input-e']"

    def name_surname_error(self):
        e1 = self.get_visibility_elements(self.ERROR_NAME_SURNAME)[0].text
        e2 = self.get_visibility_elements(self.ERROR_NAME_SURNAME)[1].text
        return e1, e2


class BaseSettingsForm(BaseComponent):
    PERSONAL_DATA = "//div[@class='user-settings_i_lk lstp-t al']"

    PROFILE1 = "//a[@class='compact-profile_a ellip-i']"

    def personal_data(self):
        personal_data = self.driver.find_elements_by_xpath(self.PERSONAL_DATA)[0]
        self.driver.execute_script("arguments[0].click();", personal_data)
        return PersonalDataForm(self.driver)

    def profile_get(self):
        return self.get_visibility_element(self.PROFILE1).text

    def profile_click(self):
        self.get_clickable_element(self.PROFILE1).click()
        #self.driver.find_element_by_xpath(self.PROFILE1).click()


