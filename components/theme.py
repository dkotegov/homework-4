from helpers import Component


class Theme(Component):
    HTML = "html"
    THEME = ".theme-box"

    LIGHT = "light"
    DARK = "dark"

    def get_theme(self):
        html = self.helpers.get_element(self.HTML)

        if self.helpers.is_element_contains_class(html,  "theme-light"):
            return self.LIGHT

        elif self.helpers.is_element_contains_class(html, "theme-dark"):
            return self.DARK

    def change_theme(self):
        self.helpers.click_element(self.THEME)

    def is_light_theme(self):
        return self.helpers.is_contains_class(self.HTML, self.LIGHT)

    def is_dark_theme(self):
        return self.helpers.is_contains_class(self.HTML, self.DARK)
