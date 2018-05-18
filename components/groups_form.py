from components.base_component import BaseComponent


class GroupsForm(BaseComponent):
    GROUPS_CONTAINER_BLOCKED = "//div[@class='stub-empty_t']"
    GROUPS_CONTAINER = "//div[@class='ugrid_cnt']"

    def groups_container_blocked(self):
        return self.get_visibility_element(self.GROUPS_CONTAINER_BLOCKED)

    def groups_container(self):
        return self.get_visibility_element(self.GROUPS_CONTAINER)

