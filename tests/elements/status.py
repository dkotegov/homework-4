from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class Status(BaseElement):
    STATUS_EDIT = (By.XPATH, '//*[@id="posting_form_text_field"]')
    PUBLISH = (By.XPATH, '//*[@class="posting-form"]//*[@class="form-actions"]//*[@class="jcol-r"]//*[@class="button-pro"]')
    SHOW_EDIT = (By.XPATH, '//*[@class="posting-form_itx_w"]//*[@class="posting-form_itx_dec itx_w"]//*[@class="input_placeholder"]')
    IN_STATUS_CHBX = (By.XPATH,'//*[@class="posting-form"]//*[@class="form-actions"]//*[@class="jcol-r"]//*[@class="posting-form_ac-status"]//*[@class="irc"]')
    COMMENT = (By.XPATH,'//*[@id="hook_Block_MiddleColumnTopCard_StatusNew"]//*[@class="media_feed_status show-on-hover"]//*[@class="mst mst__current __has-widgets"]/div[3]/div/ul/li[1]/div/a/span[2]')