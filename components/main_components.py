from components.base_component import BaseComponent

class MainForm(BaseComponent):
    PROFILE = "//h1[@class='mctc_name_tx bl']"
    def get_name_surname(self):
        return self.get_visibility_element(self.PROFILE).text