from src.components.base_element import BaseElement


class CreateGiftElement(BaseElement):

    XPATH_I_FRAME = '//iframe[@id="appMain_Div"]'
    XPATH_TITLE = '//span[@class="con-txt __lasco __extralarge pts_string pts_startcaption js-congrat_intro"]'

    def __init__(self, driver):
        self._driver = driver
        super(CreateGiftElement, self).__init__(driver)

    def is_exists_grid(self):
        self._driver.switch_to_frame(self.get_field_by_xpath(self.XPATH_I_FRAME))
        span_title = self.existence_of_element_by_xpath(self.XPATH_TITLE)
        self._driver.switch_to_default_content()
        return span_title
