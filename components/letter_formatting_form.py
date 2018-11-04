# coding=utf-8
import selenium
from selenium.common.exceptions import WebDriverException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from components.base_form import BaseForm


class LetterFormattingForm(BaseForm):
    # text formatting elements
    MESSAGE_FIELD = '//div[@role="textbox"]/div/div'
    BOLD_BUTTON = '//button[@title="Жирный текст"]'
    ITALIC_BUTTON = '//button[@title="Наклонный текст"]'
    UNDERLINED_BUTTON = '//button[@title="Подчёркнутый текст"]'
    STRIKETHROUGH_BUTTON = '//button[@title="Зачёркнутый текст"]'

    TEXT_COLOR_BUTTON = '//button[@title="Цвет текста"]'
    COLOR_VALUE = '//div[@style="background-color: rgb(202, 242, 245);"]'

    BACKGROUND_COLOR_BUTTON = '//button[@title="Цвет фона"]'
    BACKGROUND_COLOR_VALUE = '//div[@class="cell--3K4W6"]/div[6]/div[2]/div/div[4]'
    FORMATTER_TEXT = '//div[@role="textbox"]/div/div/span'

    FONT_BUTTON = '//button[@title="Шрифт"]'
    FONT_VALUE = '//div[@class="cell--3K4W6"]/div[7]/div[2]/div/div[2]'

    TEXT_ALIGN = '//button[@title="Выравнивание"]'
    TEXT_ALIGN_VALUE_LEFT = '//div[@class="cell--3K4W6"]/div[8]/div[2]/div/div[3]'
    TEXT_ALIGN_VALUE_RIGHT = '//div[@class="cell--3K4W6"]/div[8]/div[2]/div/div[3]'

    TEXT_MARGIN = '//button[@title="Отступ"]'
    TEXT_MARGIN_VALUE = '//div[@class="cell--3K4W6"]/div[9]/div[2]/div/div[2]'

    # Жирный шрифт
    def click_on_bold_icon(self):
        self.driver.find_element_by_xpath(self.BOLD_BUTTON).click()

    # Курсивый шрифт
    def click_on_italic_icon(self):
        self.driver.find_element_by_xpath(self.ITALIC_BUTTON).click()

    # Подчеркнутый текст
    def click_on_underlined_icon(self):
        self.driver.find_element_by_xpath(self.UNDERLINED_BUTTON).click()

    # Зачеркнутый текст
    def click_on_strikethrough_icon(self):
        self.driver.find_element_by_xpath(self.STRIKETHROUGH_BUTTON).click()

    # Цвет текста
    def click_on_color_text_icon(self):
        self.driver.find_element_by_xpath(self.TEXT_COLOR_BUTTON).click()

    # Значение цвета
    def click_on_color_value(self):
        elem = self.driver.find_element_by_xpath(self.COLOR_VALUE)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Цвет фона
    def click_on_background_color_icon(self):
        self.driver.find_element_by_xpath(self.BACKGROUND_COLOR_BUTTON).click()

    # Значение цвета фона
    def click_on_background_color_value(self):
        elem = self.driver.find_element_by_xpath(self.BACKGROUND_COLOR_VALUE)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Размер шрифта
    def click_on_font_icon(self):
        elem = self.driver.find_element_by_xpath(self.FONT_BUTTON)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Значение размера шрифта
    def click_on_font_value(self):
        elem = self.driver.find_element_by_xpath(self.FONT_VALUE)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Вырванивание текста
    def click_on_text_align_icon(self):
        elem = self.driver.find_element_by_xpath(self.TEXT_ALIGN)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Значение выравнивания текста
    def click_on_text_align_value_icon(self):
        elem = self.driver.find_element_by_xpath(self.TEXT_ALIGN_VALUE_RIGHT)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Отступ текста
    def click_on_text_margin_icon(self):
        elem = self.driver.find_element_by_xpath(self.TEXT_MARGIN)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Значение отступа
    def click_on_text_margin_value_icon(self):
        elem = self.driver.find_element_by_xpath(self.TEXT_MARGIN_VALUE)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Ввод текста
    def write_some_text(self, text):
        element = self.driver.find_element_by_xpath(self.MESSAGE_FIELD)
        ActionChains(self.driver).move_to_element(element).click().perform()
        ActionChains(self.driver).key_down(text).perform()

    # Получение innerHTML элемента
    def get_text(self):
        return self.driver.find_element_by_xpath(self.MESSAGE_FIELD).get_attribute('innerHTML')

    # Получение цвета элемента
    def get_text_color(self):
        return self.driver.find_element_by_xpath(self.FORMATTER_TEXT) \
            .value_of_css_property("color")

    # Получение цвета фона элемента
    def get_background_color(self):
        return self.driver.find_element_by_xpath(self.FORMATTER_TEXT).value_of_css_property("background-color")

    # Получение свойства font-size
    def get_size_of_text(self):
        return self.driver.find_element_by_xpath(self.FORMATTER_TEXT).value_of_css_property("font-size")

    # Получение свойства line-height
    def get_line_height_of_text(self):
        return self.driver.find_element_by_xpath(self.FORMATTER_TEXT).value_of_css_property("line-height")

    # Получение свойства text-align
    def get_align_of_text(self):
        return self.driver.find_element_by_xpath(self.MESSAGE_FIELD).value_of_css_property("text-align")

    # Получение свойства margin
    def get_margin_of_text(self):
        return self.driver.find_element_by_xpath(self.MESSAGE_FIELD).value_of_css_property("margin-left")
        # return self.driver.find_element_by_xpath(self.MESSAGE_FIELD).get_attribute('innerHTML')

    # Выделение текста
    def text_selection(self):
        self.driver.find_element_by_xpath(self.MESSAGE_FIELD).click()
        ActionChains(self.driver).key_down(Keys.LEFT_CONTROL).perform()
        ActionChains(self.driver).key_down(Keys.LEFT_SHIFT).perform()
        ActionChains(self.driver).key_down(Keys.LEFT).perform()
        ActionChains(self.driver).key_up(Keys.LEFT).perform()
        ActionChains(self.driver).key_up(Keys.LEFT_SHIFT).perform()
        ActionChains(self.driver).key_up(Keys.LEFT_CONTROL).perform()

    # Очищение поля ввода
    def clear_field(self):
        self.text_selection()
        ActionChains(self.driver).key_down(Keys.DELETE).perform()

    # Очищение поля + сброс выравнивания
    def full_clear_field(self):
        mess_field = self.driver.find_element_by_xpath(self.MESSAGE_FIELD)
        ActionChains(self.driver).move_to_element(mess_field).double_click().perform()

        text_align_butt = self.driver.find_element_by_xpath(self.TEXT_ALIGN)
        ActionChains(self.driver).move_to_element(text_align_butt).click().perform()

        val = self.driver.find_element_by_xpath(self.TEXT_ALIGN_VALUE_LEFT)
        ActionChains(self.driver).move_to_element(val).click().perform()

        ActionChains(self.driver).key_down(Keys.DELETE).perform()
