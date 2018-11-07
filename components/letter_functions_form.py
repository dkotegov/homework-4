import selenium
from selenium.common.exceptions import WebDriverException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from components.base_form import BaseForm

class LetterFunctionsForm(BaseForm):
    IMPORTANT_MARK = '//div[class = "compose-app__widgets" ]/div[0]/div/div'

    NOTIFICATION_MARK = '//div[class = "compose-app__widgets" ]/div[1]/div/div'

    REMINDER_MARK = '//div[class = "compose-app__widgets" ]/div[2]/div/div'
    REMINDER_MARK_OHOUR = '//div[class = "compose-app__widgets" ]/div' \
                          '[2]/div/div/div/div/div[class="c0126"]/div' \
                          '/div/div/div[class="c0116"]/div[0]'
    REMINDER_MARK_THOUR = '//div[class = "compose-app__widgets" ]/div[2]' \
                          '/div/div/div/div/div[class="c0126"]/div/div/' \
                          'div/div[class="c0116"]/div[1]'
    REMINDER_MARK_ODAY = '//div[class = "compose-app__widgets" ]/div[2]' \
                         '/div/div/div/div/div[class="c0126"]/div/div/' \
                         'div/div[class="c0116"]/div[2]'
    REMINDER_MARK_TDAY = '//div[class = "compose-app__widgets" ]/div[2]' \
                         '/div/div/div/div/div[class="c0126"]/div/div/' \
                         'div/div[class="c0116"]/div[3]'
    REMINDER_MARK_FDAY = '//div[class = "compose-app__widgets" ]/div[2]' \
                         '/div/div/div/div/div[class="c0126"]/div/div/' \
                         'div/div[class="c0164"]/div[4]'

    DELAYED_MARK = '//div[class = "compose-app__widgets" ]/div[3]/div/div'

    FIRST_LETTER = '//div[class = "dataset_items"]/a[0]'

    FIRST_LETTER_IMPORTANT = '//div[class = "dataset_items"]/a[0]/div[class = "llc__content"]/div[class="llc__item_bage"]/div[class="letter-category_important"]'

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
    def click_on_reminder2_mark(self):
        element = self.driver.find_element_by_xpath(self.DELAYED_MARK)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Проверка важного письма
    def check_important_letter(self):
        element = self.driver.find_element_by_xpath(self.FIRST_LETTER_IMPORTANT)
        if element:
            return True
        else:
            return False