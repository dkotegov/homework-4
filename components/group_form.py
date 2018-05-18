from components.base_component import BaseComponent


class GroupForm(BaseComponent):
    GROUP_DELETE = "//a[@class='dropdown_i']"
    GROUP_MENU = "//span[@class='dropdown_ac button-pro __with-arrow __sec']"
    GROUP_ADD = "//a[@id='button-pro __wide']"

    def group_add(self): 
        return self.get_clickable_element(self.GROUP_ADD)

    def group_menu(self): 
        return self.get_clickable_element(self.GROUP_MENU)

    def group_delete(self): 
        return self.get_clickable_element(self.GROUP_DELETE)
