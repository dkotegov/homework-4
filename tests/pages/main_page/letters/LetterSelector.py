# -*- coding: utf-8 -*-
from tests.pages.BasicPage import BasicPage
from selenium.webdriver import ActionChains


class LetterSelector(BasicPage):
    first_letter = '.llc:first-of-type > .llc__container'
    letter = '.llc > .llc__container'
    letter_subject = 'a.llc > .llc__container .llc__subject'
    letter_subject_only = '.llc__subject'
    first_letter_text = 'a.llc:first-of-type > .llc__container .llc__snippet'
    letter_read_status = '.ll-rs'
    first_letter_avatar = '.llc:first-of-type button.ll-av'
    letter_avatar = 'button.ll-av'
    link_element = 'a[href="http://park.mail.ru"]'

    letters = 'a.llc'

    opened_letter_subject = '.thread__subject'
    opened_letter_text = ''
    opened_letter_body = '.letter__body'

    all_letters = 'div.portal-menu-element_select'

    dataset_empty = '.dataset__empty'

    bold_selector = 'div.letter-body__body strong'
    italic_selector = 'div.letter-body__body em'
    underline_selector = 'div.letter-body__body u'
    strike_through_selector = 'div.letter-body__body s'
    span_selector = 'div.letter-body__body span'
    purple_color_selector = "div.letter-body__body span[style='color:#e70091;']"
    blue_color_selector = "div.letter-body__body span[style='background-color:#6ee4fe;']"
    div_selector = 'div.letter-body__body div'

    font_button_selector = 'div.letter-body__body span[style="font-size:32px;line-height:40px;"]'
    alignment_button_selector = 'div.letter-body__body div[style="text-align:center"]'
    indent_button_selector = 'div.letter-body__body div[style="margin-left:40px"]'

    div_with_not_bold_text = 'div.cke_editable > div > div:not(strong):first-child'
    div_with_bold_text = 'div.cke_editable > div > div:first-child > strong'
    div_with_unformating_text = 'div.cke_editable > div > div:not(em):not(u):not(strong):not(s):first-child'

    def select_letter(self, subject):
        letter = self.find_letter_by_subject(subject)
        elem = letter.find_element_by_css_selector(self.letter_avatar)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

    def open_letter(self, subject):
        elem = self.find_letter_subject_real(subject)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

    def get_opened_letter_subject(self):
        subject = self.wait_render(self.opened_letter_subject)
        return subject.text

    def get_opened_letter_text(self):
        body = self.get_opened_letter_body()
        # Only text, without sign
        return body.split('\n')[0]

    def get_opened_letter_body(self):
        body = self.wait_render(self.opened_letter_body)
        return body.text

    def get_replied_letter_text(self):
        body = self.get_opened_letter_body()
        return body.split('\n')[-1]

    def get_letter_read_status(self, subject):
        letter = self.find_letter_by_subject(subject)
        elem = letter.find_element_by_css_selector(self.letter_read_status)
        if elem.get_attribute('title') == (u'Пометить прочитанным') or elem.get_attribute('data-title') == (u'Пометить прочитанным'):
            return False
        else:
            return True

    def set_letter_read_status(self, subject, status):
        letter = self.find_letter_by_subject(subject)
        elem = letter.find_element_by_css_selector(self.letter_read_status)
        # Invert status only it's needed
        if self.get_letter_read_status(subject) != status:
            elem.click()

    def select_all_letters(self):
        elem = self.wait_render(self.all_letters)
        elem.click()

    def click_letter(self, subject):
        elem = self.wait_render(self.first_letter)
        elem.click()

    def is_there_no_letters(self):
        self.wait_render(self.dataset_empty)

    def get_bold(self):
        elem = self.wait_render(self.bold_selector)
        return elem

    def get_italic(self):
        elem = self.wait_render(self.italic_selector)
        return elem

    def get_underline(self):
        elem = self.wait_render(self.underline_selector)
        return elem

    def get_strike_through(self):
        elem = self.wait_render(self.strike_through_selector)
        return elem

    def get_font_text_title1(self):
        elem = self.wait_render(self.span_selector)
        return elem

    def get_text_color_purple(self):
        elem = self.wait_render(self.purple_color_selector)
        return elem

    def get_background_color_blue(self):
        elem = self.wait_render(self.blue_color_selector)
        return elem

    def get_alignment_text_center(self):
        elem = self.wait_render(self.alignment_button_selector)
        return elem

    def get_indent_text(self):
        elem = self.wait_render(self.indent_button_selector)
        return elem

    def get_bold_text(self):
        elem = self.wait_render(self.div_with_bold_text)
        return elem.text

    def get_not_bold_text(self):
        elem = self.wait_render(self.div_with_not_bold_text)
        return elem.text

    def get_unformating_text(self):
        elem = self.wait_render(self.div_with_unformating_text)
        return elem.text

    def get_link_text(self):
        elem = self.wait_render(self.link_element)
        return elem.text

    def get_all_letters_subjects(self):
      subjects = self.wait_render_all(self.letter_subject)
      return subjects

    def get_all_letters(self):
        letters = self.wait_render_all(self.letters)
        return letters
    
    def find_letter_subject_real(self, subject):
        subjects_elements = self.get_all_letters_subjects()
        for subject_element in subjects_elements:
            if subject_element.text == subject:
                return subject_element
        return None
    
    def find_letter_by_subject(self, subject):
        letters = self.get_all_letters()
        for letter in letters:
            subject_element = letter.find_element_by_css_selector(self.letter_subject_only)
            if subject_element.text == subject:
                return letter
        return None
  
