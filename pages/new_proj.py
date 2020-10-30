from pages.default import Page, Component


class NewProjPage(Page):
    PATH = 'page/newproject'

    @property
    def form(self):
        return NewProjForm(self.driver)


class NewProjForm(Component):
    RETURN = '//div[@id="goToMainMenuBtn"]'
    NAME = '//input[@id="pNameField"]'
    DESCRIPTION = '//textarea[@id="pDescriptionField"]'
    CREATE = '//div[@id="projectAddBtn"]'

    def return_click(self):
        self.wait_for_visible(self.RETURN)
        self.driver.find_element_by_xpath(self.RETURN).click()

    def set_name(self, name):
        self.wait_for_visible(self.NAME)
        input_key = self.driver.find_element_by_xpath(self.NAME)
        input_key.clear()
        input_key.send_keys(name)

    def set_description(self, desc):
        self.wait_for_visible(self.DESCRIPTION)
        input_key = self.driver.find_element_by_xpath(self.DESCRIPTION)
        input_key.clear()
        input_key.send_keys(desc)

    def submit(self):
        self.wait_for_visible(self.CREATE)
        self.driver.find_element_by_xpath(self.CREATE).click()


