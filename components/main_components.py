from components.base_component import BaseComponent

class MainForm(BaseComponent):
    PROFILE = "//h1[@class='mctc_name_tx bl']"
    def get_name_surname(self):
        return self.get_visibility_element(self.PROFILE).text

    DATE = "//div[@class='user-profile_i_value ellip']"
    def get_birthday(self):
        return self.get_visibility_element(self.DATE).text