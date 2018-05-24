# -*- coding: utf-8 -*-
from components.base_component import BaseComponent


class GroupForm(BaseComponent):
    GROUP_DELETE = "//a[@class='dropdown_i']"
    GROUP_MENU = "//span[@class='dropdown_ac button-pro __with-arrow __sec']"
    GROUP_ADD = "//a[@class='button-pro __wide']"
    GROUP_INVITE_FRIENDS = "//span[@class ='tico' and text() = '"
    GROUP_FRIEND_INVITE = "//div[@data-id = '569689583231'"
    GROUP_INVITE_BUTTON = "//input[@id = 'hook_FormButton_button_invite']"
    GROUP_FRIEND_INVITE_SEARCH = "//input[@id='inviteFriends_field_query']"
    # GROUP_INVITE_BLOCKED = "//tico_img ic ic_closed"

    def group_add(self): 
        return self.get_clickable_element(self.GROUP_ADD)

    def group_menu(self): 
        return self.get_clickable_element(self.GROUP_MENU)

    def group_delete(self): 
        return self.get_clickable_element(self.GROUP_DELETE)

    def group_invite_friends(self): 
    	text = u'Пригласить друзей'
        return self.get_clickable_element(self.GROUP_INVITE_FRIENDS + text + "']")

    def group_friend_invite(self): 
        return self.get_clickable_element(self.GROUP_FRIEND_INVITE)

    def group_invite_button(self): 
        return self.get_clickable_element(self.GROUP_INVITE_BUTTON)

    def group_invite_search(self): 
        return self.get_clickable_element(self.GROUP_FRIEND_INVITE_SEARCH)