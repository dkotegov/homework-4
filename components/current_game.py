from components.base_component import BaseComponent


class CurrentGame(BaseComponent):
    INFORMATION_ABOUT_THE_GAME_BUTTON = "//em[@class='tico_simb_txt']"
    NOTIFICATION_BUTTON = "//li[@class='inav-drop_li']"
    CONFIRM_BUTTON = "//input[@data-l='t,confirm']"

    def get_information_about_the_game_button(self):
        return self.driver.find_element_by_xpath(self.INFORMATION_ABOUT_THE_GAME_BUTTON)

    def get_notification_button(self):
        return self.get_elements_by_path(self.NOTIFICATION_BUTTON)[3]

    def get_confirm_button(self):
        return self.get_clickable_element(self.CONFIRM_BUTTON)
