from tests.Components.CommonComponents.MainTopContentBar import MainTopContentBar
from tests.Components.CommonComponents.NavigationToolBar import NavigationToolBar
from tests.Components.CommonComponents.QuitPopUp import QuitPopUp
from tests.pages.primaryPhotoSection.Page import Page


class CommonPage(Page):
    PATH = ''

    @property
    def navigation_toolbar(self):
        return NavigationToolBar(self.driver)

    @property
    def quit_popup(self):
        return QuitPopUp(self.driver)

    @property
    def main_top_content_bar(self):
        return MainTopContentBar(self.driver)