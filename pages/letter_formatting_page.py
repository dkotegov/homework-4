from components.letter_formatting_form import LetterFormattingForm
from pages.page import Page


class LetterFormattingPage(Page):
    PATH = ''

    @property
    def form(self):
        return LetterFormattingForm(self.driver)
