from components.base_component import BaseComponent


class GroupsForm(BaseComponent):
    Groups_CONTAINER = "//div[@id='listBlockPanelFriendAltGroup2RBlock']"

    def groups_container(self):
        self.get_visibility_element(self.GROUPS_CONTAINER)

