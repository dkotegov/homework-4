import os

import unittest
import urllib.parse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from tests.Pages import AuthPage, QuestionPage, PollPage

class CheckListTests(unittest.TestCase):
    # USEREMAIL = 'leshikne@bk.ru'
    # PASSWORD = os.environ['PASSWORD']
    USEREMAIL = 'test_qwerty1122@mail.ru'
    PASSWORD = 'qqaawwss123'
    DEBUG = True


    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.auth_page = AuthPage(self.driver)
        self.question_page = QuestionPage(self.driver)
        self.poll_page = PollPage(self.driver)

        self.question_form = self.question_page.question_form
        self.auth_form = self.auth_page.auth_form
        self.poll_form = self.poll_page.poll_form
        

    def tearDown(self):
        self.driver.quit()

    def openAskPage(self):
        self.auth_page.open()

    # - Если пользователь не авторизован, то при нажатии на кнопку "Фото" или "Видео" должно всплывать окно авторизации.
    def photoVideoUploadTest(self):
        self.question_form.open_photo_upload_form()
        self.question_form.press_esc()

        self.question_form.open_video_upload_form()
        self.question_form.press_esc()

        if self.DEBUG:
            print('Photo/video upload test:.............PASSED\n')

    def authorize(self):  
        self.auth_form.open_form()
        if self.DEBUG:
            print("=============Authorizations============")
            print("Open auth form:...............OK")

        self.auth_form.switch_driver_to_iframe("ag-popup__frame__layout__iframe")
        if self.DEBUG:
            print("Switche to iframe:............OK")

        self.auth_form.set_login(self.USEREMAIL)
        self.auth_form.submit_login()
        if self.DEBUG:
            print("Login input:..................OK")
        
        self.auth_form.set_password(self.PASSWORD)
        self.auth_form.submit_password()
        if self.DEBUG:
            print("Password input:...............OK")

        self.auth_form.switch_driver_to_default_content()
        if self.DEBUG:
            print("Switch to default content:....OK")
            print('Authorization:.......................PASSED\n')

    def largeTextTest(self):
        self.question_form.check_question_textarea_alert()
        self.auth_form.open_form()
        if self.DEBUG:
            print("Large text alert test:...............PASSED\n")

    def invalidQuestionTitleTest(self):
        self.question_form.check_question_title_textarea_alert()
        if self.DEBUG:
            print("Invalid string print:.........OK")

        self.question_form.press_esc()
        self.question_form.press_esc() # На случай появления вторгоо алерта сверху
        if self.DEBUG:
            print("Invalid question title alert test:...PASSED\n")

    def newQuestionEditTest(self):
        self.question_form.make_default_question()
        if self.DEBUG:
            print("make default question:........OK")

        self.question_form.chaeck_edit_time()
        if self.DEBUG:
            print("check ediе time:..............OK")
            print("Question edit case test:.............PASSED\n")

    def settingsTest(self):
        self.openAskPage()
        self.question_form.check_settings_page()
        if self.DEBUG:
            print("Login input:..................OK")
            print("Open settings:................OK")
            print("Settings open test:..................PASSED\n")

    def pollOptionsTest(self):
        self.openAskPage()
        self.poll_form.open_poll_form()
        if self.DEBUG:
            print("Poll page open:...............OK")

        self.poll_form.check_poll_option_correct_add()
        if self.DEBUG:
            print("Settings open test:..................PASSED\n")

    def test(self):

        self.openAskPage()
        self.photoVideoUploadTest()
        
        # Авторизируемся 
        self.authorize()

        # - При вводе большого текста в поле "Текст вопроса" появляется предупреждение об ограничении в 3800 символов.
        self.largeTextTest()

        # - При вводе невалидной строки в теме вопроса/опроса (Прример: "ыв ыва ыва 23") длжно всплывать окно с ошибкой 
        #   "Просьба более подробно и грамотно сформулировать тему вопроса.".
        self.invalidQuestionTitleTest()

        # - При публикации нового опроса должно всплывать окно, информирующее о возможности редактирования содежания опроса в течении 30 мин.
        self.newQuestionEditTest()

        # - По нажатию на кнопку "Настройки" открывается страница пользовательских настроек. X
        self.settingsTest()

        # - Автоматическое добавление новой формы ответа по нажатию на последнюю в списке форму вопросов при "включении" опции 
        #   "Можно выбрать несколько вариантов" в форме создания опроса и его публикации. 
        #   То есть в форме создания опроса изначально нам доступны 3 варианта ответа в виде 3-х незаполненных форм, 
        #   проверить нужно добавление новой формы при нажатии на последнюю форму в списке.
        self.pollOptionsTest()