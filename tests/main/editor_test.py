import os

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

        cls.page.open()

    def tearDown(self):
        self.page.setMessageBody('')

    def test_editor_bold(self):
        source = "wolf"
        target = "**wolf**"
        
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.editorSelectAll()
        self.page.clickRedactorBold()

        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_italic(self):
        source = "wolf"
        target = "*wolf*"
        
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.editorSelectAll()
        self.page.clickRedactorItalic()
        
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_strikethrough(self):
        source = "wolf"
        target = "~~wolf~~"
        
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.editorSelectAll()
        self.page.clickRedactorStrikethrough()
        
        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_code(self):
        source = "wolf"
        target = "`wolf`"

        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.editorSelectAll()
        self.page.clickRedactorCode()

        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_H1(self):
        source = "wolf"
        target = "# wolf"

        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.editorSelectAll()
        self.page.clickRedactorH1()

        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_H2(self):
        source = "wolf"
        target = "## wolf"

        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.editorSelectAll()
        self.page.clickRedactorH2()

        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_H3(self):
        source = "wolf"
        target = "### wolf"

        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.editorSelectAll()
        self.page.clickRedactorH3()

        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_blockquote(self):
        source = "wolf\nlion"
        target = "> wolf\n> lion"

        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.editorSelectAll()
        self.page.clickRedactorBlockquote()

        self.assertEqual(self.page.getMessageBody(), target, "Message body unexpected")

    def test_editor_list(self):
        source = "wolf\nlion"
        target = "- wolf\n- lion"

        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody(source)
        self.page.editorSelectAll()
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

    def test_editor_photo_positive(self):
        if not self.page.is_windows():
            return

        target_start = "![image](https://mail.liokor.ru/api/media/files/"

        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.setMessageBody("")

        image_path = os.path.join(os.getcwd(), "images", "good_image.jpg")
        self.page.send_file(self.page.clickRedactorPhoto, image_path)

        self.assertTrue(self.page.is_popup_success(), "Image not loaded")
        self.assertTrue(self.page.getMessageBody().startswith(target_start), "Bad image markdown format")
