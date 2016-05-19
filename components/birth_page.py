# -*- coding: utf-8 -*-
from components.component import Component

class BirthHeaderBlock(Component):
    CALENDAR = 'dropdown_calendar'
    DROPDOWN_BOX = 'dropdown__box'
    CALENDAR_MONTH = 'calendar__month'
    CALENDAR_NEXT = 'js-calendar_next'
    CALENDAR_PREVIOUS = 'js-calendar_prev'
    CALENDAR_DAY_SELECTOR = '//a[@href="/person/birthday/?day=0{0}-0{1}"]'
    USER_IMAGE_HREF = 'itemperson__img'
    PARENT_NODE = '..'
    ACTIVE_CALENDAR_DAY = 'calendar__cell calendar__cell_enabled calendar__cell_active'
    CLASS_ATTR = 'class'

    @property
    def calendar(self):
        return self.driver.find_element_by_class_name(self.CALENDAR)

    @property
    def today_month(self):
        return self.driver.find_element_by_class_name(self.CALENDAR_MONTH).text

    def click_calendar_dropdown_button(self):
        return self.calendar.click()

    def click_next_month_button(self):
        return self.driver.find_element_by_class_name(self.CALENDAR_NEXT).click()

    def click_previous_month_button(self):
        return self.driver.find_element_by_class_name(self.CALENDAR_PREVIOUS).click()

    def calendar_dropdown_box_visible(self):
        return self.driver.find_element_by_class_name(self.DROPDOWN_BOX).is_displayed()

    def click_day(self, day, month):
        return self.driver.find_element_by_xpath(self.CALENDAR_DAY_SELECTOR.format(month, day)).click()

    def day_is_active(self, day, month):
        href = self.driver.find_element_by_xpath(self.CALENDAR_DAY_SELECTOR.format(month, day))
        return href.find_element_by_xpath(self.PARENT_NODE).get_attribute(self.CLASS_ATTR) == self.ACTIVE_CALENDAR_DAY

class BirthListBlock(Component):
    USER_IMAGE_HREF = 'itemperson__img'

    def click_first_item(self):
        return self.driver.find_element_by_class_name(self.USER_IMAGE_HREF).click()

    def get_item_info(self):
        info = self.driver.find_element_by_tag_name('time').text
        return info.split()[:2]
