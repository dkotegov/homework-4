from components.letter_functions_form import LetterFunctionsForm
from pages.page import Page


class LetterFunctionsPage(Page):
    PATH = ''

    @property
    def form(self):
        return LetterFunctionsForm(self.driver)
