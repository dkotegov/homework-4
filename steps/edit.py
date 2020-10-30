from pages.edit import EditPage
from steps.default import Steps


class EditSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, EditPage(driver))

    def back_to_menu(self):
        self.page.return_click()

    def open_pic_lib(self):
        self.page.tab.pic_lib_click()

    def open_pin_lib(self):
        self.page.tab.pin_lib_click()

    def open_text_lib(self):
        self.page.tab.text_lib_click()

    def open_leg_lib(self):
        self.page.tab.leg_lib_click()

    def open_group_lib(self):
        self.page.tab.group_lib_click()

    def open_control_lib(self):
        self.page.tab.control_lib_click()

    def open_zone_lib(self):
        self.page.tab.zone_lib_click()

    def create_legend(self, name):
        self.page.menu.set_leg_name(name)
        self.page.menu.save_leg_click()

    def default_leg_presence(self):
        return self.page.menu.default_leg_presence()

    def create_layer(self, path, name):
        self.page.menu.load_layer_img(path)
        self.page.menu.add_layer_click()
        self.page.accept_alert_input(name)

    def layer_presence(self):
        return self.page.menu.layer_presence()

    def layer_not_presence(self):
        return self.page.menu.layer_not_presence()

    def create_text(self, size):
        self.page.menu.set_text_size(size)
        self.page.menu.save_text()

    def default_text_size_presence(self):
        return self.page.menu.default_text_size_presence()

    def choose_pin(self, name):
        self.page.menu.watch_store_click()
        self.page.menu.watch_tag_click(name)
        return self.page.menu.get_tag_id()

    def save_pin(self, pin_id):
        self.page.menu.save_pin_click()
        self.page.accept_alert_input(pin_id)

    def pin_presence(self, pin_id):
        return self.page.menu.pin_presence(pin_id)

    def save_proj(self):
        self.page.menu.save_project_click()
        return self.accept_alert_text()
