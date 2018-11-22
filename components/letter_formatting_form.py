# coding=utf-8
import selenium
from selenium.common.exceptions import WebDriverException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ES

from components.base_form import BaseForm


class LetterFormattingForm(BaseForm):
    # text formatting elements
    TEST_FILE_DIR = './test_files/'

    BOLD_BUTTON = '//div[@data-test-id="bold"]'
    ITALIC_BUTTON = '//button[@title="Наклонный текст"]'
    UNDERLINED_BUTTON = '//button[@title="Подчёркнутый текст"]'
    STRIKETHROUGH_BUTTON = '//button[@title="Зачёркнутый текст"]'

    TEXT_COLOR_BUTTON = '//button[@title="Цвет текста"]'
    COLOR_VALUE = '//div[@data-test-id="#CAF2F5"]'

    BACKGROUND_COLOR_BUTTON = '//button[@title="Цвет фона"]'
    # BACKGROUND_COLOR_VALUE = '//div[@class="cell--3K4W6"]/div[6]/div[2]/div/div[4]'
    BACKGROUND_COLOR_VALUE = '//div[@data-test-id="highlight"]//div[@data-test-id="#CAF2F5"]'
    FORMATTED_TEXT = '//div[@role="textbox"]/div/div/span'

    FONT_BUTTON = '//button[@title="Шрифт"]'
    FONT_VALUE = '//div[@class="cell--3K4W6"]/div[7]/div[2]/div/div[2]'

    TEXT_ALIGN = '//button[@title="Выравнивание"]'
    # TEXT_ALIGN_VALUE_LEFT = '//div[@class="cell--3K4W6"]/div[8]/div[2]/div/div[1]'
    TEXT_ALIGN_VALUE_RIGHT = '//div[@data-test-id="align"]//div[@data-test-id="right"]'

    TEXT_MARGIN = '//button[@title="Отступ"]'
    TEXT_MARGIN_INC = '//div[@class="cell--3K4W6"]/div[9]/div[2]/div/div[2]'
    TEXT_MARGIN_DEC = '//div[@class="cell--3K4W6"]/div[9]/div[2]/div/div[1]'

    LIST_BUTTON = '//button[@title="Список"]'
    NUMBERED_LIST = '//div[@class="cell--3K4W6"]/div[10]/div[2]/div/div[1]'
    BULLETED_LIST = '//div[@class="cell--3K4W6"]/div[10]/div[2]/div/div[2]'
    LISTED_TEXT = '//div[@role="textbox"]/div/ol'
    BULLETED_TEXT = '//div[@role="textbox"]/div/ul'

    CANCEL_BUTTON = '//button[@title="Отменить"]'
    REPEAT_BUTTON = '//button[@title="Повторить"]'

    LINK_BUTTON = '//div[@class="cell--3K4W6"]/div[13]'
    OK_LINK_BUTTON = '//button[@tabindex="520"]'
    LINK_IN_MESSAGE_FIELD = '//div[@role="textbox"]/div/div/a'

    PICTURE_BUTTON = '//button[@title="Вставить картинку"]/input'
    TEST_PICTURE = TEST_FILE_DIR + 'pict.png'
    IMG_IN_MESSAGE_FIELD = '//div[@role="textbox"]/div/div'

    ClEAR_FORMATTING = '//button[@title="Очистить форматирование"]'

    CANCEL_MESSAGE_BUTTON = '//span[@data-qa-id="cancel"]'

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

    # Увеличить отступ
    def click_on_text_margin_inc(self):
        elem = self.driver.find_element_by_xpath(self.TEXT_MARGIN_INC)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Уменьшить отступ
    def click_on_text_margin_dec(self):
        elem = self.driver.find_element_by_xpath(self.TEXT_MARGIN_DEC)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Список
    def click_on_list_icon(self):
        elem = self.driver.find_element_by_xpath(self.LIST_BUTTON)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Нумерованный список
    def click_on_numbered_list(self):
        elem = self.driver.find_element_by_xpath(self.NUMBERED_LIST)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Маркированный список
    def click_on_bulleted_list(self):
        elem = self.driver.find_element_by_xpath(self.BULLETED_LIST)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Отменить действие
    def click_on_cancel_icon(self):
        elem = self.driver.find_element_by_xpath(self.CANCEL_BUTTON)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Повторить действие
    def click_on_repeat_icon(self):
        elem = self.driver.find_element_by_xpath(self.REPEAT_BUTTON)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Вставить ссылку
    def click_on_link_icon(self):
        elem = self.driver.find_element_by_xpath(self.LINK_BUTTON)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Подтверждение вставки ссылки
    def click_on_ok_link_button(self):
        elem = self.driver.find_element_by_xpath(self.OK_LINK_BUTTON)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Очистить форматирование
    def click_on_clear_formatting_icon(self):
        elem = self.driver.find_element_by_xpath(self.ClEAR_FORMATTING)
        ActionChains(self.driver).move_to_element(elem).click().perform()

    # Нажатие TAB
    def click_on_tab_key(self):
        ActionChains(self.driver).key_down(Keys.TAB).perform()

    # Вставка картинки
    def send_picture(self):
        elem = self.driver.find_element_by_xpath(self.PICTURE_BUTTON)
        elem.send_keys(self.TEST_PICTURE)

    # Получение картинки
    def get_img(self):
        return self.driver.find_element_by_xpath(self.IMG_IN_MESSAGE_FIELD).get_attribute('innerHTML')

    # Получение ссылки
    def get_link(self):
        return self.driver.find_element_by_xpath(self.LINK_IN_MESSAGE_FIELD).get_attribute('href'), \
               self.driver.find_element_by_xpath(self.LINK_IN_MESSAGE_FIELD).get_attribute('innerHTML')

    # Получение цвета элемента
    def get_text_color(self):
        return self.driver.find_element_by_xpath(self.FORMATTED_TEXT) \
            .value_of_css_property("color")

    # Получение цвета фона элемента
    def get_background_color(self):
        return self.driver.find_element_by_xpath(self.FORMATTED_TEXT).value_of_css_property("background-color")

    # Получение свойства font-size
    def get_size_of_text(self):
        return self.driver.find_element_by_xpath(self.FORMATTED_TEXT).value_of_css_property("font-size")

    # Получение свойства line-height
    def get_line_height_of_text(self):
        return self.driver.find_element_by_xpath(self.FORMATTED_TEXT).value_of_css_property("line-height")

    # Получение свойства text-align
    def get_align_of_text(self):
        return self.driver.find_element_by_xpath(self.MESSAGE_FIELD).value_of_css_property("text-align")

    # Получение свойства margin
    def get_margin_of_text(self):
        return self.driver.find_element_by_xpath(self.MESSAGE_FIELD).value_of_css_property("margin-left")

    # Получение нумерованного списка
    def get_numbered_text(self):
        return self.driver.find_element_by_xpath(self.LISTED_TEXT).get_attribute('innerHTML')

    # Получение маркированного списка
    def get_bulleted_text(self):
        return self.driver.find_element_by_xpath(self.BULLETED_TEXT).get_attribute('innerHTML')

    def click_on_backspace(self):
        ActionChains(self.driver).key_down(Keys.DELETE).perform()
        ActionChains(self.driver).key_up(Keys.DELETE).perform()

    # Выделение текста

    def text_selection(self):
        elem = self.driver.find_element_by_xpath(self.MESSAGE_FIELD)
        ActionChains(self.driver).move_to_element(elem).click().perform()

        ActionChains(self.driver).key_down(Keys.LEFT).perform()
        ActionChains(self.driver).key_up(Keys.LEFT).perform()
        ActionChains(self.driver).key_down(Keys.LEFT).perform()
        ActionChains(self.driver).key_up(Keys.LEFT).perform()
        ActionChains(self.driver).key_down(Keys.LEFT).perform()
        ActionChains(self.driver).key_up(Keys.LEFT).perform()
        ActionChains(self.driver).key_down(Keys.LEFT).perform()
        ActionChains(self.driver).key_up(Keys.LEFT).perform()
        ActionChains(self.driver).key_down(Keys.LEFT).perform()
        ActionChains(self.driver).key_up(Keys.LEFT).perform()

        ActionChains(self.driver).key_down(Keys.LEFT_SHIFT).perform()

        ActionChains(self.driver).key_down(Keys.RIGHT).perform()
        ActionChains(self.driver).key_up(Keys.RIGHT).perform()
        ActionChains(self.driver).key_down(Keys.RIGHT).perform()
        ActionChains(self.driver).key_up(Keys.RIGHT).perform()
        ActionChains(self.driver).key_down(Keys.RIGHT).perform()
        ActionChains(self.driver).key_up(Keys.RIGHT).perform()
        ActionChains(self.driver).key_down(Keys.RIGHT).perform()
        ActionChains(self.driver).key_up(Keys.RIGHT).perform()
        ActionChains(self.driver).key_down(Keys.RIGHT).perform()
        ActionChains(self.driver).key_up(Keys.RIGHT).perform()

        ActionChains(self.driver).key_up(Keys.LEFT_SHIFT).perform()

    # Очищение поля ввода
    def clear_field(self):
        # self.text_selection()
        # ActionChains(self.driver).key_down(Keys.BACK_SPACE).perform()
        elem = self.driver.find_element_by_xpath(self.MESSAGE_FIELD)
        elem.clear()

    def click_cancel_writing_message(self):
        cancel_btn = self.driver.find_element_by_xpath(self.CANCEL_MESSAGE_BUTTON)
        cancel_btn.click()
        WebDriverWait(self.driver, 2) \
            .until(ES.invisibility_of_element(cancel_btn))
