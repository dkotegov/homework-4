from tests.Components.PhotoSectionPageComponents.AddPhotoButton import AddPhotoButton
from tests.Components.PhotoSectionPageComponents.CreateAlbumPopUp import CreateAlbumPopUp
from tests.Components.PhotoSectionPageComponents.PhotoAlbumsListBar import PhotoAlbumsListBar
from tests.pages.primaryPhotoSection.Page import Page


class PhotoSectionPage(Page):
    PATH = ''

    @property
    def photo_albums_list_bar(self):
        return PhotoAlbumsListBar(self.driver)

    @property
    def create_album_popup(self):
        return CreateAlbumPopUp(self.driver)

    @property
    def add_photo_button(self):
        return AddPhotoButton(self.driver)
