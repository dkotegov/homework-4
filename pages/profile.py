import constants
from pages.default import Page
from utils import wait_for_element_by_selector, wait_for_url


class ProfilePage(Page):
    PATH = 'profile/'
    SRC = 'src'
    TITLE = '.title-wrapper__title'
    SUBSCRIPTION_BTN = '.subscription__button'
    AVATAR = '.input-wrapper__img'
    INPUT_FOR_AVATAR = '#file'
    UPLOAD_AVATAR_BTN = 'label.input-wrapper__input'
    SAVE_AVATAR_BTN = '.input-wrapper__button'

    def get_title_of_page(self):
        return wait_for_element_by_selector(self.driver, self.TITLE).text

    def click_on_subscription_btn(self):
        wait_for_element_by_selector(self.driver, self.SUBSCRIPTION_BTN).click()

    def is_umoney_url(self):
        try:
            wait_for_url(self.driver, constants.UMONEY_URL)
            return True
        except:
            return False

    def get_current_avatar(self):
        return wait_for_element_by_selector(self.driver, self.AVATAR).get_attribute(self.SRC)

    def upload_new_avatar(self, path):
        wait_for_element_by_selector(self.driver, self.UPLOAD_AVATAR_BTN)
        self.driver.find_element_by_css_selector(self.INPUT_FOR_AVATAR).send_keys(path)

    def save_avatar(self):
        wait_for_element_by_selector(self.driver, self.SAVE_AVATAR_BTN).click()
        wait_for_element_by_selector(self.driver, self.SAVE_AVATAR_BTN)

