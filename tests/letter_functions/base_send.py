from pages.letter_function_page import LetterFunctionsPage
from tests.base_test import BaseTest


class BaseSend(BaseTest):
    def writeLetter(self,subject, message):
        self.functions_form.open_writing_letter()
        self.functions_form.set_destionation_email()
        self.functions_form.click_on_subject_field()
        self.functions_form.write_some_text(subject)
        self.functions_form.click_on_message_field()
        self.functions_form.write_some_text(message)

    def test(self):
        BaseTest.test(self)
        self.functions_page = LetterFunctionsPage(self.driver)
        self.functions_form = self.functions_page.form
        self.functions_page.redirectQA()
