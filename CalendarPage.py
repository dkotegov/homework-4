from utils import Utils

from selenium import webdriver
from selenium.webdriver import ActionChains

class CalendarPage(Utils):
    CALENDAR_URL = 'https://m.calendar.mail.ru/calendar/new/'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.CALENDAR_URL)
        self.update_button = 'div.header-menu-item.header-menu-item__sidebutton.header-menu-item__ok'
        self.login_buton = '.calendar-create-item.panel-item.panel-item__marked'
        self.click_script = 'arguments[0].click();'
        self.close_sidebar_button = 'div.header-menu-item.header-menu-item__sidebutton.header-menu-item__forward'
        self.name_input = 'input.panel-input__white.calendar-summary-input'
        self.colors_button = 'div.panel-item.calendar-color-chooser.panel-item__last'
        self.colors = 'div.panel-item.panel-item__withcols.color-item'
        self.calendar_names = '.panel-content.panel-content__dark:not(.settings-panel)'
        self.options = 'div.panel-item-text.panel-item-text__nowrap'
        self.first_calendar_name = self.calendar_names + ' .panel-item:first-child'
        self.edit_button = 'div.calendars-edit.panel-item.panel-item__marked.panel-item__last'
        self.delete_icon = '.panel-content.panel-content__dark .panel-item:first-child .icn__calendar.icn__calendar-delete'
        self.delete_button = 'div.button.button-delete.button__big'
        self.settings = '.panel-content.panel-content__dark .panel-item:first-child .icn__calendar.icn__calendar-settings'
        self.close_button = 'div.header-menu-item.header-menu-item__sidebutton.header-menu-item__close'

    def click_btn_update_forms(self):
        elem = self.wait_renderbtn(self.update_button)
        elem.click()

    def in_calendar_list(self, calendar):
        self.driver.refresh()
        self.open_sidebar()
        calendars = self.check_calendar_names()
        return (calendar.encode('ascii', 'ignore') in calendars)

    def close_sidebar(self):
        elem = self.wait_renderbtn(self.close_sidebar_button)
        elem.click()

    def enter_calendar_name(self, name):
        elem = self.wait_renderbtn(self.name_input)
        elem.send_keys(name)

    def choose_calendar_color(self):
        colors = self.wait_renderbtn(self.colors_button)
        colors.click()

        number_of_color_in_que = 2
        child = ':nth-child(%s)' % (number_of_color_in_que)
        elem = self.wait_renderbtn(self.colors + child)
        elem.click()

    def check_calendar_names(self):
        self.driver.refresh()
        self.open_sidebar()

        elem = self.wait_renderbtn(self.calendar_names)
        options = [(x.text) for x in elem.find_elements_by_css_selector(self.options)]
        return options

    def check_last_calendar_name(self):
        self.wait_renderbtn(self.calendar_names)
        self.wait_invisible(self.first_calendar_name)
        elem = self.wait_renderbtn(self.first_calendar_name)

        return (elem.text)
    
    def open_addNewCalendar(self):
        login_but = self.wait_renderbtn('.calendar-create-item.panel-item.panel-item__marked')
        self.driver.execute_script("arguments[0].click();", login_but)
        element = self.wait_renderbtn('.calendar-create-item.panel-item.panel-item__marked')
        # element.click()
        ActionChains(self.driver).move_to_element(element ).click(element).perform()

    # Редактирование календаря
    def open_edit_calendars(self):
        elem = self.wait_presence_located(self.edit_button)
        elem = self.wait_invisible(self.edit_button)

        webdriver.ActionChains(self.driver).move_to_element(elem).click(elem).perform()

    def delete_last_calendar(self):
        self.wait_presence_located(self.delete_icon).click()
        self.wait_presence_located(self.delete_button).click()

    def edit_last_calendar(self):
        elem = self.wait_renderbtn(self.settings)
        elem.click()

    def add_calendar_rubbish(self):
        elem = self.wait_renderbtn(self.name_input)
        elem.send_keys("addRubbish")

    def close_edit_window(self):
        self.wait_renderbtn(self.close_button).click()
