from tests.Components.UploadedPhotoEditorPageComponents.AbovePhotoPanel import AbovePhotoPanel
from tests.Components.UploadedPhotoEditorPageComponents.CreateNoteForm import CreateNoteForm
from tests.Components.UploadedPhotoEditorPageComponents.UploadedImageCard import UploadedImageCard
from tests.pages.primaryPhotoSection.Page import Page


class UploadedPhotoEditorPage(Page):
    PATH = ''

    @property
    def above_photo_panel(self):
        return AbovePhotoPanel(self.driver)

    @property
    def create_note_form(self):
        return CreateNoteForm(self.driver)

    @property
    def uploaded_image_card(self):
        return UploadedImageCard(self.driver)
