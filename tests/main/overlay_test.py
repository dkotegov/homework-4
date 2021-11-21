from tests.main.main_base_test import MainBaseTest


class OverlayTest(MainBaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.page.delete_all_dialogues()

    def tearDown(self) -> None:
        self.page.delete_all_dialogues()

    def test_overlay(self):
        name = 'wolf@wolf.wolf'

        self._create_dialogue_with_name(name)

        self.page.clickDeleteDialogue(name)
        self.page.discardOverlayByNo()

        self.page.clickDeleteDialogue(name)
        self.page.discardOverlayByCross()

        self.assertEqual(self.page.getDialoguesCount(), 2)
