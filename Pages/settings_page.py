from Pages.page import Page


class SettingPage(Page):
    OLD = '//input[@placeholder="Старый пароль"]'
    NEW = '//input[@placeholder="Новый пароль"]'
    REPEAT = '//input[@placeholder="Повторите новый пароль"]'
    SUBMIT = '//button[text()="Сохранить"]'

    def set_old_pass(self, old):
        self.driver.find_element_by_xpath(self.OLD).send_keys(old)

    def set_new_pass(self, new):
        self.driver.find_element_by_xpath(self.NEW).send_keys(new)
        self.driver.find_element_by_xpath(self.REPEAT).send_keys(new)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
