from components.base_component import BaseComponent


class MessageDialog(BaseComponent):
    MESSAGE_INPUT = "//div[@class='itx js-comments_add js-ok-e comments_add-ceditable']"
    MESSAGE_SEND_BUTTON = "//button[@class='button-pro comments_add-controls_save']"

    def get_message_input(self):
        return self.get_visibility_element(self.MESSAGE_INPUT)
        #return self.driver.find_element_by_xpath(self.MESSAGE_INPUT)

    def get_message_send_button(self):
        #return self.get_clickable_element(self.MESSAGE_SEND_BUTTON)
        return self.driver.find_element_by_xpath(self.MESSAGE_SEND_BUTTON)
