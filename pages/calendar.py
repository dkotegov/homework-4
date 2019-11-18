# coding=utf-8
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from default import *


class CalendarPage(Page):
    PATH = ''

    @property
    def form(self):
        return CalendarForm(self.driver)

    @property
    def tasks(self):
        return TasksForm(self.driver)

    def settings(self):
        return SettingsForm(self.driver)


class CalendarForm(Component, Page):
    EVENT_PAGE = '//div[@class="event-page"]'
    CREATE_EVENT__BUTTON = '//a[contains(@class, "button_create-event")]'
    SAVE_EVENT__BUTTON = '//a[contains(@class, "event-new__button_submit")]'
    CANCEL_EVENT__BUTTON = '//a[contains(@class, "event-new__reset")]'
    ATTENDEES___INPUT = '//div[@class="attendees-selector__textbox"]//input[@name="input"]'
    EVENT_NAME__INPUT = '//div[@class="event-new__summary event-new__row"]//input'
    DATE_END__INPUT = '//input[@name="dateEnd"]'
    DATE_FORMAT = "%d.%m.%Y"
    LOCATION__INPUT = '//div[@class="event-new__row event-new__row_location"]//input'
    DESCRIPTION__INPUT = '//div[@class="event-new__row event-new__row_description"]//textarea'

    def save_event(self):
        self.wait_for_clickable(self.SAVE_EVENT__BUTTON).click()

    def create_event(self):
        self.wait_for_clickable(self.CREATE_EVENT__BUTTON).click()

    def cancel_event(self):
        self.wait_for_clickable(self.CANCEL_EVENT__BUTTON).click()

    def set_name(self, name):
        self.wait_for_clickable(self.EVENT_NAME__INPUT).send_keys(name)

    def set_location(self, location):
        self.wait_for_clickable(self.LOCATION__INPUT).send_keys(location)

    def set_description(self, description):
        self.wait_for_clickable(self.DESCRIPTION__INPUT).send_keys(description)

    def add_attendees(self, email):
        elem = self.wait_for_element(self.ATTENDEES___INPUT)
        elem.send_keys(email)
        elem.send_keys(Keys.ENTER)

    def get_date_end(self):
        elem = self.wait_for_element(self.DATE_END__INPUT)
        dateStr = elem.get_attribute("value")
        return datetime.datetime.strptime(dateStr, self.DATE_FORMAT).date()

    def set_date_end(self, date):
        elem = self.wait_for_element(self.DATE_END__INPUT)
        self.driver.execute_script("arguments[0].setAttribute('value','" + date.strftime(self.DATE_FORMAT) + "')", elem)
        elem.click()

    SETTINGS = '//div[@data-role="popup"]'
    SETTINGS_BUTTON = '//a[@href="?action=settings"]'
    SETTINGS_SUBMIT = '//button[@data-action="submit"]'
    SETTINGS_REMINDERS_BUTTON = '//a[@data-page-link="reminders"]'
    SELECT_CALENDAR = '//select[@data-element="calendar"]'
    SELECT_CALENDAR_ELEMENT = '//option[@value="B4AADE80-1122-42EB-A010-6E7C73804192"]'
    WORKDAY_START = '//input[@name="start"]'
    WORKDAY_END = '//input[@name="end"]'
    WORKDAY_CHECKBOXES = './/span[@class="workdays__day"]'
    WORKDAY_CHECKBOX_ITEM = './/span[@data-id="%d"]'
    WORKDAY_CHECKBOX_ITEM_VALUE = './/input[@class="checkbox-input"]'
    WORKDAY_CHECKBOX_ERROR = '//span[@class="checkbox checkbox_layout_inline checkbox_top checkbox_error"]'
    REMINDERS = '//div[@class="reminders reminders_default"]'
    REMINDERS_ITEM = './/div[@class="reminders-item valign_20"]'
    REMINDERS_ITEM_CHECKBOX = './/span[@data-role="checkbox"]'
    REMINDERS_ITEM_CHECKBOX_EMAIL = './/span[@name="email"]'
    REMINDERS_SOUND = '//span[@name="disable_sound"]'
    REMINDERS_EMAIL_DIV = '//div[@class="form-param__value"]'
    REMINDERS_EMAIL_ITEM = './/div[@class="settings-notify-types-item"]'
    REMINDERS_EMAIL_ITEM_CHECKBOX = './/span[@data-role="checkbox"]'

    def settings_click(self):
        self.wait_for_element(self.SETTINGS_BUTTON)
        self.wait_for_clickable(self.SETTINGS_BUTTON)
        self.driver.find_element_by_xpath(self.SETTINGS_BUTTON).click()

    def settings_submit(self):
        self.wait_for_element(self.SETTINGS_SUBMIT)
        self.wait_for_clickable(self.SETTINGS_SUBMIT)
        self.driver.find_element_by_xpath(self.SETTINGS_SUBMIT).click()

    def change_workday_times(self):
        time_begin = '08:00'
        time_end = '15:00'
        time_format_len = 5

        self.wait_for_element(self.SETTINGS)
        settings = self.driver.find_element_by_xpath(self.SETTINGS)
        self.wait_for_clickable(self.WORKDAY_START)
        start = settings.find_element_by_xpath(self.WORKDAY_START)

        for i in range(0, time_format_len):
            start.send_keys(Keys.BACK_SPACE)

        start.send_keys(time_begin)
        self.wait_for_clickable(self.WORKDAY_END)
        end = settings.find_element_by_xpath(self.WORKDAY_END)

        for i in range(0, time_format_len):
            end.send_keys(Keys.BACK_SPACE)

        end.send_keys(time_end)

    def change_calendar(self):
        self.wait_for_element(self.SETTINGS)
        settings = self.driver.find_element_by_xpath(self.SETTINGS)
        self.wait_for_clickable(self.SELECT_CALENDAR)
        select = settings.find_element_by_xpath(self.SELECT_CALENDAR)
        select.click()

        self.wait_for_clickable(self.SELECT_CALENDAR_ELEMENT)
        select.find_element_by_xpath(self.SELECT_CALENDAR_ELEMENT).click()

    def change_to_two_workdays(self):
        self.wait_for_element(self.SETTINGS)
        settings = self.driver.find_element_by_xpath(self.SETTINGS)
        days = settings.find_elements_by_xpath(self.WORKDAY_CHECKBOXES)

        i = 1
        for item in days:
            self.wait_for_clickable(self.WORKDAY_CHECKBOX_ITEM % i)
            span = item.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM % i)
            value = span.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM_VALUE)
            if value.get_attribute('value') == 'true':
                span.click()
            i += 1

        max_workdays = 2

        i = 1
        for item in days:
            if i <= max_workdays:
                self.wait_for_clickable(self.WORKDAY_CHECKBOX_ITEM % i)
                item.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM % i).click()
                i += 1
            else:
                break

    def change_to_zero_workdays(self):
        self.wait_for_element(self.SETTINGS)
        settings = self.driver.find_element_by_xpath(self.SETTINGS)
        days = settings.find_elements_by_xpath(self.WORKDAY_CHECKBOXES)

        i = 1
        for item in days:
            self.wait_for_clickable(self.WORKDAY_CHECKBOX_ITEM % i)
            span = item.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM % i)
            value = span.find_element_by_xpath(self.WORKDAY_CHECKBOX_ITEM_VALUE)
            if value.get_attribute('value') == 'true':
                span.click()
            i += 1

    def reminders_click(self):
        self.wait_for_element(self.SETTINGS_REMINDERS_BUTTON)
        self.wait_for_clickable(self.SETTINGS_REMINDERS_BUTTON)
        self.driver.find_element_by_xpath(self.SETTINGS_REMINDERS_BUTTON).click()

    def change_to_one_reminder(self):
        self.wait_for_element(self.REMINDERS)
        reminders = self.driver.find_elements_by_xpath(self.REMINDERS_ITEM)

        for item in reminders:
            self.wait_for_clickable(self.REMINDERS_ITEM_CHECKBOX)
            span = item.find_element_by_xpath(self.REMINDERS_ITEM_CHECKBOX)
            if span.get_attribute('data-checked') == 'true' and span.get_attribute('name') != 'email':
                span.click()
            if span.get_attribute('data-checked') == 'false' and span.get_attribute('name') == 'email':
                span.click()

    def change_to_zero_reminders(self):
        self.wait_for_element(self.REMINDERS)
        reminders = self.driver.find_elements_by_xpath(self.REMINDERS_ITEM)

        for item in reminders:
            self.wait_for_clickable(self.REMINDERS_ITEM_CHECKBOX)
            span = item.find_element_by_xpath(self.REMINDERS_ITEM_CHECKBOX)
            if span.get_attribute('data-checked') == 'true':
                span.click()

    def mute_sound(self):
        self.wait_for_element(self.REMINDERS_SOUND)
        self.wait_for_clickable(self.REMINDERS_SOUND)
        sound = self.driver.find_element_by_xpath(self.REMINDERS_SOUND)
        if sound.get_attribute('data-checked') == 'false':
            sound.click()

    def change_email_reminders(self, state):
        self.wait_for_element(self.REMINDERS_EMAIL_DIV)
        reminders = self.driver.find_elements_by_xpath(self.REMINDERS_EMAIL_ITEM)

        for item in reminders:
            self.wait_for_clickable(self.REMINDERS_EMAIL_ITEM_CHECKBOX)
            span = item.find_element_by_xpath(self.REMINDERS_EMAIL_ITEM_CHECKBOX)
            if span.get_attribute('data-checked') == state:
                span.click()


class TasksForm(Component, Page):
    TASK_INPUT = '//input[@name="summary"]'
    TASK_WITH_DATE_SETTINGS_BUTTON = '//div[@title="Дополнительные параметры задачи"]'
    TASK_WITH_DATE_SUBMIT_BUTTON = '//button[@type="submit"]'

    LAST_CREATED_TASK_ITEM = '//div[@class="group__header" and text()="{}"]/..//div[@class="group__items"]/div[@class="group__item"]'
    LAST_CREATED_TASK_ITEM_SPAN = LAST_CREATED_TASK_ITEM + '/span'
    LAST_CREATED_TASK_TITLE = LAST_CREATED_TASK_ITEM + '//span[@data-role="checkbox-text"]'
    LAST_CREATED_TASK_SETTINGS_BUTTON = LAST_CREATED_TASK_ITEM + '//div[@title="Редактировать задачу"]'
    LAST_CREATED_TASK_CHECKBOX = LAST_CREATED_TASK_ITEM + '//span[contains(@class, "checkbox-control")]'
    LAST_CREATED_TASK_SAVE_SETTINGS_BUTTON = '//button[text()="Сохранить"]'

    TASK_SETTINGS_FORM = '//div[contains(@class, "todo-form_opened")]'  # "2019-11-22T00:00:00+03:00"
    TASK_SETTINGS_FORM_DATE = '//div[contains(@class, "todo-form_opened")]//td[@data-day="{}"]'

    def add_task(self):
        task_input = self.wait_for_visible(self.TASK_INPUT)
        task_input.send_keys(Keys.ENTER)
        self.wait_for_stale(self.LAST_CREATED_TASK_SETTINGS_BUTTON.format("Неразобранное"))

    def add_task_with_date(self):
        TASK_WITH_DATE_SUBMIT_BUTTON = self.TASK_WITH_DATE_SUBMIT_BUTTON.format("Неразобранное")
        self.wait_for_visible(TASK_WITH_DATE_SUBMIT_BUTTON).click()

    def execute_task(self, list_title):
        LAST_CREATED_TASK_CHECKBOX = self.LAST_CREATED_TASK_CHECKBOX.format(list_title)
        task_checkbox = self.wait_for_visible(LAST_CREATED_TASK_CHECKBOX)
        task_checkbox.click()

        LAST_CREATED_TASK_CHECKBOX = self.LAST_CREATED_TASK_CHECKBOX.format(list_title)
        self.wait_for_stale(LAST_CREATED_TASK_CHECKBOX)

    def is_task_has_title(self, list_title, task_title):
        LAST_CREATED_TASK_TITLE = self.LAST_CREATED_TASK_TITLE.format(list_title)
        return WebDriverWait(self.driver, 5, self.FREQ).until(
            EC.text_to_be_present_in_element((By.XPATH, LAST_CREATED_TASK_TITLE), task_title)
        )

    def is_last_created_task_crossed(self, list_title):
        LAST_CREATED_TASK_ITEM_SPAN = self.LAST_CREATED_TASK_ITEM_SPAN.format(list_title)
        last_added_no_date_task_title = self.wait_for_visible(LAST_CREATED_TASK_ITEM_SPAN)
        is_checked = 'checkbox_checked' in last_added_no_date_task_title.get_attribute('class')
        return is_checked

    def open_last_created_task_settings(self, list_title):
        LAST_CREATED_TASK_SETTINGS_BUTTON = self.LAST_CREATED_TASK_SETTINGS_BUTTON.format(list_title)
        webdriver.ActionChains(self.driver).move_to_element(self.wait_for(LAST_CREATED_TASK_SETTINGS_BUTTON)).perform()
        webdriver.ActionChains(self.driver).click(self.wait_for_visible(LAST_CREATED_TASK_SETTINGS_BUTTON)).perform()

    def open_task_settings(self):
        self.wait_for_visible(self.TASK_WITH_DATE_SETTINGS_BUTTON).click()

    def set_task_date(self, date):
        TASK_SETTINGS_FORM_DATE = self.TASK_SETTINGS_FORM_DATE.format(date)
        self.wait_for_visible(self.TASK_SETTINGS_FORM)
        self.wait_for_visible(TASK_SETTINGS_FORM_DATE).click()

    def set_task_title(self, task_topic):
        self.wait_for_visible(self.TASK_INPUT).send_keys(task_topic)

    def save_task_settings(self):
        save_button = WebDriverWait(self.driver, 20, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.LAST_CREATED_TASK_SAVE_SETTINGS_BUTTON)))
        save_button.click()


class SettingsForm(Component, Page):
    SETTINGS_BUTTON = '//a[text()="Настройки"]'
    NOTIFICATIONS_BUTTON = '//a[text()="Уведомления"]'
    ADD_PHONE_NUMBER_BUTTON = '//a[text()="Добавить"]'

    def open_settings(self):
        submit = self.wait_for_visible(self.SETTINGS_BUTTON)
        submit.click()

    def open_notifications_tab(self):
        submit = self.wait_for_visible(self.NOTIFICATIONS_BUTTON)
        submit.click()

    def add_phone_number(self):
        submit = self.wait_for_visible(self.ADD_PHONE_NUMBER_BUTTON)
        submit.click()


def open_next_tab(driver):
    tabs_amount = len(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
