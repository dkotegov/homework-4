# -*- coding: utf-8 -*-

from component import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys


class Searchbar(Component):
    BASE = '//div[@class="search-panel__column"]'
    BASE_ACTIVE = '//div[@class="search-panel__column search-panel__column_active"]'
    ICON_BASE = '//div[@class="search-panel-recent search-panel-recent_recent search-panel-recent_date"]'

    ICON_UNREAD = '//div[@class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_unread"]'
    ICON_FLAGGED = '//div[@class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_flagged"]'
    ICON_ATTACH = '//div[@class="search-panel-recent-item search-panel-recent-item_flag search-panel-recent-item_flag_attach"]'
    ICON_ORDERS = '//div[@class="search-panel-recent-item search-panel-recent-item_transaction search-panel-recent-item_transaction_order"]'
    ICON_FINANCE = '//div[@class="search-panel-recent-item search-panel-recent-item_transaction search-panel-recent-item_transaction_finance"]'
    ICON_REGISTRATION = '//div[@class="search-panel-recent-item search-panel-recent-item_transaction search-panel-recent-item_transaction_registration"]'
    ICON_TRAVEL = '//div[@class="search-panel-recent-item search-panel-recent-item_transaction search-panel-recent-item_transaction_travel"]'
    ICON_EVENT = '//div[@class="search-panel-recent-item search-panel-recent-item_transaction search-panel-recent-item_transaction_event"]'
    ICON_FEES = '//div[@class="search-panel-recent-item search-panel-recent-item_transaction search-panel-recent-item_transaction_fees"]'
    ICON_DATE = '//div[@class="search-panel-recent-item search-panel-recent-item_button"]'

    CALENDAR_BASE = '//div[@class="form__calendar"]'
    CALENDAR_BUTTON = CALENDAR_BASE+'//a[@id="{}"]'
    CALENDAR_PM_BUTTON = CALENDAR_BASE+'//a[@class="form__calendar__link"][@data-lapse="{}"]'
    CALENDAR_PM_BUTTON_SELECTED = CALENDAR_BASE+'//a[@class="form__calendar__link form__calendar__link_selected"][@data-lapse="{}"]'
    CALENDAR_OPERAND = BASE_ACTIVE+'//input[@class="js-input js-date b-operand__date-input"]'

    FOLDERS_ACTIVATE = '//span[@class="button2 button2_has-ico button2_folder button2_pure button2_square"]'
    FOLDERS_BASE = '//div[@class="nav-folders"]'
    FOLDER_BUTTON = FOLDERS_BASE+'//a[@class="nav__item nav__item_shortcut"][@title="{}"]'

    LETTERS = '//div[@class="llc__avatar"]'

    def waitForVisible(self):
        WebDriverWait(self.driver, 30, 1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.BASE))
        )

    def waitForVisibleAfterReload(self):
        WebDriverWait(self.driver, 30, 1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.BASE_ACTIVE))
        )

    def make_search(self, search_key):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.BASE))
        ).click()
        actions = ActionChains(self.driver)
        actions.send_keys(search_key)
        actions.send_keys(Keys.RETURN)
        actions.perform()

    def search_with_icon(self, icon_name):
        time.sleep(1)
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.BASE_ACTIVE))
        ).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, icon_name))
        ).click()

    def search_by_date(self, date):
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.BASE))
        ).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.ICON_DATE))
        ).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.CALENDAR_BASE))
        )
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.CALENDAR_BUTTON.format(date)))
        ).click()

    def search_by_date_pm(self, date, interval):
        #кликнуть по поиску
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.BASE))
        ).click()
        #кликнуть по "дата"
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.ICON_DATE))
        ).click()
        #Кликнуть по нужной дате
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.CALENDAR_BUTTON.format(date)))
        ).click()
        #кликнуть по оператору
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.CALENDAR_OPERAND))
        ).click()
        #кликнуть по нужной плюс-минус кнопке
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.CALENDAR_PM_BUTTON.format(interval)))
        ).click()

    def change_pm(self, interval):
        # кликнуть по оператору
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.CALENDAR_OPERAND))
        ).click()
        # кликнуть по нужной плюс-минус кнопке
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.CALENDAR_PM_BUTTON_SELECTED.format(interval)))
        ).click()


    def search_in_folder(self, folder_name):
        #кликнуть по строке поиска
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.BASE_ACTIVE))
        ).click()
        #кликнуть по "папка"
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.FOLDERS_ACTIVATE))
        ).click()
        #кликнуть по
        WebDriverWait(self.driver, 30, 0.1).until(
            ec.element_to_be_clickable(
                (By.XPATH, self.FOLDER_BUTTON.format(folder_name)))
        ).click()

    def has_letters(self):
        time.sleep(2)
        try:
            elems = WebDriverWait(self.driver, 30, 0.1).until(
                lambda d: d.find_elements_by_xpath(self.LETTERS)
            )
            return len(elems)
        except:
            return 0