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

    NOTIFICATION_MARK = '//div[@data-qa-id = "receipt" ]'

    REMINDER_MARK = '//div[@data-qa-id = "remind" ]'
    REMINDER_MARK_OHOUR = '//div[@data-qa-id = "remind" ] div[class="c0116"]/div[0]'
    REMINDER_MARK_THOUR = '//div[@data-qa-id = "remind" ] div[class="c0116"]/div[1]'
    REMINDER_MARK_ODAY = '//div[@data-qa-id = "remind" ] div[class="c0116"]/div[2]'
    REMINDER_MARK_TDAY = '//div[@data-qa-id = "remind" ] div[class="c0116"]/div[3]'
    REMINDER_MARK_FDAY = '//div[@data-qa-id = "remind" ] div[class="c0116"]/div[4]'

    DELAYED_MARK = '//div[@data-qa-id = "schedule" ]'

    FIRST_LETTER = '//div[@data-qa-id  = "letter-item:subject:Вход с нового устройства"]'
    FIRST_LETTER_IMPORTANT = '//a[@data-qa-id = "letter-item:subject:{}"]'

    TEMPLATE_MARK = '//div[@data-test-id = "button" ]'
    TEMPLATE_MARK_SAVE = '//div[@class ="checked--1gJVx" ]'


    def click_template_mark(self):
        try:
            elem = WebDriverWait(self.driver, 1) \
                .until(lambda driver: driver.find_element_by_xpath(self.TEMPLATE_MARK))
            element = WebDriverWait(self.driver, 1) \
                .until(lambda driver: driver.find_element_by_xpath(self.TEMPLATE_MARK_SAVE))
            ActionChains(self.driver).move_to_element(elem).click().perform()
            ActionChains(self.driver).move_to_element(element).click().perform()
            print 'destination email is set'
        except WebDriverException:
            print 'destination input not found'


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
    def check_letter_by_subj(self, subject):
        element = self.driver.find_element_by_xpath(self.FIRST_LETTER_IMPORTANT.format(subject))
        if element:
            return True
        else:
            return False

        # letter-item:subject:ImportantS