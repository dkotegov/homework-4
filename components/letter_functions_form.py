# coding=utf-8
# coding=utf-8
# coding=utf-8
# coding=utf-8
# coding=utf-8
# coding=utf-8
import selenium
from selenium.common.exceptions import WebDriverException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from components.base_form import BaseForm

class LetterFunctionsForm(BaseForm):
    IMPORTANT_MARK = '//div[@data-qa-id = "priority" ]'

    NOTIFICATION_MARK = '[data-qa-id = "receipt" ]'

    REMINDER_MARK = '[data-qa-id = "remind" ]'
    REMINDER_MARK_OHOUR = '[data-qa-id = "remind" ] div[class="c0116"]/div[0]'
    REMINDER_MARK_THOUR = '[data-qa-id = "remind" ] div[class="c0116"]/div[1]'
    REMINDER_MARK_ODAY = '[data-qa-id = "remind" ] div[class="c0116"]/div[2]'
    REMINDER_MARK_TDAY = '[data-qa-id = "remind" ] div[class="c0116"]/div[3]'
    REMINDER_MARK_FDAY = '[data-qa-id = "remind" ] div[class="c0116"]/div[4]'

    DELAYED_MARK = '[data-qa-id = "schedule" ]'

    FIRST_LETTER = '[data-qa-id  = "letter-item:subject:Вход с нового устройства"]'
    FIRST_LETTER_IMPORTANT = '//a[@data-qa-id = "letter-item:subject:Important"]'

    # Клик на отметке важного письма
    def click_on_important_mark(self):
        element = self.driver.find_element_by_xpath(self.IMPORTANT_MARK)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на отметке письма с уведомлением
    def click_on_notification_mark(self):
        element = self.driver.find_element_by_xpath(self.NOTIFICATION_MARK)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на отметке письма с напоминанием об ответе
    def click_on_reminder_mark(self):
        element = self.driver.find_element_by_xpath(self.REMINDER_MARK)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на отметке письма с напоминанием об ответе через 2 часа
    def click_on_reminder2_mark(self):
        element = self.driver.find_element_by_xpath(self.REMINDER_MARK_THOUR)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на отметке письма с отложенным отправлением
    def click_on_delayed_mark(self):
        element = self.driver.find_element_by_xpath(self.DELAYED_MARK)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Проверка важного письма
    def check_important_letter(self):
        element = self.driver.find_element_by_xpath(self.FIRST_LETTER_IMPORTANT)
        if element:
            return True
        else:
            return False