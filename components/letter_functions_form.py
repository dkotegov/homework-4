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

    TEMPLATE_MARK = '//div[@class="container--m44Tk relative--3LYxp"]/button[@data-test-id = "button" ]'
    TEMPLATE_MARK_SAVE = '//div[@class ="control--3U0pa" ]'
    TEMPLATE_FIRST = '//div[@class="container--2hzoN"]/div'

    #Получение первого шаблона из списка
    def get_first_template(self):
            elem = WebDriverWait(self.driver, 1) \
                .until(lambda driver: driver.find_elements_by_xpath(self.TEMPLATE_FIRST)[0])
            return elem.text

    # Выведение списка шаблонов
    def click_template_mark(self):
            elem = WebDriverWait(self.driver, 1) \
                .until(lambda driver: driver.find_element_by_xpath(self.TEMPLATE_MARK))
            ActionChains(self.driver).move_to_element(elem).click().perform()

    # Сохранение шаблона
    def click_save_template(self):
        element = WebDriverWait(self.driver, 1) \
            .until(lambda driver: driver.find_element_by_xpath(self.TEMPLATE_MARK_SAVE))
        ActionChains(self.driver).move_to_element(element).click().perform()

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

    # Проверка на наличие письма по заголовку
    def check_letter_by_subj(self, subject):
        element = self.driver.find_element_by_xpath(self.FIRST_LETTER_IMPORTANT.format(subject))
        if element:
            return True
        else:
            return False

        # letter-item:subject:ImportantS