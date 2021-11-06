from helpers.component import Component


class Theme(Component):
    THEME = ".theme-box"

    def get_theme(self):
        html = self.helpers.get_element("html")

        if self.helpers.is_element_contains_class(html, "theme-light"):
            return "light"

        elif self.helpers.is_element_contains_class(html, "theme-dark"):
            return "dark"

    def change_theme(self):
        self.helpers.click_element(self.THEME)
