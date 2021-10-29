from pages.default_page import DefaultPage


class Theme(DefaultPage):
    THEME = ".theme-box"

    def get_theme(self):
        html = self.__get_element__("html")

        if self.__contains_class__(html, "theme-light"):
            return "light"

        elif self.__contains_class__(html, "theme-dark"):
            return "dark"

    def change_theme(self):
        self.__click_button__(self.THEME)
