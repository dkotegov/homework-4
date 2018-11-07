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

    # Клик на отметке важного письма
    def important_mark_klick(self):
        element = self.driver.find_element_by_xpath(self.IMPORTANT_MARK)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на отметке письма с уведомлением
    def notification_mark_klick(self):
        element = self.driver.find_element_by_xpath(self.NOTIFICATION_MARK)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на отметке письма с напоминанием об ответе
    def reminder_mark_klick(self):
        element = self.driver.find_element_by_xpath(self.REMINDER_MARK)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на отметке письма с напоминанием об ответе через 2 часа
    def reminder2_mark_klick(self):
        element = self.driver.find_element_by_xpath(self.REMINDER_MARK_THOUR)
        ActionChains(self.driver).move_to_element(element).click().perform()

    # Клик на отметке письма с отложенным отправлением
    def reminder2_mark_klick(self):
        element = self.driver.find_element_by_xpath(self.DELAYED_MARK)
        ActionChains(self.driver).move_to_element(element).click().perform()