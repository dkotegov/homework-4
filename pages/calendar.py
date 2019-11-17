# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.common import Page, Component


class CalendarPage(Page):
    @property
    def tasks(self):
        return TasksForm(self.driver)

    def settings(self):
        return SettingsForm(self.driver)


class TasksForm(Component):
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


class SettingsForm(Component):
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