from steps.default import DefaultSteps
from pages.create_new_file import CreateNewFilePage

class CreateNewFile(DefaultSteps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = CreateNewFilePage(driver)

    def create_new_doc(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_on_create_new()
        self.page.click_on_create_new_doc()
        self.page.switch_to_nth_tab(0)

    def create_new_table(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_on_create_new()
        self.page.click_on_create_new_table()

    def create_new_pptx(self):
        self.page.open()
        self.page.close_bubble()
        self.page.click_on_create_new()
        self.page.click_on_create_new_pres()


