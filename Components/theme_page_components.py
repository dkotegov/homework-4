# -*- coding: utf-8 -*-
from Components.component import Component
from selenium.webdriver.support.ui import WebDriverWait


class ThemeForm(Component):
    CREATE_THEME_DIV = u"//div[contains(@class,'posting-form_itx_dec')]/div[contains(text(),'Создать новую тему')]"
    THEME_TEXT = u"//div[@class='posting_itx emoji-tx h-mod js-ok-e ok-posting-handler']"
    SUBMIT = '//div[@data-action="submit"]'

    def open_form(self):
        # self.driver.find_element_by_xpath(self.CREATE_THEME_DIV).click()
        create_theme = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_THEME_DIV)
        )
        create_theme.click()

    def set_text(self,text="Default text"):
        text_field = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.THEME_TEXT)
        )
        text_field.send_keys(text)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()