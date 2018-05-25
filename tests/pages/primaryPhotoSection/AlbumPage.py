from tests.Components.AlbumPageComponents.AlbumActionPanel import AlbumActionPanel
from tests.Components.AlbumPageComponents.ListOfPhotos import ListOfPhotos
from tests.pages.primaryPhotoSection.Page import Page


class AlbumPage(Page):
    PATH = ''

    @property
    def action_panel(self):
        return AlbumActionPanel(self.driver)

    @property
    def list_of_photos(self):
        return ListOfPhotos(self.driver)