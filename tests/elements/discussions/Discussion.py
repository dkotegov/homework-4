from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class Discussion(BaseElement):
    TITLE = (By.XPATH, '//*[@class="mdialog_list_conversations custom-scrolling"]//*[@class="disc-i disc-i_sel"]//*[@class="disc-i_cnt"]//*[@class="disc-i_cnt_group_theme"]')

    def get_last_comment(self):
        elms = self.driver.find_elements(By.XPATH, '//*[@class="d_comment_w d_comment_w__avatar __me show-on-hover"]')
        if elms is None:
            return None
        else:
            if len(elms) == 0:
                return None
            self.element = elms[-1].find_element(By.CSS_SELECTOR, 'div.d_comment_w_center > div.d_comment_right_w > div.d_comment_text_w > div.d_comment_text.textWrap > div')
            return self

    def get_last_comment_delete_button(self):
        elms = self.driver.find_elements(By.XPATH, '//*[@class="d_comment_w d_comment_w__avatar __me show-on-hover"]')
        if elms is None:
            return None
        else:
            if len(elms) == 0:
                return None
            self.element = elms[-1].find_element(By.CSS_SELECTOR, 'div.d_comment_w_center > div.d_comment_right_w > div.d_comment_text_w > div.d_comment_r > div.d_comment_act_w > a.d_comment_act.d_comment_act_del.d_comment_act_spam.ic10.ic10_close-g.fade-on-hover')
            return self