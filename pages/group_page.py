from components.group_component import GroupComponent
from pages.page import Page
from constants import dialog


class GroupPage(Page):
    PAGE = 'group/54182734987425'

    def __init__(self, driver):
        super(GroupPage, self).__init__(driver)
        self.group_component = GroupComponent(self.driver)

    def block_page(self):
        self.get_hover(self.group_component.get_start_block_button())
        self.group_component.get_block_button().click()

    def unblock_page(self):
        self.get_hover(self.group_component.get_start_block_button())
        self.group_component.get_unblock_button().click()

    def public_post(self):
        self.group_component.get_new_theme().click()
        self.group_component.get_message_input().send_keys(dialog.TEST_MESSAGE)
        self.group_component.get_send_button().click()

    def delete_post(self):
        self.get_hover(self.group_component.get_href_sender_item())
        self.get_hover(self.group_component.get_down_arrow())
        self.group_component.get_delete_button().click()

    def get_href_from_receiver_message(self):
        # href = self.group_component.get_href_item()
        try:
            if self.group_component.get_href_item() is False:
                return False
            return self.group_component.get_href_item().get_attribute('href')[-14:]
        except AttributeError:
            return False

    def get_href_from_sender_message(self):
        return self.group_component.get_href_sender_item().get_attribute('href')[-14:]
