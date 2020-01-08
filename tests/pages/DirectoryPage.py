from BasicPage import BasicPage
from MainPage import MainPage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class DirectoryPage(MainPage):
    ARCHIVE_URL = 'https://e.mail.ru/archive'
    create_message = '.compose-button__wrapper'
    click_flag = '.ll-fs'
    archive_button = "div.portal-menu-element_archive"
    # img:nth-of-type(2n)
    select_letter_button = 'a.llc:first-of-type .ll-rs'

    

    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        self.driver.get(self.LOGIN_URL)

    def move_to_archive(self):
        elem = self.wait_render(self.archive_button)
        elem.click()
        self.wait_show_notification()
        self.hide_notification()

    def click_archive_button(self):
        elem = self.wait_render(self.nav_archive_button)
        elem.click()
        self.wait_redirect(self.ARCHIVE_URL)
        

    def select_letter(self):
        elem = self.wait_render(self.select_letter_button)
        elem.click()


