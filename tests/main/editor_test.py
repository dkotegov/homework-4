from pages.main_page import MainPage
from pages.auth_page import AuthPage

from tests.base_test import BaseTest

DEFAULT_DIALOGUE = "support@liokor.ru"


class EditorTest(BaseTest):
    auth_page = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.auth_page = AuthPage(cls.driver)
        cls.auth_page.auth()

        cls.page = MainPage(cls.driver)
        cls.page.driver.maximize_window()

    def tearDown(self):
        self.page.setMessageBody('')

    def test_editor_bold(self):
        source = "Message body\nWith one string break."
        target = "Message **body**\nWith one string break."
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.selectTextInMessageInput(8, 4)
        self.page.clickRedactorBold()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_italic(self):
        source = "Message body\nWith one string break."
        target = "Message  _body_ \nWith one string break."
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.selectTextInMessageInput(8, 4)
        self.page.clickRedactorItalic()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_strikethrough(self):
        source = "Message body\nWith one string break."
        target = "Message  ~~body~~ \nWith one string break."
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.selectTextInMessageInput(8, 4)
        self.page.clickRedactorStrikethrough()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_code(self):
        source = "Message body\nWith one string break."
        target = "Message `body`\nWith one string break."
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.selectTextInMessageInput(8, 4)
        self.page.clickRedactorCode()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_H1(self):
        source = "Message body\nWith three string breaks\nThat's end\nOh, no, that's end"
        target = "Message body\n# With three string breaks\nThat's end\nOh, no, that's end"
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.selectLinesInMessageInput(1, 0)
        self.page.clickRedactorH1()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_H2(self):
        source = "Message body\nWith three string breaks\nThat's end\nOh, no, that's end"
        target = "Message body\n## With three string breaks\nThat's end\nOh, no, that's end"
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.selectLinesInMessageInput(1, 0)
        self.page.clickRedactorH2()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_H3(self):
        source = "Message body\nWith three string breaks\nThat's end\nOh, no, that's end"
        target = "Message body\n### With three string breaks\nThat's end\nOh, no, that's end"
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.selectLinesInMessageInput(1, 0)
        self.page.clickRedactorH3()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_blockquote(self):
        source = "Message body\nWith three string breaks\nThat's end\nOh, no, that's end"
        target = "Message body\n> With three string breaks\n> That's end\nOh, no, that's end"
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.selectLinesInMessageInput(1, 1)
        self.page.clickRedactorBlockquote()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_list(self):
        source = "Message body\nWith three string breaks\nThat's end\nOh, no, that's end"
        target = "Message body\n- With three string breaks\n- That's end\nOh, no, that's end"
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.selectLinesInMessageInput(1, 1)
        self.page.clickRedactorList()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_link(self):
        link = "http://ya.ru"
        text = "Yandex search"
        target = "[" + text + "](" + link + ")"
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody("")
        self.page.clickRedactorLink()
        self.page.fillOverlay(link)
        self.page.submitOverlay()
        self.page.fillOverlay(text)
        self.page.submitOverlay()
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    # TODO: Image load tests
    '''
    def test_editor_photo_positive(self):
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        clickf = self.page.clickRedactorPhoto
        self.page.enter_file_path(clickf, os.path.join(os.getcwd(), 'images', 'good_image.jpg'))
        self.assertTrue(self.page.is_popup_success(), "Image not loaded")
        self.assertTrue(self.page.getMessageBody().startswith("![image](https://mail.liokor.ru/api/media/files/"),
                        "Bad image markdown format")
    
    def test_editor_photo_negative(self):
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        clickf = self.page.clickRedactorPhoto
        self.page.enter_file_path(clickf, os.path.join(os.getcwd(), 'images', 'bad_image.jpg'))
        self.assertFalse(self.page.is_popup_success(), "Image loaded but mustn't")
    '''