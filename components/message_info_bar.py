from components.base_component import BaseComponent


class MessageInfoBar(BaseComponent):
    # INFO_BUTTON = "//div[@id='300935120']"
    INFO_BUTTON = "//div[@class='ic inlineBlock ic_info-menu']"
    BLACK_LIST_BUTTON = "//i[@class='tico_img ic ic_block']"
    ADDING_TO_BLACK_LIST_BUTTON = "//input[@id='hook_FormButton_menu_op_confirm_btn']"

    def get_info_button(self):
        return self.get_visibility_element(self.INFO_BUTTON)
        # return self.driver.find_element_by_xpath(self.INFO_BUTTON)

    def get_black_list_button(self):
        return self.get_clickable_element(self.BLACK_LIST_BUTTON)

    def accept_adding_to_black_list(self):
        return self.get_clickable_element(self.ADDING_TO_BLACK_LIST_BUTTON)
