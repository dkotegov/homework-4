from selenium.webdriver.remote.webelement import WebElement

from src.components.base_element import BaseElement


class GiftElement(BaseElement):

    GIFTS_MARKED_ITEM_NAV_BAR = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st._aid=NavMenu_User_Presents"]' \
                                '[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'

    AUTHORS_GIFTS_BUTTON = '//i[@class="tico_img ic ic_nav_bear"]'

    ACTUAL_GIFTS_BUTTON = '//i[@class="tico_img ic ic_nav_gifts"]'

    POSTACARDS_BUTTON = '//i[@class="tico_img ic ic_nav_flower"]'

    VIP_GIFT_BUTTON = '//i[@class="tico_img ic ic_nav_vipsale"]'

    CREATE_GIFT_BUTTON = '//a[@hrefattrs="st.cmd=appMain&st.appId=5738496"]'

    NEW_PRESENTS_GRID = '//div[@class="ugrid __xxxl __actualGifts __type_default"]'
    PRESENT_CLASS_NAME = 'gift_a'

    SECRET_BUTTON = '//input[@class="irc js-simpleSendPresent_chbx"][@id="anonymLabel"]'
    PRIVATE_BUTTON = '//input[@class="irc js-simpleSendPresent_chbx"][@id="privateLabel"]'

    RECEIVERS_GRID = '//ul[@class="ugrid_cnt"]'
    RECEIVER = 'photo_img'

    EDIT_TEXT_SEARCH_GIFT = '//input[@class="it search-input_it"][@id="gf-search-input"]'
    SEARCH_BUTTON = '//div[@id="gf-search-lupa"]'

    EDIT_TEXT_FIND_RECEIVER = '//input[@class="it search-input_it search-input_it h-mod"][@id="field_search_query"]'

    SELF_GIFTS_BUTTON = '//a[@href="/gifts/my"]'

    LIKE = '//span[@class="widget_cnt controls-list_lk h-mod"]'

    def is_marked(self):
        return self.existence_of_element_by_xpath(self.GIFTS_MARKED_ITEM_NAV_BAR)

    def get_authors_gift_button(self):
        return self.get_button_by_xpath(self.AUTHORS_GIFTS_BUTTON)

    def get_actual_gift_button(self):
        return self.get_button_by_xpath(self.ACTUAL_GIFTS_BUTTON)

    def get_postcard_button(self):
        return self.get_button_by_xpath(self.POSTACARDS_BUTTON)

    def get_vip_gift_button(self):
        return self.get_button_by_xpath(self.VIP_GIFT_BUTTON)

    def get_create_gift_button(self):
        return self.get_button_by_xpath(self.CREATE_GIFT_BUTTON)

    def get_present(self):
        #   getting grid with new presents
        new_presents_grid = self.get_button_by_xpath(self.NEW_PRESENTS_GRID)
        #   finding first element with class gift_a
        present = new_presents_grid.find_element_by_class_name(self.PRESENT_CLASS_NAME)
        return present

    def get_secret_button(self):
        return self.get_button_by_xpath(self.SECRET_BUTTON)

    def get_private_button(self):
        return self.get_button_by_xpath(self.PRIVATE_BUTTON)

    def get_receiver(self):
        receivers_grid = self.get_button_by_xpath(self.RECEIVERS_GRID)
        receiver = receivers_grid.find_element_by_class_name(self.RECEIVER)
        return receiver

    def get_edit_text(self):
        return self.get_button_by_xpath(self.EDIT_TEXT_SEARCH_GIFT)

    def get_edit_text_find_receiver(self):
        return self.get_button_by_xpath(self.EDIT_TEXT_FIND_RECEIVER)

    def get_search_button(self):
        return self.get_button_by_xpath(self.SEARCH_BUTTON)

    def get_send_gift_secretly_button(self):
        return self.get_button_by_xpath(self.CREATE_GIFT_BUTTON)

    def get_self_gifts_button(self):
        return self.get_button_by_xpath(self.SELF_GIFTS_BUTTON)

    def get_like_gift(self):
        return self.existence_of_element_by_xpath(self.LIKE)
