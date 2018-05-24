from tests.pages.primaryPhotoSection.AlbumPage import AlbumPage
from tests.pages.primaryPhotoSection.EditAlbumPage import EditAlbumPage
from tests.pages.primaryPhotoSection.PhotoSectionPage import PhotoSectionPage


class CreateAlbumTestsMethods:

    def __init__(self, driver):
        self.driver = driver

    def create_album_from_photo_section_page(self, name):

        photo_section_page = PhotoSectionPage(self.driver)

        photo_album_list = photo_section_page.photo_albums_list_bar
        photo_album_list.open_create_album_popup()

        create_album_popup = photo_section_page.create_album_popup
        create_album_popup.set_album_name(name)
        create_album_popup.submit_album_creation()

    def delete_album_from_photo_section(self, name):
        photo_section_page = PhotoSectionPage(self.driver)

        photo_album_list = photo_section_page.photo_albums_list_bar
        photo_album_list.open_album_with_name(name)

        album_page = AlbumPage(self.driver)
        album_action_panel = album_page.action_panel
        album_action_panel.edit_album()

        edit_album_page = EditAlbumPage(self.driver)

        edit_album_action_panel = edit_album_page.action_panel
        edit_album_action_panel.open_delete_album_popup()

        delete_album_popup = edit_album_page.delete_album_popup
        delete_album_popup.press_delete_button_in_popup()

    def close_create_album_popup(self):
        photo_section_page = PhotoSectionPage(self.driver)
        create_album_popup = photo_section_page.create_album_popup
        create_album_popup.close_create_album_popup()
