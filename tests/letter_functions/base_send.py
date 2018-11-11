from pages.letter_function_page import LetterFunctionsPage
from tests.base_test import BaseTest


class BaseSend(BaseTest):
    def test(self):
        BaseTest.test(self)
        self.functions_page = LetterFunctionsPage(self.driver)
        self.functions_form = self.functions_page.form
