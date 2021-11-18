from utils.random_strings import _randomMail
from tests.main.main_base_test import MainBaseTest

DEFAULT_DIALOGUE = "support@liokor.ru"

DEFAULT_AVATAR = "/images/default-avatar.jpg"
MAIL_AVATAR = "/images/mail.png"
YANDEX_AVATAR = "/images/yandex.png"
GMAIL_AVATAR = "/images/gmail.png"


class DialoguesTest(MainBaseTest):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.page.delete_all_dialogues()

    def tearDown(self) -> None:
        self.driver.refresh()
        self.page.delete_all_dialogues()

    def test_open_dialogue(self):
        self.page.clickDialogue(DEFAULT_DIALOGUE)
        self.page.wait_until(lambda d: self.page.isDialogueOpened(DEFAULT_DIALOGUE))

    def test_create_dialogue_positive(self):
        self._create_dialogue_with_name(_randomMail(15))

    def test_create_dialogue_positive_long_name(self):
        self._create_dialogue_with_name(_randomMail(150))

    def test_create_dialogue_positive_HTML_tags(self):
        self._create_dialogue_with_name("<p>No</p><strong>Very_strong</strong>@mail.ru")

    def test_create_dialogue_positive_cyrillic(self):
        self._create_dialogue_with_name("Здесь_дают_*three_hundred_bucks*@mail.ru")

    def test_create_dialogue_negative_incorrect_email(self):
        incorrect_email = _randomMail(15, "leo.o")
        self._create_dialogue_with_name_negative(incorrect_email)

    def test_create_dialogue_negative_spaces_in_name(self):
        mail = _randomMail(15)
        mail = mail[:5] + " " + mail[5:]
        self._create_dialogue_with_name_negative(mail)

    def test_create_dialogue_negative_empty_name(self):
        self._create_dialogue_with_name_negative("")

    def test_create_dialogue_negative_existed_name(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail)
        self.page.clickCreateDialogue()
        self.page.setFindDialogue(mail)
        self.page.clickCreateDialogue()

        self.assertTrue(self.page.isDialogueOpened(mail), "Dialogue opened")

    def test_find_dialogue(self):
        dialoguesNames = ["no_way@yandex.ru", "no_way@mail.ru", "way@yandex.ru"]
        for name in dialoguesNames:
            self._create_dialogue_with_name(name)

        self.page.setFindDialogue("no")
        self.page.wait_until(lambda d: self.page.getDialoguesCount() == 2)

        self.page.setFindDialogue("yandex")
        self.page.wait_until(lambda d: self.page.getDialoguesCount() == 2)

        self.page.setFindDialogue("way")
        self.page.wait_until(lambda d: self.page.getDialoguesCount() == 3)

        self.page.setFindDialogue("liokor")
        self.page.wait_until(lambda d: self.page.getDialoguesCount() == 1)

    def test_create_many_dialogues(self):
        oldAmount = self.page.getDialoguesCount()
        dialoguesAmount = 7
        dialoguesNames = [_randomMail(15) for _ in range(dialoguesAmount)]
        for name in dialoguesNames:
            self._create_dialogue_with_name(name)

        self.page.wait_until(lambda d: self.page.getDialoguesCount() == oldAmount + dialoguesAmount)

        self.page.clickDialogue(dialoguesNames[-1])
        self.assertTrue(self.page.isDialogueOpened(dialoguesNames[-1]), "Can't open last dialogue")

    def test_open_previous_dialogue_after_refresh(self):
        mail = _randomMail(15)
        self._create_dialogue_with_name(mail)

        self.assertTrue(self.page.isDialogueOpened(mail), "Dialogue not opened")

    def _test_dialogue_image(self, mail, expectedUrl):
        self._create_dialogue_with_name(mail)
        self.assertTrue(self.page.getDialogueImage(mail).endswith(expectedUrl), "Dialogue image is different")

    def test_dialogue_image_with_liokor(self):
        self._test_dialogue_image("liokor@liokor.ru", DEFAULT_AVATAR)

    def test_dialogue_image_with_yandex(self):
        self._test_dialogue_image("liokor@yandex.ru", YANDEX_AVATAR)

    def test_dialogue_image_with_ya(self):
        self._test_dialogue_image("liokor@ya.ru", YANDEX_AVATAR)

    def test_dialogue_image_with_mail(self):
        self._test_dialogue_image("liokor@mail.ru", MAIL_AVATAR)

    def test_dialogue_image_with_gmail(self):
        self._test_dialogue_image("liokor@gmail.com", GMAIL_AVATAR)
