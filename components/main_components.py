from components.base_component import BaseComponent


class MainForm(BaseComponent):
    PROFILE = "//h1[@class='mctc_name_tx bl']"

    def get_name_surname(self):
        return self.get_visibility_element(self.PROFILE).text

    DATE = "//div[@class='user-profile_i_value ellip']"

    def get_birthday(self):
        return self.get_visibility_element(self.DATE).text

    BIRTH_NOTE = "//span[@class='user-profile_i_t_inner']"

    def get_birth_note(self):
        return self.get_visibility_element(self.BIRTH_NOTE).text

    CURRENT_CITY = "//div[@class='user-profile_i_value ellip']"

    def get_current_city(self):
        return self.get_visibility_elements(self.CURRENT_CITY)[1].text