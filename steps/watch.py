from pages.watch import WatchPage
from steps.default import Steps


class WatchSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, WatchPage(driver))

    def back_to_menu(self):
        self.page.return_click()

    def hide_panels(self):
        self.page.menu.hide_panels_click()
        return self.page.menu.is_full_screen_visible()

    def show_panels(self):
        self.page.menu.show_panels_click()
        return self.page.menu.is_full_screen_visible()

    def show_legend(self, name):
        self.page.menu.legend_click(name)
        return self.page.menu.is_legend_visible()

    def hide_legend(self):
        self.page.menu.close_legend_click()
        return self.page.menu.is_legend_visible()

    def show_slide(self):
        self.page.menu.show_slide_click()
        return self.page.menu.is_slide_show_visible()

    def show_empty_slide(self):
        self.page.menu.show_slide_click()
        return self.accept_alert_text()

    def hide_slide(self):
        self.page.menu.close_slide_click()
        return self.page.menu.is_slide_show_visible()

    def open_legend_tab(self):
        self.page.menu.legend_tab_click()

    def wait_to_load(self):
        self.page.menu.wait_to_load()
