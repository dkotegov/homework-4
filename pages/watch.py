from pages.default import Page, Component, wait_for_the_attribute_value


class WatchPage(Page):
    PATH = 'page/player'

    @property
    def menu(self):
        return Menu(self.driver)

    def return_click(self):
        self.driver.back()


class Menu(Component):
    HIDE_PANELS = '//div[@id="columnFullScreenMapBtn"]'
    SHOW_PANELS = '//div[@id="closeBigRightBtn"]'
    LAYER_TAB = '//td[@id="btn_sloy"]'
    LEGENDS_TAB = '//td[@id="btn_hist"]'
    SEARCH_INPUT = '//input[@id="findByTagPlayerField"]'
    SEARCH_BTN = '//div[@id="playerFindBtn"]'
    LEGEND = '//div[contains(@onclick, "historyShowMe")][.//span[contains(., "{name}")]]'
    LEGEND_BOX = '//div[@id="hitMetkaInfoBox"]'
    LEGEND_CLOSE = '//u[@onclick="closeMetInf()"]'
    SLIDE = '//span[@onclick="presentationSlideShowStart()"]'
    SLIDE_BOX = '//div[@id="legendImageShowBox"]'
    SLIDE_CLOSE = '//div[@onclick="hideLegShowB()"]'
    FULL_SCREEN = '//div[@id="myBiggestFullScreenBox"]'
    FULL_SCREEN_BOX = '//div[@id="bigFullScreenBox"]'

    def wait_to_load(self):
        self.wait_for_presence(self.FULL_SCREEN_BOX)
        self.wait_for_invisible(self.FULL_SCREEN_BOX)

    def hide_panels_click(self):
        self.wait_for_visible(self.HIDE_PANELS)
        self.driver.find_element_by_xpath(self.HIDE_PANELS).click()

    def show_panels_click(self):
        self.wait_for_visible(self.SHOW_PANELS)
        self.driver.find_element_by_xpath(self.SHOW_PANELS).click()

    def legend_tab_click(self):
        self.wait_for_presence(self.LEGENDS_TAB)
        self.driver.find_element_by_xpath(self.LEGENDS_TAB).click()

    def legend_click(self, name):
        self.wait_for_visible(self.LEGEND.format(name=name))
        self.driver.find_element_by_xpath(self.LEGEND.format(name=name)).click()

    def close_legend_click(self):
        self.wait_for_visible(self.LEGEND_CLOSE)
        self.driver.find_element_by_xpath(self.LEGEND_CLOSE).click()

    def show_slide_click(self):
        self.wait_for_visible(self.SLIDE)
        self.driver.find_element_by_xpath(self.SLIDE).click()

    def close_slide_click(self):
        self.wait_for_visible(self.SLIDE_CLOSE)
        self.driver.find_element_by_xpath(self.SLIDE_CLOSE).click()

    def is_legend_visible(self):
        self.wait_for_presence(self.LEGEND_BOX)
        return not self.driver.find_element_by_xpath(self.LEGEND_BOX).get_attribute("hidden")

    def is_full_screen_visible(self):
        self.wait_for_presence(self.FULL_SCREEN)
        return not self.driver.find_element_by_xpath(self.FULL_SCREEN).get_attribute("hidden")

    def is_slide_show_visible(self):
        self.wait_for_presence(self.SLIDE_BOX)
        return not self.driver.find_element_by_xpath(self.SLIDE_BOX).get_attribute("hidden")

