from pages.default import Page, Component


class TransformPage(Page):
    PATH = 'page/transformation'

    @property
    def form(self):
        return TransformForm(self.driver)

    @property
    def canvas(self):
        return CanvasWindow(self.driver)


class TransformForm(Component):
    RETURN = '//div[@onclick="goMainMenu()"]'
    WIDTH_INPUT = '//input[@id="fieldWidth"]'
    HEIGHT_INPUT = '//input[@id="fieldHeight"]'
    SELECT_FILE_INPUT = '//input[@onchange="workWithThisFile(this.files)"]'
    TRANSFORM = '//div[@onclick="transformBtnClick()"]'
    CANVAS = '//canvas[@id="myCanvas"]'

    def return_click(self):
        self.wait_for_visible(self.RETURN)
        self.driver.find_element_by_xpath(self.RETURN).click()

    def set_width(self, width):
        self.wait_for_visible(self.WIDTH_INPUT)
        input_width = self.driver.find_element_by_xpath(self.WIDTH_INPUT)
        input_width.clear()
        input_width.send_keys(width)

    def set_height(self, height):
        self.wait_for_visible(self.HEIGHT_INPUT)
        input_height = self.driver.find_element_by_xpath(self.HEIGHT_INPUT)
        input_height.clear()
        input_height.send_keys(height)

    def load_image(self, name):
        self.wait_for_presence(self.SELECT_FILE_INPUT)
        self.driver.find_element_by_xpath(self.SELECT_FILE_INPUT).send_keys(name)

    def transform_click(self):
        self.wait_for_visible(self.TRANSFORM)
        self.driver.find_element_by_xpath(self.TRANSFORM).click()


class CanvasWindow(Component):
    RETURN = '//div[@onclick="goMainMenu()"]'
    REPEAT = '//div[@onclick="updatePage()"]'
    CANVAS = '//canvas[@id="myCanvas"]'
    SIZE_LABEL = '//td[contains(., "Ширина:")][contains(., "Высота:")]'

    def return_click(self):
        self.wait_for_visible(self.RETURN)
        self.driver.find_element_by_xpath(self.RETURN).click()

    def wait_for_canvas(self):
        self.wait_for_visible(self.CANVAS)
        canvas = self.driver.find_element_by_xpath(self.CANVAS)
        width = canvas.get_attribute("width")
        height = canvas.get_attribute("height")
        return width, height

    def get_size_labels(self):
        self.wait_for_visible(self.SIZE_LABEL)
        size = self.driver.find_element_by_xpath(self.SIZE_LABEL)
        return size.get_attribute("innerText")

    def go_to_transform(self):
        self.wait_for_visible(self.REPEAT)
        self.driver.find_element_by_xpath(self.REPEAT).click()



