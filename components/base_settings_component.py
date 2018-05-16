from components.base_component import BaseComponent

class PersonalDataForm(BaseComponent):
    NAME = "//input[@name='fr.name']"
    SURNAME = "//input[@name='fr.surname']"
    SAVE_BUTTON = "//input[@id='hook_FormButton_button_savePopLayerEditUserProfileNew']"
    CLOSE_BUTTON = "//input[@id='buttonId_button_close']"

    def name_surname(self):
        name = self.driver.find_element_by_xpath(self.NAME)
        self.driver.execute_script("arguments[0].value='Name1'", name)
        surname = self.driver.find_element_by_xpath(self.SURNAME)
        self.driver.execute_script("arguments[0].value='Surname1'", surname)

    def save(self):
        self.driver.find_element_by_xpath(self.SAVE_BUTTON).click()

    def close_save(self):
        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

class BaseSettingsForm(BaseComponent):
    PERSONAL_DATA = "//div[@class='user-settings_i_lk lstp-t al']"

    PROFILE1 = "//a[@class='compact-profile_a ellip-i']"

    def personal_data(self):
        personal_data = self.driver.find_element_by_xpath(self.PERSONAL_DATA)
        self.driver.execute_script("arguments[0].click();", personal_data)
        return PersonalDataForm(self.driver)

    def profile_get(self):
        return self.driver.find_element_by_xpath(self.PROFILE1).text

    def profile_click(self):
        self.driver.find_element_by_xpath(self.PROFILE1).click()


