from pages.default import Page, Component


class SourcePage(Page):
    PATH = 'page/newsource'
    HEADER = '//h2[contains(text(), "Добавление ресурса")]'

    @property
    def form(self):
        return NewSourceForm(self.driver)


class NewSourceForm(Component):
    RETURN = '//div[@id="goToMainMenuBtn"]'
    SELECT_FILE_BTN = '//div[@id="toFileBtn"]'
    SELECT_FILE_INPUT = '//input[@id="mainFileBtn"]'
    SAVE = '//div[@id="saveSourceBtn"]'
    IMAGE = '//img[@id="imageField"]'

    def return_click(self):
        self.wait_for_visible(self.RETURN)
        self.driver.find_element_by_xpath(self.RETURN).click()

    def select_file_click(self):
        self.wait_for_visible(self.SELECT_FILE_BTN)
        self.driver.find_element_by_xpath(self.SELECT_FILE_BTN).click()

    def save_click(self):
        self.wait_for_visible(self.SAVE)
        self.driver.find_element_by_xpath(self.SAVE).click()

    def get_image_src(self):
        self.wait_for_visible(self.IMAGE)
        return self.driver.find_element_by_xpath(self.IMAGE).get_attribute("src")

    def load_image(self, name):
        self.wait_for_presence(self.SELECT_FILE_INPUT)
        self.driver.find_element_by_xpath(self.SELECT_FILE_INPUT).send_keys(name)
