from components.base_component import BaseComponent


class GamesForm(BaseComponent):
    GAMES_CONTAINER = "//div[@class='ugrid']"

    def games_container(self):
        self.get_visibility_element(self.GAMES_CONTAINER)

