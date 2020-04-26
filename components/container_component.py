from components.base_component import Component


class Container(Component):

    def set_root(self, root):
        self.LOCATORS = {
            'ROOT': root,
        }

    def wait_for_container(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['ROOT'])
