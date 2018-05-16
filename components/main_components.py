from components.base_component import BaseComponent

class MainForm(BaseComponent):
    PROFILE = "//h1[@class='mctc_name_tx bl']"
    def get_name_surname(self):
        return self.driver.find_element_by_xpath(self.PROFILE).text