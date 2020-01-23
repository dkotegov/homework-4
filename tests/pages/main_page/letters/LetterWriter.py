# -*- coding: utf-8 -*-
from tests.pages.BasicPage import BasicPage
from selenium.webdriver import ActionChains
from LetterSelector import LetterSelector

from selenium.webdriver.common.keys import Keys

import time


class LetterWriter(BasicPage):
    write_letter_button = '.compose-button_white'

    email_receiver_field = "input[type='text']"
    subject_field = "input[name='Subject']"
    textbox_field = "div[role='textbox']"
    link_field = "input[name='href']"
    text_link_field = "input[name='text']"
    link = "http://park.mail.ru"
    text_link = "Tehnopark"

    textbox_first_line = "div[role='textbox'] > div > div:first-child"
    send_letter_button = '.button2__txt:nth-child(1)'
    close_sent_window_button = "span.button2_close[title='Закрыть']"
    close_sent_window_button_after_move = "span.button2_close[data-title='Закрыть']"
    banner = "div.layer-window[__mediators='layout-manager']"
    advertisement = 'div.message-sent__wrap'

    bold_button = "button[title='Жирный текст']"
    preview_button = "button[title='Отменить']"
    italic_button = "button[title='Наклонный текст']"
    underline_button = "button[title='Подчёркнутый текст']"
    strike_through_button = "button[title='Зачёркнутый текст']"
    clear_all_button = "button[title='Очистить форматирование']"
    link_button = "button[title='Вставить ссылку']"
    confirm_link_button = "div.row--foWEL.margin--31Osl.fluid--39mFx > button:first-child"

    bold_selector = "div[role='textbox'] strong"
    italic_selector = "div[role='textbox'] em"
    underline_selector = "div[role='textbox'] u"
    strike_through_selector = "div[role='textbox'] s"
    span_selector = "div[role='textbox'] span"
    div_selector = "div[role='textbox'] div"

    font_button = "button[title='Шрифт']"
    font_button_selector = "div[role='textbox'] span[style='font-size:32px;line-height:40px;']"
    font_button_type_normal = ".row--foWEL:first-child > :first-child > :nth-child(7) > :last-child > div > :nth-child(1)"
    font_button_type_title1 = ".row--foWEL:first-child > :first-child > :nth-child(7) > :last-child > div > :nth-child(2)"

    text_color_button = "button[title='Цвет текста']"
    text_color_purple = '.row--foWEL:first-child > :first-child > :nth-child(5) > :last-child > div > div:nth-child(18)'
    purple_color_selector = "div[role='textbox'] span[style='color:#e70091;']"
    background_color_button = "button[title='Цвет фона']"
    background_color_blue = '.row--foWEL:first-child > :first-child > :nth-child(6) > :last-child > div > div:nth-child(23)'
    blue_color_selector = "div[role='textbox'] span[style='background-color:#6ee4fe;'"
    alignment_button = "button[title='Выравнивание']"
    alignment_button_selector = "div[role='textbox'] span[style='text-align: center;']"
    alignment_button_type_left = ".row--foWEL:first-child > :first-child > :nth-child(8) > :last-child > div > :nth-child(1)"
    alignment_button_type_center = ".row--foWEL:first-child > :first-child > :nth-child(8) > :last-child > div > :nth-child(2)"

    indent_button = "button[title='Отступ']"
    indent_button_selector = "div[role='textbox'] div[style='margin-left: 40px;']"
    indent_button_type_minus = ".row--foWEL:first-child > :first-child > :nth-child(9) > :last-child > div > :nth-child(1)"
    indent_button_type_plus = ".row--foWEL:first-child > :first-child > :nth-child(9) > :last-child > div > :nth-child(2)"

    def __init__(self, driver):
        self.driver = driver
        self.letter_selector = LetterSelector(self.driver)

    def click_write_letter_button(self):
        elem = self.wait_render(self.write_letter_button)
        elem.click()

    def enter_email_receiver(self, email):
        elem = self.wait_render(self.email_receiver_field)
        ActionChains(self.driver).click(elem).send_keys(email).perform()
        # It's needed to confirm a receiver
        another_field = self.wait_render(self.subject_field)
        ActionChains(self.driver).click(another_field).perform()

    def enter_subject(self, subject):
        elem = self.wait_render(self.subject_field)
        elem.send_keys(subject)

    def enter_textbox(self, text):
        elem = self.wait_render(self.textbox_field)
        elem.send_keys(text)

    def click_send_letter_button(self):
        elem = self.wait_render(self.send_letter_button)
        elem.click()

    def close_sent_window(self):
        self.wait_render(self.banner)
        self.wait_render(self.advertisement)
        elem = self.wait_render(self.close_sent_window_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        # Successful window must be closed before executing other operations
        self.wait_invisible(self.banner)

    def select_text(self):
        actions = ActionChains(self.driver)
        text_container = self.wait_render(self.textbox_first_line)
        length = len(text_container.text)
        actions.click(text_container)
        actions.key_down(Keys.SHIFT)
        for i in range(length):
            actions.send_keys(Keys.ARROW_LEFT)
        actions.perform()

    def set_bold_text(self):
        self.select_text()
        elem = self.wait_render(self.bold_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_render(self.bold_selector)

    def set_italic_text(self):
        self.select_text()
        elem = self.wait_render(self.italic_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_render(self.italic_selector)

    def set_underline_text(self):
        self.select_text()
        elem = self.wait_render(self.underline_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_render(self.underline_selector)

    def set_strike_through_text(self):
        self.select_text()
        elem = self.wait_render(self.strike_through_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_render(self.strike_through_selector)

    def set_font_text_normal(self):
        self.select_text()
        elem = self.wait_render(self.font_button)
        elem.click()
        elem = self.wait_render(self.font_button_type_normal)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_render(self.span_selector)

    def set_font_text_title1(self):
        self.select_text()
        elem = self.wait_render(self.font_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        elem = self.wait_render(self.font_button_type_title1)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_render(self.span_selector)

    def set_text_color_purple(self):
        self.select_text()
        elem = self.wait_render(self.text_color_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        color_panel = self.wait_render(self.text_color_purple)
        ActionChains(self.driver).move_to_element(
            color_panel).click(color_panel).perform()
        self.wait_render(self.purple_color_selector)

    def set_background_color_blue(self):
        self.select_text()
        elem = self.wait_render(self.background_color_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        color_panel = self.wait_render(self.background_color_blue)
        ActionChains(self.driver).move_to_element(
            color_panel).click(color_panel).perform()
        self.wait_render(self.blue_color_selector)

    def set_alignment_text_center(self):
        self.select_text()
        elem = self.wait_render(self.alignment_button)
        elem.click()
        elem = self.wait_render(self.alignment_button_type_center)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_render(self.span_selector)

    def set_indent_text_plus(self):
        self.select_text()
        elem = self.wait_render(self.indent_button)
        elem.click()
        elem = self.wait_render(self.indent_button_type_plus)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_render(self.indent_button_selector)

    def set_indent_text_minus(self):
        self.select_text()
        button = self.wait_render(self.indent_button)
        button.click()
        elem = self.wait_render(self.indent_button_type_plus)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        button.click()
        elem = self.wait_render(self.indent_button_type_plus)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        button.click()
        elem = self.wait_render(self.indent_button_type_minus)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_render(self.indent_button_selector)

    def click_preview_button(self):
        elem = self.wait_render(self.preview_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

    def click_clear_all_button(self):
        elem = self.wait_render(self.clear_all_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

    def click_link_button(self):
        elem = self.wait_render(self.link_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

    def enter_link(self, link):
        elem = self.wait_render(self.link_field)
        elem.send_keys(link)

    def enter_text_link(self, text):
        elem = self.wait_render(self.text_link_field)
        elem.send_keys(text)

    def click_confirm_link(self):
        elem = self.wait_render(self.confirm_link_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
