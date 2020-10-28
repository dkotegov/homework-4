from pages.transform import TransformPage
from steps.default import Steps


class TransformSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, TransformPage(driver))

    def back_to_menu(self):
        self.page.form.return_click()

    def set_size(self, width, height):
        self.page.form.set_width(width)
        self.page.form.set_height(height)

    def select_image(self, name):
        self.page.form.load_image(name)

    def transform_finished(self):
        self.page.form.transform_click()
        return self.page.canvas.wait_for_canvas()

    def transform(self):
        self.page.form.transform_click()

    def check_size_label(self):
        return self.page.canvas.get_size_labels()

    def go_to_transform(self):
        return self.page.canvas.go_to_transform()

