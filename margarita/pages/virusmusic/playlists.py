from selenium.webdriver.common.keys import Keys

from margarita.pages.default import Page
from margarita.utils import wait_for_element_by_selector, wait_for_element_to_be_clickable_by_selector

class PlaylistPage(Page):
    PATH = '/playlist/'
    DELETE = '#playlist-delete-button'
    NAME = 'div.m-big-name'
    EDIT = '#playlist-edit-button'
    NAME_INPUT = 'input.m-big-name'
    IMAGE_INPUT = 'input#image-upload'
    SHARE = 'button.m-button-share'
    COPY = '#playlist-share-button'
    VK_SHARE = '#vk-share'

    def __init__(self, driver, id):
        super().__init__(driver)
        self.PATH += id

    def change_name(self, name):
        self.open()
        self.edit()
        nameInput = wait_for_element_to_be_clickable_by_selector(self.driver, self.NAME_INPUT)
        nameInput.clear()
        nameInput.send_keys(name + Keys.ENTER)

    def get_name(self):
        return wait_for_element_by_selector(self.driver, self.NAME).get_attribute('innerText')

    def load_image(self, path):
        self.open()
        self.edit()
        self.driver.find_element_by_css_selector(self.IMAGE_INPUT).send_keys(path)

    def copy_link(self):
        self.open()
        self.share()
        copy = wait_for_element_by_selector(self.driver, self.COPY)
        copy.click()

    def vk_share(self):
        self.open()
        self.share()
        vkShare = wait_for_element_by_selector(self.driver, self.VK_SHARE)
        vkShare.click()

    def delete(self):
        self.open()
        delete = wait_for_element_by_selector(self.driver, self.DELETE)
        delete.click()

    def delete_track(self, track_id):
        self.open()
