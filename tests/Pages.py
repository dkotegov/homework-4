import os

import unittest
import urllib.parse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Pages:

class Page(object):
    BASE_URL = 'https://otvet.mail.ru/ask'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urllib.parse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

class QuestionPage(Page):
    PATH = ''

    @property
    def question_form(self):
        return QuestionForm(self.driver)

class AuthPage(Page):
    PATH = ''

    @property
    def auth_form(self):
        return AuthForm(self.driver)

class PollPage(Page):
    PATH = ''

    @property
    def poll_form(self):
        return PollForm(self.driver)

# Component:

class Component(object):

    def __init__(self, driver):
        self.driver = driver

    def switch_driver_to_iframe(self, iframe_class_name):
        WebDriverWait(self.driver, 5).until( \
            EC.frame_to_be_available_and_switch_to_it( \
                (By.CLASS_NAME, 'ag-popup__frame__layout__iframe')))

    def switch_driver_to_default_content(self):
        self.driver.switch_to_default_content()

    def press_esc(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
    
# Forms:

class AuthForm(Component):
    LOGIN = '//input[@name="Login"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT_LOGIN = '//span[text()="Ввести пароль"]'
    SUBMIT_PASSWORD = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход"]'

    def open_form(self):
        login_button = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN_BUTTON)
        )
        login_button.click()
        # self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def find_login_input(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN)
        )

    def find_login_submit_button(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_LOGIN)
        )


    def send_login(self, login):
        login_form = self.find_login_input()
        submit_button = self.find_login_submit_button()
        login_form.send_keys(login)
        submit_button.click()

    def set_login(self, login):
        login_form = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN)
        )
        login_form.send_keys(login)
        # self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)
    
    def submit_login(self):
        # submit_login_button = WebDriverWait(self.driver, 15, 0.1).until(
        #     lambda d: d.find_element_by_xpath(self.SUBMIT_LOGIN)
        # )
        # submit_login_button.click()
        self.driver.find_element_by_xpath(self.SUBMIT_LOGIN).click()

    def set_password(self, pwd):
        password_form =  WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, 'Password')))
        password_form.send_keys(pwd)
        
    def submit_password(self):
        submit_password_button = WebDriverWait(self.driver, 15, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_PASSWORD)
        )
        submit_password_button.click()

    def authorization(self, mail, passwd):
        # self.set_login(mail)
        # self.submit_login()
        self.send_login(mail)
        self.set_password(passwd)
        self.submit_password()


class PollForm(Component):
    def open_poll_form(self):
        poll_form = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_class_name('_3LtjwRRK3wqD0IfUUl1sxB_0')
        )
        poll_form.click()

    def check_poll_option_correct_add(self):

        variant_3 = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//div[@name="poll_options"]/div[4]/label/div[2]/div/div/div/input')
        )
        variant_3.click()
        variant_3.send_keys("getting 4 option")
        
        variant_4 = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//div[@name="poll_options"]/div[5]/label/div[2]/div/div/div/input')
        )

        variant_4.click()
        variant_4.send_keys("getting 5 option")

        self.driver.find_element_by_xpath('//div[@name="poll_options"]/div[6]/label/div[2]/div/div/div/input')


class QuestionForm(Component):

    LARGETEXT = 'sdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffffsdfffffffffffffffffffffffffffffff'

    def find_question_form(self):
        return self.driver.find_element_by_xpath('//div[@data-vv-as="«Текст вопроса»"]')

    def open_photo_upload_form(self):
        photo_span = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//span[text()="Фото"]')
        )
        photo_span.find_element_by_xpath('./..').click()

    def open_video_upload_form(self):
        video_span = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//span[text()="Видео"]')
        )
        video_span.find_element_by_xpath('./..').click()

    def close_login_form(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def print_question_text(self, text):
        title_input = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//textarea[@name="question_additional"]')
        )
        title_input.send_keys(text)
        # self.driver.find_element_by_xpath('//textarea[@name="question_additional"]').send_keys(text)

    def print_question_title(self, text):
        text_input = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//textarea[@name="question_text"]')
        )
        text_input.send_keys(text)
        # self.driver.find_element_by_xpath('//textarea[@name="question_text"]').send_keys(text)
        
    def check_question_title_textarea_alert(self):
        self.print_question_title("sadf")
        self.print_question_text("sadf")
        
        ask_button = WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "_3ykLdYEqVa47ACQrpqnZOj_0"))
        )
        ask_button.click()

        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_class_name('popup--fade')
        )

    def check_question_textarea_alert(self):
        self.print_question_text(self.LARGETEXT)
        self.driver.find_element_by_xpath('//div[text()="Поле «Текст вопроса» не может быть больше 3800 символов."]')

    def make_default_question(self):
        # self.print_question_title("Вопрос про салаты")
        # self.print_question_text("Собственно говоря, если греческий салат испортился, то можно ли его называть древнегреческим?")
        # self.print_question_title("Ээ Кызлыр жэб кыздыр ламар? Котык басс дырбн кизлар?")
        # self.print_question_text("Тухтур игрым буерак из матч ай джаст донт нов вот то райт хир фор секс сессфулли пассинг бот чекинг")
        self.print_question_title(" Ду бист ай, оо мин ин де швайн")
        self.print_question_text("ыва")
        
        ask_button = WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "_3ykLdYEqVa47ACQrpqnZOj_0"))
        )
        ask_button.click()

    def chaeck_edit_time(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_class_name('q-edit-control')
        )

    def delete_question(self):
        self.driver.find_element_by_class_name('btn action--sms').click()

    def check_settings_page(self):
        settings_button = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//span[text()="Настройки"]')
        )    
        settings_button.click()
        WebDriverWait(self.driver, 10, 0.1).until(
            # lambda d: d.find_element_by_xpath('//button[@name="submit_btn"]').click()
            lambda d: d.find_element_by_class_name('page-settings')
        )    