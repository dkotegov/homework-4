from pages.letter_formatting_page import LetterFormattingPage
from tests.base_test import BaseTest


class BaseFormatting(BaseTest):
    SAMPLE_TEXT = 'hello'
    NOT_BOLD_TEXT = '</strong>​​​​​​​' + SAMPLE_TEXT
    BOLD_TEXT = '<strong>​​​​​​​' + SAMPLE_TEXT + '</strong>'
    ITALIC_TEXT = '<em>​​​​​​​' + SAMPLE_TEXT + '</em>'
    UNDERLINED_TEXT = '<u>​​​​​​​' + SAMPLE_TEXT + '</u>'
    STRIKETHROUGH_TEXT = '<s>​​​​​​​' + SAMPLE_TEXT + '</s>'
    TEXT_COLOR = 'rgba(202, 242, 245, 1)'
    FONT_SIZE = '32px'
    LINE_HEIGHT = '40px'
    TEXT_ALIGN = 'right'
    MARGIN_LEFT = '40px'
    LISTED_TEXT = '<li>​​​​​​​' + SAMPLE_TEXT + '</li>'
    EMPTY_FIELD = '<br>'
    LINK = 'https://vk.com/'
    def test(self):
        BaseTest.test(self)
        self.letter_formatting_page = LetterFormattingPage(self.driver)
        self.letter_formatting_form = self.letter_formatting_page.form
        self.letter_formatting_page.redirectQA()
        self.letter_formatting_form.open_writing_letter()
