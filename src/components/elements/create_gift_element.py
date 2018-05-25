from src.components.base_element import BaseElement


class CreateGiftElement(BaseElement):

    XPATH_I_FRAME = '//iframe[@id="appMain_Div"]'
    XPATH_TITLE = '//span[@class="con-txt __lasco __extralarge pts_string pts_startcaption js-congrat_intro"]'

    XPATH_GIFT_CREATED_TITLE = '//span[@class="con-txt __lasco __xlarge pts_string pts_congrats js-final_congrat"]'

    XPATH_GIFT_SENT_I_FRAME = '//iframe[@class="modal-new_payment-frame"]'
    XPATH_GIFT_SENT_TITLE = '//div[@class="portlet_h_name_t"]'

    def __init__(self, driver):
        self._driver = driver
        super(CreateGiftElement, self).__init__(driver)

    def is_exists_grid(self):
        self._driver.switch_to_frame(self.get_field_by_xpath(self.XPATH_I_FRAME))
        span_title = self.existence_of_element_by_xpath(self.XPATH_TITLE)
        self._driver.switch_to_default_content()
        return span_title

    def if_gift_created(self):
        self._driver.switch_to_frame(self.get_field_by_xpath(self.XPATH_I_FRAME))
        span_title = self.existence_of_element_by_xpath(self.XPATH_GIFT_CREATED_TITLE)
        self._driver.switch_to_default_content()
        return span_title

    def is_gift_sent(self):
        self._driver.switch_to_frame(self.get_field_by_xpath(self.XPATH_GIFT_SENT_I_FRAME))
        title = self.existence_of_element_by_xpath(self.XPATH_GIFT_SENT_TITLE)
        self._driver.switch_to_default_content()
        return title
