from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class Discussion(BaseElement):
    TITLE = (By.XPATH, '//*[@class="mdialog_list_conversations custom-scrolling"]//*[@class="disc-i"]//*[@class="disc-i_cnt"]//*[@class="disc-i_cnt_group_theme"]')