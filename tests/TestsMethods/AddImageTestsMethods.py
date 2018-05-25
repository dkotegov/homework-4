from tests.pages.primaryPhotoSection.AlbumPage import AlbumPage
from tests.pages.primaryPhotoSection.EditAlbumPage import EditAlbumPage
from tests.pages.primaryPhotoSection.PhotoSectionPage import PhotoSectionPage
from tests.pages.primaryPhotoSection.UploadedPhotoEditorPage import UploadedPhotoEditorPage


class AddImageTestsMethods:
    def __init__(self, driver):
        self.driver = driver

    def upload_image(self, name):
        photo_section_page = PhotoSectionPage(self.driver)
        add_photo_button = photo_section_page.add_photo_button
        add_photo_button.upload_file(name)

    def get_image_id_on_uploaded_photo_editor_page(self):
        uploaded_photo_editor_page = UploadedPhotoEditorPage(self.driver)
        uploaded_image_card = uploaded_photo_editor_page.uploaded_image_card
        return uploaded_image_card.get_uploaded_photo_id()

    def delete_photo_from_album_by_id(self, photo_id):
        album_page = AlbumPage(self.driver)
        action_panel = album_page.action_panel
        action_panel.edit_album()

        edit_album_page = EditAlbumPage(self.driver)
        list_of_photos = edit_album_page.list_of_photos
        list_of_photos.delete_photo_by_id(photo_id)

    def redirect_to_album_page_from_photo_section_page(self, album_name):
        photo_section_page = PhotoSectionPage(self.driver)
        photo_albums_list_bar = photo_section_page.photo_albums_list_bar
        photo_albums_list_bar.open_album_with_name(album_name)

    def wait_until_photo_downloaded(self):
        uploaded_photo_editor_page = UploadedPhotoEditorPage(self.driver)
        above_photo_panel = uploaded_photo_editor_page.above_photo_panel
        above_photo_panel.wait_until_photo_will_be_downloaded()

    def restore_photo_after_delete(self):
        edit_album_page = EditAlbumPage(self.driver)
        list_of_photos = edit_album_page.list_of_photos
        list_of_photos.restore_last_deleted_photo()

    def wait_until_photo_deleted(self):
        edit_album_page = EditAlbumPage(self.driver)
        list_of_photos = edit_album_page.list_of_photos
        list_of_photos.wait_until_photo_deleted()

    def redirect_from_edit_page_to_album_page(self):
        edit_album_page = EditAlbumPage(self.driver)
        list_of_photos = edit_album_page.list_of_photos
        list_of_photos.redirect_back_to_album_page()

    def cancel_photo_uploading(self):
        uploaded_photo_editor_page = UploadedPhotoEditorPage(self.driver)
        above_photo_panel = uploaded_photo_editor_page.above_photo_panel
        above_photo_panel.cancel_photo_uploading()
        above_photo_panel.wait_until_uploading_canceled()

    def get_number_of_photos_in_default_album(self):
        photo_section_page = PhotoSectionPage(self.driver)
        photo_albums_list_bar = photo_section_page.photo_albums_list_bar
        return photo_albums_list_bar.get_number_of_photos_in_default_album()
