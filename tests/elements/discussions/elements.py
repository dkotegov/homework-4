from selenium.webdriver.common.by import By
from tests.elements.base import BaseElement


class Discussions(BaseElement):
    DISCUSSION_BUTTON = (By.ID, 'hook_ToolbarIconDiscussions_ToolbarDiscussions')
    FRIENDS_DISC = (By.ID, 'd-f-tab-fF')
    FRIENDS_SELECTOR = (By.CLASS_NAME, 'disc-i')
    COMMENT_OWNER = (By.CLASS_NAME, 'd_comment_owner')
    PUPMENU = (By.CLASS_NAME, 'gwt-shortcutMenu-img-w')
    USERCARD = (By.XPATH, '//*[@id="topPanelPopup_d"]/div[3]/table/tbody/tr/td/div/div')
    DOWNBUTTON = (By.XPATH, '/html/body/div[7]/div[9]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[4]')
    DISCCHAT = (By.CSS_SELECTOR, '.mdialog_chat_conversation_cnt_w')
    SCROLLTO = (By.XPATH,
                '/html/body/div[7]/div[9]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div['
                '3]/div[2]/div[2]/div[1]/span')
    SCROLLHEAD = (By.CLASS_NAME, 'dsub_head_sub_show')
    COMMENTBODY = (By.CSS_SELECTOR, '#d-id-cmnt-1511875975623--6929-rp > div:nth-child(2)')
    CLASSPANEL = (By.CSS_SELECTOR, '#d-id-cmnt-1511875975623--6929-rp > div:nth-child(3)')
    WARNPANEL = (By.CSS_SELECTOR, '#d-id-cmnt-1511875975623--6929-spam')
    TIMEPANEL = (
    By.CSS_SELECTOR, '#d-id-cmnt-1511875975623--6929-rp > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)')
