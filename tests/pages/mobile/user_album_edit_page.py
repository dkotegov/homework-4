import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.mobile.page import Page, Component
from tests.utils.waits import ElementsCountChanged, wait_until_url_changes


class UserAlbumEditPage(Page):
    PATH = '/dk?st.cmd=userAlbumEdit'

    @property
    def form(self):
        return EditForm(self.driver)

    def create_album(self, album_name='Test album #{}'.format(time.time())):
        self.open()
        create_form = self.form
        create_form.set_name(album_name)
        create_form.submit()


class EditForm(Component):
    NAME_FIELD = 'field_name'
    NAME_ERROR = 'field_name_label'
    PUBLIC_FIELD = 'field_toPublic'
    FRIENDS_FIELD = 'field_toFriend'
    BEST_FRIENDS_FIELD = 'field_toCloseFriend'
    COLLEAGUE_FIELD = 'field_toCollegue'
    SHOWS_CHECKBOXES = '//div[@data-view="collapsingCheckboxes"]/div[@class="mb3"]'
    SAVE_BUTTON = 'button_save'

    @property
    def shows_checkboxes_count(self):
        return len(self.driver.find_elements_by_xpath(self.SHOWS_CHECKBOXES))

    def set_name(self, name):
        name_field = self.driver.find_element_by_id(self.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)

    @wait_until_url_changes
    def submit(self):
        self.driver.find_element_by_name(self.SAVE_BUTTON).click()

    def shows_all(self):
        count = self.shows_checkboxes_count
        self.driver.find_element_by_id(self.PUBLIC_FIELD).click()
        WebDriverWait(self.driver, 1, 0.1).until(ElementsCountChanged((By.XPATH, self.SHOWS_CHECKBOXES), count))

    def shows_friends(self):
        count = self.shows_checkboxes_count
        self.driver.find_element_by_id(self.FRIENDS_FIELD).click()
        WebDriverWait(self.driver, 1, 0.1).until(ElementsCountChanged((By.XPATH, self.SHOWS_CHECKBOXES), count))

    def shows_best_friends(self):
        self.driver.find_element_by_id(self.BEST_FRIENDS_FIELD).click()

    def shows_colleagues(self):
        self.driver.find_element_by_id(self.COLLEAGUE_FIELD).click()

    def is_shows_best_friends(self):
        return self.driver.find_element_by_id(self.BEST_FRIENDS_FIELD).get_attribute('checked')

    def is_shows_colleagues(self):
        return self.driver.find_element_by_id(self.COLLEAGUE_FIELD).get_attribute('checked')

    def is_name_error(self):
        try:
            self.driver.find_element_by_id(self.NAME_ERROR)
            return True
        except NoSuchElementException:
            return False
