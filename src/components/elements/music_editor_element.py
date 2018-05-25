from src.components.base_element import BaseElement


class MusicEditorElement(BaseElement):

    MARKED_ITEM_NAV_BAR = '//a[@hrefattrs="st.cmd=userAltGroup&st._aid=NavMenu_User_AltGroups"]' \
                          '[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'

    XPATH_GRID = '//div[@class="music-gift_cnt"]'

    XPATH_BUTTON_SUBMIT = '//button[@class="modal_buttons_yes form-actions_yes button-pro"]'


    def get_grid(self):
        return self.get_field_by_xpath(self.XPATH_GRID)


    def get_first_music(self):
        grid = self.get_grid()
        return grid.find_element_by_class_name('track_cnt')

    def get_submit_button(self):
        return self.get_button_by_xpath(self.XPATH_BUTTON_SUBMIT)

