from pages.default import Page, Component, wait_for_the_attribute_value


class EditPage(Page):
    PATH = 'page/constructor'

    @property
    def map(self):
        return Map(self.driver)

    @property
    def tab(self):
        return Tab(self.driver)

    @property
    def menu(self):
        return Tab(self.driver)

    def return_click(self):
        self.driver.back()


class Map(Component):
    PIC_LIB = '//h3[@id="ui-id-1"]'

    def pic_lib_click(self):
        self.wait_for_visible(self.PIC_LIB)
        self.driver.find_element_by_xpath(self.PIC_LIB).click()


class Menu(Component):
    LEG_NAME_INPUT = '//input[@id="histName"]'
    TEXT_SIZE_INPUT = '//input[@id="sizeShriftField"]'
    ADD_TEXT_BTN = '//div[@id="createNewLabelBtn"]'
    TEXT_LABEL = '//div[@id="label_text_label_text_0"]'
    SAVE_LEG_BTN = '//div[@onclick="histLegendSave()"]'
    SAVED_LEG = '//div[@class="history-legend-class"][img[contains(@src,"cleverMan")]]'
    WATCH_STORE_BTN = '//div[@onclick="watchMetkaStore()"]'
    WATCH_TAG_BTN = '//span[contains(@onclick, "opTag")][contains(@onclick, "{name}")]'
    WATCH_TAG_ID = '//div[@id="storeContentMetkiBufBox"]//b'
    LOAD_PIN_BTN = '//div[@id="loadNewMetkiBtn"]'
    SAVED_PIN = '//div[@class="metka-list-class-metka-elem"][contains(., "Метка {pin_id}")]'
    SAVE_PROJ_BTN = '//div[@id="saveProjectBtn"]'
    LOAD_LAYER = '//div[@id="uploadingFileInputBtn"]'
    ADD_LAYER = '//div[@onclick="addToScene(this, 200, 150, 100, 100)"]'
    LAYER = '//img[contains(@id, "lay_lay")]'

    def load_layer_img(self, name):
        self.wait_for_visible(self.LOAD_LAYER)
        self.driver.find_element_by_xpath(self.LOAD_LAYER).send_keys(name)

    def add_layer_click(self):
        self.wait_for_visible(self.ADD_LAYER)
        self.driver.find_element_by_xpath(self.ADD_LAYER).click()

    def layer_presence(self):
        self.wait_for_visible(self.LAYER)
        return self.driver.find_element_by_xpath(self.LAYER).get_attribute("src")

    def layer_not_presence(self):
        self.do_not_wait_presence(self.LAYER)

    def set_text_size(self, size):
        self.wait_for_visible(self.TEXT_SIZE_INPUT)
        self.driver.find_element_by_xpath(self.TEXT_SIZE_INPUT).send_keys(size)

    def save_text(self):
        self.wait_for_visible(self.ADD_TEXT_BTN)
        self.driver.find_element_by_xpath(self.ADD_TEXT_BTN).click()

    def default_text_size_presence(self):
        self.wait_for_visible(self.TEXT_LABEL)
        return self.driver.find_element_by_xpath(self.TEXT_LABEL).get_attribute("style")

    def set_leg_name(self, name):
        self.wait_for_visible(self.LEG_NAME_INPUT)
        self.driver.find_element_by_xpath(self.LEG_NAME_INPUT).send_keys(name)

    def save_leg_click(self):
        self.wait_for_visible(self.SAVE_LEG_BTN)
        self.driver.find_element_by_xpath(self.SAVE_LEG_BTN).click()

    def default_leg_presence(self):
        self.wait_for_visible(self.SAVED_LEG)
        return self.driver.find_element_by_xpath(self.SAVED_LEG).get_attribute("innerText")

    def watch_store_click(self):
        self.wait_for_visible(self.WATCH_STORE_BTN)
        return self.driver.find_element_by_xpath(self.WATCH_STORE_BTN).click()

    def watch_tag_click(self, name):
        self.wait_for_visible(self.WATCH_TAG_BTN.format(name=name))
        return self.driver.find_element_by_xpath(self.WATCH_TAG_BTN.format(name=name)).click()

    def get_tag_id(self, name):
        self.wait_for_visible(self.WATCH_TAG_ID.format(name=name))
        return self.driver.find_element_by_xpath(self.WATCH_TAG_ID.format(name=name)).get_attribute("innerText")

    def save_pin_click(self):
        self.wait_for_visible(self.LOAD_PIN_BTN)
        return self.driver.find_element_by_xpath(self.LOAD_PIN_BTN).click()

    def pin_presence(self, pin_id):
        self.wait_for_visible(self.SAVED_PIN.format(pin_id=pin_id))
        return self.driver.find_element_by_xpath(self.SAVED_PIN.format(pin_id=pin_id)).get_attribute("innerText")


class Tab(Component):
    PIC_LIB = '//h3[@id="ui-id-1"]'
    PIN_LIB = '//h3[@id="ui-id-2"]'
    TEXT_LIB = '//h3[@id="ui-id-3"]'
    LEG_LIB = '//h3[@id="ui-id-4"]'
    ZONE_LIB = '//h3[@id="ui-id-5"]'
    GROUP_LIB = '//h3[@id="ui-id-6"]'
    CONTROL_LIB = '//h3[@id="ui-id-7"]'

    def return_click(self):
        self.driver.back()

    def pic_lib_click(self):
        self.wait_for_visible(self.PIC_LIB)
        self.driver.find_element_by_xpath(self.PIC_LIB).click()

    def pin_lib_click(self):
        self.wait_for_visible(self.PIN_LIB)
        self.driver.find_element_by_xpath(self.PIN_LIB).click()

    def text_lib_click(self):
        self.wait_for_visible(self.TEXT_LIB)
        self.driver.find_element_by_xpath(self.TEXT_LIB).click()

    def leg_lib_click(self):
        self.wait_for_visible(self.LEG_LIB)
        self.driver.find_element_by_xpath(self.LEG_LIB).click()

    def zone_lib_click(self):
        self.wait_for_visible(self.ZONE_LIB)
        self.driver.find_element_by_xpath(self.ZONE_LIB).click()

    def group_lib_click(self):
        self.wait_for_visible(self.GROUP_LIB)
        self.driver.find_element_by_xpath(self.GROUP_LIB).click()

    def control_lib_click(self):
        self.wait_for_visible(self.CONTROL_LIB)
        self.driver.find_element_by_xpath(self.CONTROL_LIB).click()


