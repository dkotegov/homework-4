# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


import urlparse
from support.waiter import ElementWaiter

class Page(object):

    BASE_URL = 'https://mail.ru/'
    PATH = ''
    
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)

class Component(object):

    def __init__(self, driver, xpath):
        self.driver = driver
        self.container = ElementWaiter.wait_by_xpath(driver = driver, locator = xpath)

class AuthPage(Page):

    @property
    def form(self):
        return AuthMail(self.driver, '//div[@id="mailbox-container"]')

class AuthMail(Component):

    LOGIN = 'mailbox:login'
    PASSWORD = 'mailbox:password'
    SUBMIT = '//input[@class="o-control"][@type="submit"][1]'

    def set_login(self, login):
        elem = self.container.find_element_by_id(self.LOGIN)
        elem.click()
        elem.clear()
        elem.send_keys(login)

    def set_password(self, pwd):
         elem = self.container.find_element_by_id(self.PASSWORD)
         elem.clear()
         elem.send_keys(pwd)

    def submit(self):
        self.container.find_element_by_xpath(self.SUBMIT).click()

class MailPage(Page):

    APP_LOADER = '//div[@id="app-loader"][contains(@style,"display: none")]'
    SETTINGS_MENU = '//div[@class="settings"]'
    SETTINGS_ROW = '//div[@class="list-item list-item_hover-support"][contains(text(), "Настройки")]'
    FOLDER_ROW = '//div[@id="b-nav_folders"]//span[contains(text(), "'
    OPEN_LETTER =  '//div[@class="b-datalist__item__subj"][contains(text(), "'
    APP_LOADER = '//div[@id="app-loader"][contains(@style,"display: none")]'
    #WRITE_LETTER = '//span[@class="compose-button__txt"][contains(text(), "Написать письмо")]'
    LETTER_PROPERTIES = '//div[@class="b-datalist__item__subj"][contains(text(), "'
    LETTER_FLAG = '")]/./../../../../div[@class="b-datalist__item__flag"]/div[@title="Снять флажок"]'
    WHICH_READ = '")]/./../../../../div[@class="b-datalist__item__status"]'
    WHICH_READ_STATUS = '//span[@class="b-datalist__item__status-read"]'
    LETTER_HEADER_SUBJECT = '//div[@class="b-letter__head__subj__text"][contains(text(), "'
    DELETE_LETTER = '//div[@data-name="remove"]'
    LOG_OUT = '//a[@id="PH_logoutLink"]'
    FOLDER_OPENED = '//div[contains(@class, "b-nav__item_active")]//span[contains(text(), "'

    def open_settings_menu(self):
        ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.APP_LOADER)
        elem = ElementWaiter.wait_clickable_by_xpath(driver = self.driver, locator = self.SETTINGS_MENU)
        elem.click()

    def open_settings_page(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.SETTINGS_ROW)
        elem.click()

    def open_folder(self, folder):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.FOLDER_ROW + folder +'")]')
        elem.click()
        ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.FOLDER_OPENED + folder + '")]')
    
    def open_msg_by_subject(self, subject):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.OPEN_LETTER + subject +'")]')
        if elem == None:
            return False
        elem.click() #TODO: check that everything still works
        return True

    def find_msg_by_subject(self, subject):
        elem = ElementWaiter.wait_by_xpath_with_delay(driver = self.driver, locator = self.OPEN_LETTER + subject +'")]', delay = 5)
        if elem == None:
            return False
        return True

    def find_msg_by_subject_with_flag(self, subject):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.LETTER_PROPERTIES + subject  + self.LETTER_FLAG)
        if elem == None:
            return False
        return True

    def find_msg_by_subject_which_read(self, subject):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.LETTER_PROPERTIES + subject + self.WHICH_READ + self.WHICH_READ_STATUS)
        if elem == None:
            return False
        return True

    def check_if_letter_is_open(self, subject):
        ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.LETTER_HEADER_SUBJECT + subject +'")]')

    def delete_letter(self):
        elem = ElementWaiter.wait_elements_by_xpath(driver = self.driver, locator = self.DELETE_LETTER)[1]
        elem.click()
        
    def log_out(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.LOG_OUT)
        elem.click()

class SettingsPage(Page):

    FILTERING_RULES = '//div[@class="b-nav__item"][7]'
    CREATE_NEW_FILTERING = '//div[@class="form__row form__row_super-narrow js-add-filter-super-narrow"]/a[@class="btn js-button"]'
    WRITE_LETTER = '//span[@class="b-toolbar__btn__text b-toolbar__btn__text_pad"][contains(text(), "Написать письмо")]'
    CHANGE_FILTER = '//i[@class="icon icon_form icon_form_change"]'
    DELETE_FILTER = '//i[@class="icon icon_form icon_form_remove_big"]'
    CONFIRM_POPUP = '//button[@class="btn btn_main confirm-ok"]'
    FILTER_LIST_HEADER = '//div[@class="b-content__head__title"][contains(text(), "Правила фильтрации")]'

    def open_filters(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.FILTERING_RULES)
        elem.click()
    
    def create_new_filter(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.CREATE_NEW_FILTERING)
        elem.click()

    def write_letter_click(self):
        elem = ElementWaiter.wait_clickable_by_xpath(driver = self.driver, locator = self.WRITE_LETTER)
        elem.click()
    
    def change_filter(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.CHANGE_FILTER)
        hov = ActionChains(self.driver).move_to_element(elem)
        hov.perform()
        elem.click()
    
    def change_filter(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.CHANGE_FILTER)
        hov = ActionChains(self.driver).move_to_element(elem)
        hov.perform()
        elem.click()

    def delelte_filter(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.DELETE_FILTER)
        hov = ActionChains(self.driver).move_to_element(elem)
        hov.perform()
        elem.click()

    def delete_filter(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.DELETE_FILTER)
        hov = ActionChains(self.driver).move_to_element(elem)
        hov.perform()
        elem.click()
        popup = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.CONFIRM_POPUP)
        popup.click()

    def delete_all_filters(self):
        elems = ElementWaiter.wait_elements_by_xpath(driver = self.driver, locator = self.DELETE_FILTER)
        for elem in elems:
            hov = ActionChains(self.driver).move_to_element(elem)
            hov.perform()
            elem.click()
            popup = ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.CONFIRM_POPUP)
            popup.click()
    
    def check_if_filter_list_exists(self):
        ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.FILTER_LIST_HEADER)


class WriteMailPage(Page):

    WRITE_MAIL_FORM = '//form[@name="Compose"]'

    @property
    def form(self):
        return WriteMailForm(self.driver, self.WRITE_MAIL_FORM)

class WriteMailForm(Component):

    ADDRESSEE = '//textarea[@tabindex="4"]'
    SUBJECT = '//input[@tabindex="7"]'
    COPIES_LINK = '//div[@class="compose__controls js-row-controls"]//label[@data-for="compose_cc"]//span[@class="compose-label__text"][contains(text(), "Копия")]'
    COPIES = '//textarea[@tabindex="5"]'
    SEND = '//span[@class="b-toolbar__btn__text"][contains(text(), "Отправить")]'
    IS_EMPTY = '//div[@class="is-compose-empty_in"]//button[@class="btn btn_stylish btn_main confirm-ok"][@type="submit"]'
    WAS_SENT = '//div[@class="b-compose__sent"]'

    def setAddressee(self, mail):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.ADDRESSEE)
        elem.send_keys(mail.decode('utf-8'))
    
    def setSubject(self, subject):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.SUBJECT)
        elem.send_keys(subject.decode('utf-8'))

    def setCopies(self, mail):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.COPIES_LINK)
        if elem.is_displayed():
            elem.click()
        elem = ElementWaiter.wait_clickable_by_xpath(driver = self.container, locator = self.COPIES)
        elem.send_keys(mail.decode('utf-8'))

    def send(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.SEND)
        elem.click()
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.IS_EMPTY)
        elem.click()
        ElementWaiter.wait_by_xpath(driver = self.driver, locator = self.WAS_SENT)

class CreateFilterPage(Page):

    NEW_FILTER_FORM = '//form[@id="settings-form-edit-filter"]'

    @property
    def form(self):
        return NewFilterForm(self.driver, self.NEW_FILTER_FORM)

class NewFilterForm(Component):
    FORM_CONTAINS = '//a[@class="filters__dropdown__link js-link"][1]'
    CHANGE_CONDITION_OPEN = '//a[@class="filters__dropdown__link js-link"]'
    SET_RILE = '//a[@class="form__dropdown__item"]'
    CHANGE_VALUE_EFFECT = '//a[@class="pseudo-link js-link"]'
    CHANGE_CONDITION_VALUE = '//textarea[@data-base-name="Condition"]'
    ADD_CONDITION = '//button[@class="btn js-add-condition"]'
    SWITCH_INTERACTION_CONDITIONS = '//a[@class="pseudo-link js-link"][contains(text(),"если выполнено одно из условий") or contains(text(),"если выполнены все условия")]'
    MOVE_TO_CHECKBOX = '//input[@class="form__checkbox__checkbox js-action-moveto"][@value="moveto"]'
    MOVE_TO_FOLDER = '//div[@class="dropdown form__row__subwidget_inline form__select form__select_medium form__select_custom-dropdown form__row__shift form__row__shift_inline"]//div[@class="form__select__box form__select__box_static"]'
    CHANGE_FOLDER_LIST = '//div[@class="dropdown form__row__subwidget_inline form__select form__select_medium form__select_custom-dropdown form__row__shift form__row__shift_inline dropdown_expanded"]'
    CHANGE_FOLDER = '//label[@data-name="'
    MARK_AS_READ_CHECKBOX = '//input[@class="form__checkbox__checkbox js-action-read"][@name="Actions_read"]'
    MARK_ACTION_FLAG_CHECKBOX = '//input[@class="form__checkbox__checkbox js-action-flag"][@name="Actions_flag"]'
    DELETE_FOREVER_CHECKBOX = '//input[@class="form__checkbox__checkbox"][@name="RuleAction"][@value="delete"]'
    OTHER_ACTIONS_LINK = '//div[@class="form__row__subwidget js-otherActions"]/a'
    FORWARD_CHECKBOX = '//input[@class="form__checkbox__checkbox js-action-forward"]'
    FOWARRD_SET_MAIL = '//div[@class="form__row__subwidget_inline form__row__shift form__row__shift_inline form__row__subwidget_top js-forward-email-container"]//textarea[@class="form__field form__field_expandable js-action-forward-input"]'
    CHANGE_FORWARD_CONTEXT = '//a[@class="pseudo-link js-link"][contains(text(),"копию сообщения") or contains(text(),"уведомление")]'
    REPLY_CHECKBOX = '//input[@class="form__checkbox__checkbox js-action-reply"]'
    REPLY_WITH_MESSAGE_CHECKBOX = '//input[@class="form__checkbox__checkbox js-replywith-message"]'
    REPLY_WITH_MESSAGE_TEXTAREA = '//textarea[@class="form__field form__field_editor form__field_wide"]'
    REPLY_NOT_FOUND_CHECKBOX = '//input[@class="form__checkbox__checkbox"][@name="ReplyWith"][@value="notfound"]'
    CONTINUE_CHECKBOX = '//input[@class="form__checkbox__checkbox js-continue-checkbox"]'
    SPAM_CHECKBOX = '//input[@class="form__checkbox__checkbox"][@name="Spam"]'
    APPLY_CHECKBOX = '//input[@class="form__checkbox__checkbox"][@name="Apply"]'
    FILTERS_FOLDERS = '//div[@class="form__select filters__folders-dropdown js-checked-dropdown"]'
    FILTERS_FOLDERS_LIST = '//div[@class="form__dropdown__list filters__dropdown__menu js-menu"][not(contains(@style, "display: none"))]'
    FILTERS_FOLDER = '//label[@class="form__dropdown__item form__checkbox form__checkbox_flat js-dropdown-item"]//span[contains(text(), "'
    SAVE_FILTER_BUTTON = '//button[@class="btn btn_main btn_stylish"]//span[contains(text(), "Сохранить")]'
    POPUP_CONFIRM_PASSWORD_INPUT = '//div[@class="form__row js-password-field"]//input[@class="form__field"]'
    POPUP_CONFIRM_SUBMIT_BUTTON = '//div[@class="popup__controls"]//button//span[contains(text(), "'

    def change_condition_open(self, id):
        elem = ElementWaiter.wait_elements_by_xpath(driver = self.container, locator = self.CHANGE_CONDITION_OPEN)[id]
        elem.click()
    
    def set_condition_property(self, id, rule):
        elem = ElementWaiter.wait_elements_by_xpath(driver = self.container, locator = self.SET_RILE + '[@data-id="' + rule + '"]')[id]
        elem.click()

    def change_value_effect(self, id):
        elem = ElementWaiter.wait_elements_by_xpath(driver = self.container, locator = self.CHANGE_VALUE_EFFECT)[id]
        elem.click()

    def change_condition_value(self, id, value):
        elem = ElementWaiter.wait_elements_by_xpath(driver = self.container, locator = self.CHANGE_CONDITION_VALUE)[id]
        elem.clear()
        elem.send_keys(value)
    
    def add_condition(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.ADD_CONDITION)
        elem.click()

    def switch_interaction_conditions_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.SWITCH_INTERACTION_CONDITIONS)
        elem.click()

    def move_to_checkbox_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.MOVE_TO_CHECKBOX)
        elem.click()

    def move_to_folder_open(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.MOVE_TO_FOLDER)
        elem.click()

    def set_move_to_folder(self, folder):
        ElementWaiter.wait_by_xpath(driver = self.container, locator = self.CHANGE_FOLDER_LIST)
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.CHANGE_FOLDER + folder +'"]')
        elem.click()

    def as_read_checkbox_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.MARK_AS_READ_CHECKBOX)
        elem.click()

    def action_flag_checkbox_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.MARK_ACTION_FLAG_CHECKBOX)
        elem.click()
    
    def delete_checkbox_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.DELETE_FOREVER_CHECKBOX)
        elem.click()

    def other_actions_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.OTHER_ACTIONS_LINK)
        elem.click()

    def forward_checkbox_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.FORWARD_CHECKBOX)
        elem.click()

    def forward_set_mail(self, mail):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.FOWARRD_SET_MAIL)
        elem.send_keys(mail)

    def forward_change_contex(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.CHANGE_FORWARD_CONTEXT)
        elem.click()

    def reply_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.REPLY_CHECKBOX)
        elem.click()

    def reply_with_mesg_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.REPLY_WITH_MESSAGE_CHECKBOX)
        elem.click()

    def reply_mesg_set(self, message):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.REPLY_WITH_MESSAGE_TEXTAREA)
        elem.send_keys(message.decode('utf-8'))

    def reply_not_found_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.REPLY_NOT_FOUND_CHECKBOX)
        elem.click()

    def continue_to_filter_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.CONTINUE_CHECKBOX)
        elem.click()

    def spam_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.SPAM_CHECKBOX)
        elem.click()

    def folders_apply_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.APPLY_CHECKBOX)
        elem.click()

    def filters_folders_open(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.FILTERS_FOLDERS)
        elem.click()

    def filter_folder_click(self, folder):
        folders_list = ElementWaiter.wait_by_xpath(self.container, self.FILTERS_FOLDERS_LIST)
        elem = ElementWaiter.wait_elements_by_xpath(folders_list, self.FILTERS_FOLDER + folder + '")]')[1]
        elem.click()

    def save_filter_click(self):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.SAVE_FILTER_BUTTON)
        elem.click()

    def get_alert_message(self):
        message = ElementWaiter.wait_by_xpath(driver=self.driver, locator='//span[@class="form__top-message__text"]')
        return message.text
    
    def get_alert_pop_up_message(self):
        message = ElementWaiter.wait_by_xpath(driver=self.driver, locator='//span[@class="js-txt _js-title notify-message__title__text notify-message__title__text_error"]')
        return message.text

    def set_value_to_contains_form(self, text):
        form = ElementWaiter.wait_by_xpath(driver=self.container, locator=self.FORM_CONTAINS)
        form.click()
        form.send_keys(text)

    def confirm_form_set_password(self, value):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, locator = self.POPUP_CONFIRM_PASSWORD_INPUT)
        elem.click()
        elem.send_keys(value)

    def confirm_form_submit_password(self, buttonText):
        elem = ElementWaiter.wait_by_xpath(driver = self.container, 
            locator = self.POPUP_CONFIRM_SUBMIT_BUTTON + buttonText + '")]')
        elem.click()
