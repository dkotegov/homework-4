from src.components.elements.music_editor_element import MusicEditorElement
from src.pages.base_page import BasePage



class MusicEditor(BasePage):

    def __init__(self, driver):
        super(MusicEditor, self).__init__(driver)
        self._element = MusicEditorElement(self.driver)

    def select_sound(self):
        btn = self._element.get_first_music()
        btn.click()
        submit_btn = self._element.get_submit_button()
        submit_btn.click()
        return GiftPage(self.driver)

from src.pages.gift_page import GiftPage