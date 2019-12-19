import unittest
import os
import configparser
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from pages.auth_page import AuthPage
from pages.userinfo_page import UserinfoPage


class UserinfoTest(unittest.TestCase):
    userinfo_page = None
    userinfo_form = None

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.authorize()

        self.userinfo_page = UserinfoPage(self.driver)
        self.userinfo_page.open()
        self.userinfo_form = self.userinfo_page.form

    def tearDown(self):
        self.driver.quit()

    def test_check_timezone(self):  
        TIMEZONE_SELECT_LIST_VALUE = '(GMT+03:00) Москва, Санкт-Петербург' 

        self.userinfo_form.uncheck_tick()
        self.userinfo_form.wait_for_timezone_selector_first_value(TIMEZONE_SELECT_LIST_VALUE)
        self.assertEqual(TIMEZONE_SELECT_LIST_VALUE, self.userinfo_form.get_timezone_selector_first_value())

    def test_image_preview_buttons(self):  
        IMAGE = 'test.png'     
        SAVE_BUTTON_VALUE = 'Сохранить'
        CANCEL_BUTTON_VALUE = 'Отменить'

        self.userinfo_form.wait_load_image(IMAGE)    
        self.assertEqual(SAVE_BUTTON_VALUE, self.userinfo_form.get_save_avatar_button_value())
        self.assertEqual(CANCEL_BUTTON_VALUE, self.userinfo_form.get_cancel_avatar_button_value())

    def test_save_empty_field(self):
        TOP_MESSAGE = 'Не заполнены необходимые поля'
        LAST_NAME_ERROR = 'Заполните обязательное поле'
        EMPTY_LAST_NAME = ''

        self.userinfo_form.set_last_name(EMPTY_LAST_NAME)
        self.userinfo_form.save()
        self.assertEqual(TOP_MESSAGE, self.userinfo_form.get_top_message())
        self.assertEqual(LAST_NAME_ERROR, self.userinfo_form.get_last_name_error_message())

    def test_gender(self):
        unselected_gender_before = self.userinfo_form.get_unselected_gender()
        unselected_gender_before_id = unselected_gender_before.id
        unselected_gender_before.click()
        self.userinfo_form.save()

        self.userinfo_page.open()
        self.userinfo_form = self.userinfo_page.form

        unselected_gender_after = self.userinfo_form.get_unselected_gender()
        unselected_gender_after_id = unselected_gender_after.id
        self.assertNotEqual(unselected_gender_before_id, unselected_gender_after_id)

    def test_long_name(self):
        LONG_LAST_NAME = f'{"very" * 10} long'
        TOP_MESSAGE = 'Некоторые поля заполнены неверно'
        LAST_NAME_ERROR = 'Поле не может содержать специальных символов и должно иметь длину от 1 до 40 символов.'
        
        self.userinfo_form.set_last_name(LONG_LAST_NAME)
        self.userinfo_form.save()
        self.assertEqual(TOP_MESSAGE, self.userinfo_form.get_top_message())
        self.assertEqual(LAST_NAME_ERROR, self.userinfo_form.get_last_name_error_message())

    def test_suggest_town(self):
        TOWN_PREFIX = 'Мос' 
        SUGGEST_LIST = [
            'Москва, Россия',
            'Московский, Московская обл., Россия',
            'Мосальск, Калужская обл., Россия'
        ]

        self.userinfo_form.set_town(TOWN_PREFIX)
        self.userinfo_form.wait_for_last_suggest(SUGGEST_LIST[-1])
        self.assertEqual(SUGGEST_LIST, self.userinfo_form.get_suggests_for_town()) 

    def test_wrong_town(self):
        WRONG_TOWN_NAME = 'qwertyuiop'
        TOP_MESSAGE = 'Некоторые поля заполнены неверно'
        TOWN_ERROR = 'Проверьте название города'

        self.userinfo_form.set_town(WRONG_TOWN_NAME)
        self.userinfo_form.wait_for_suggests_invisible()
        self.userinfo_form.save()
        self.assertEqual(TOP_MESSAGE, self.userinfo_form.get_top_message())
        self.assertEqual(TOWN_ERROR, self.userinfo_form.get_town_message())             

    def test_correct_input(self):

        NEW_STRING = 'test'
        self.userinfo_form.input_firstname(NEW_STRING)
        self.userinfo_form.input_lastname(NEW_STRING)
        self.userinfo_form.input_nickname(NEW_STRING)

        self.userinfo_form.save()
        
        self.userinfo_page.open()
        self.userinfo_form = self.userinfo_page.form


        self.assertEqual(self.userinfo_form.get_last_name(), NEW_STRING)
        self.assertEqual(self.userinfo_form.get_first_name(), NEW_STRING)
        self.assertEqual(self.userinfo_form.get_nickname(), NEW_STRING)

    def test_png_image_upload(self):
    
        CURRENT_IMAGE = self.userinfo_form.get_avatar_image_url()
        NEW_IMAGE = self.userinfo_form.input_image_and_get_new_image_url('test.png')
        self.assertNotEqual(CURRENT_IMAGE, NEW_IMAGE)

    def test_bmp_image_upload(self):
    
        CURRENT_IMAGE = self.userinfo_form.get_avatar_image_url()
        NEW_IMAGE = self.userinfo_form.input_image_and_get_new_image_url('test.bmp')
        self.assertNotEqual(CURRENT_IMAGE, NEW_IMAGE)

    def test_gif_image_upload(self):
    
        CURRENT_IMAGE = self.userinfo_form.get_avatar_image_url()
        NEW_IMAGE = self.userinfo_form.input_image_and_get_new_image_url('test.gif')
        self.assertNotEqual(CURRENT_IMAGE, NEW_IMAGE)

    def test_ico_image_upload(self):
    
        CURRENT_IMAGE = self.userinfo_form.get_avatar_image_url()
        NEW_IMAGE = self.userinfo_form.input_image_and_get_new_image_url('test.ico')
        self.assertNotEqual(CURRENT_IMAGE, NEW_IMAGE)

    
    def test_jpeg_image_upload(self):
    
        CURRENT_IMAGE = self.userinfo_form.get_avatar_image_url()
        NEW_IMAGE = self.userinfo_form.input_image_and_get_new_image_url('test.jpeg')
        self.assertNotEqual(CURRENT_IMAGE, NEW_IMAGE)

    def test_jpg_image_upload(self):
    
        CURRENT_IMAGE = self.userinfo_form.get_avatar_image_url()
        NEW_IMAGE = self.userinfo_form.input_image_and_get_new_image_url('test.JPG')
        self.assertNotEqual(CURRENT_IMAGE, NEW_IMAGE)   

    def test_authorize_redirect_after_logout(self):
        self.userinfo_form.open_settings_in_new_window()
        self.userinfo_form.click_logout_button()

        self.userinfo_form.switch_to_window(0)
        self.userinfo_form.wait_for_logout_message()

    def test_date_lists(self):
        DAY_CHILD_INPUT = 20
        MONTH_CHILD_INPUT = 12
        MONTH_NAME = 'Декабрь'
        YEAR_CHILD_INPUT = 1996

        self.userinfo_form.click_on_day_input()
        self.userinfo_form.click_on_day_child_input(DAY_CHILD_INPUT)
        self.userinfo_form.click_on_month_input()

        self.userinfo_form.click_on_month_child_input(MONTH_CHILD_INPUT)
        self.userinfo_form.click_on_year_input()
        
        self.userinfo_form.click_on_year_child_input(YEAR_CHILD_INPUT)

        self.userinfo_form.save()
        
        self.userinfo_page.open()
        self.userinfo_form = self.userinfo_page.form

        self.assertEqual(self.userinfo_form.get_birth_day(), str(DAY_CHILD_INPUT))
        self.assertEqual(self.userinfo_form.get_birth_month(), MONTH_NAME)
        self.assertEqual(self.userinfo_form.get_birth_year(), str(YEAR_CHILD_INPUT))

    def test_load_image_pdf(self): 
        FILE_PDF = 'test.pdf'
        TOP_MESSAGE = 'Недопустимый формат изображения'

        self.userinfo_form.load_image(FILE_PDF)
        self.assertEqual(TOP_MESSAGE, self.userinfo_form.get_image_error_message())

    def test_load_image_mp3(self):
        FILE_MP3 = 'test.mp3'
        TOP_MESSAGE = 'Недопустимый формат изображения'

        self.userinfo_form.load_image(FILE_MP3)
        self.assertEqual(TOP_MESSAGE, self.userinfo_form.get_image_error_message())

    def test_load_image_txt(self):
        FILE_TXT = 'test.txt'
        TOP_MESSAGE = 'Недопустимый формат изображения'

        self.userinfo_form.load_image(FILE_TXT)
        self.assertEqual(TOP_MESSAGE, self.userinfo_form.get_image_error_message())

    def test_load_image_sh(self):
        FILE_SH = 'test.sh'
        TOP_MESSAGE = 'Недопустимый формат изображения'

        self.userinfo_form.load_image(FILE_SH)
        self.assertEqual(TOP_MESSAGE, self.userinfo_form.get_image_error_message())

    def test_load_image_go(self):  
        FILE_GO = 'test.go'
        TOP_MESSAGE = 'Недопустимый формат изображения'

        self.userinfo_form.load_image(FILE_GO)
        self.assertEqual(TOP_MESSAGE, self.userinfo_form.get_image_error_message())      

    def test_load_big_image(self):  
        BIG_IMAGE = 'big_image.jpg'
        TOP_MESSAGE = 'Слишком большое разрешение изображения'

        self.userinfo_form.load_image(BIG_IMAGE)
        self.assertEqual(TOP_MESSAGE, self.userinfo_form.get_image_error_message())        

    def test_cancel_changed_image(self):           
        TEST_IMAGE = 'image.jpeg'
        NEW_IMAGE = self.userinfo_form.input_image_and_get_new_image_url(TEST_IMAGE)
        self.userinfo_form.cancel()

        self.userinfo_page.open()
        self.userinfo_form = self.userinfo_page.form
        CURRENT_IMAGE = self.userinfo_form.get_avatar_image_url()

        self.assertEqual(CURRENT_IMAGE, NEW_IMAGE)
             