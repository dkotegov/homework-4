from selenium.webdriver.common.by import By

from pages.default_page import DefaultPage


class ThemePage(DefaultPage):
    PATH = ""
    THEME = ".theme-box"

    def get_theme(self):
        html = self.driver.find_element(By.CSS_SELECTOR, "html")
        theme = html.get_attribute("class")

        if theme == "theme-light":
            return "light"

        elif theme == "theme-light":
            return "dark"

    def change_theme(self):
        self.__click_button__(self.THEME)
