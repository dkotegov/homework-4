from components.file_attaching_form import FileAttachingForm
from pages.page import Page


class FileAttachingPage(Page):
    PATH = ''

    @property
    def form(self):
        return FileAttachingForm(self.driver)
