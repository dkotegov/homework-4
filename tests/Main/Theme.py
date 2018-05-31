from tests.Lilbs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class ThemePage(Page):
    @property
    def page(self):
        return ThemePage(self.driver)


class ThemeComponent(Component):

    START_THEME_NAME = ''
    CONFIRM_BTN_CSS = '[data-l="t\,confirm"]'

    def select(self):
        self.START_THEME_NAME = self.get_selected_theme()
        theme = Lib.simple_wait_elements_css(self.driver, 'div[class="covers_cat_lst_cnt"')[
            2].find_element_by_css_selector("a")
        theme.click()

    def apply(self):
        el = Lib.simple_wait_element_css(self.driver, self.CONFIRM_BTN_CSS)
        el.click()

    def get_selected_theme(self):
        return self.driver.find_element_by_css_selector('div[class="covers_cat_lst_cnt"] div[class*="selected"]').text.split(
            "\n")[0]
