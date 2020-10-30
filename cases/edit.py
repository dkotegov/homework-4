import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.auth import AuthSteps
from steps.edit import EditSteps
from steps.main import MainSteps
from steps.new_proj import NewProjSteps
from steps.source import SourceSteps
from steps.tag import TagSteps


# Редактирование проект
class EditTest(unittest.TestCase):
    KEY = os.environ['PASSWORD']
    SUCCESS = 'Добавление прошло успешно'
    SUCCESS_SAVE = 'Сохранение прошло успешно'
    SUCCESS_PIN = 'Метка {}'
    SUCCESS_TEXT = 'font-size: {}px;'
    FAILED_TEXT = 'Некорректный размер'
    MIDDLE_SOURCE = './sources/middle_source.jpg'
    MIDDLE_STRING = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAA'
    FAILED = 'Проект отсутствует'
    FAILED_PIN = 'Ресурс отсутствует'
    PROJ_NAME = 'ВралУЫЕдр'
    LEGEND_NAME = 'acPCaycla'
    TEXT_SIZE = '14'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='127.17.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.auth_page = AuthSteps(self.driver)
        self.auth_page.open()
        self.auth_page.login(self.KEY)

        self.main_page = MainSteps(self.driver)
        self.main_page.go_to_new_proj()

        self.proj_page = NewProjSteps(self.driver)
        self.proj_page.fill_form(self.PROJ_NAME, self.PROJ_NAME)
        self.proj_page.back_to_menu()
        self.proj_id = self.main_page.get_proj_id(self.PROJ_NAME)

        self.main_page.go_to_new_source()
        self.source_page = SourceSteps(self.driver)
        self.source_page.upload_file(self.MIDDLE_SOURCE)
        self.source_page.save_img(self.MIDDLE_SOURCE)
        self.source_page.accept_alert_text()
        self.source_page.back_to_menu()

        self.main_page.go_to_edit(self.proj_id)

        self.createdProj = [self.PROJ_NAME]

        self.edit_page = EditSteps(self.driver)
        self.tag_page = TagSteps(self.driver)

    def tearDown(self):
        self.edit_page.back_to_menu()
        for proj in self.createdProj:
            self.main_page.delete_proj(proj)

        self.main_page.go_to_tag(self.MIDDLE_SOURCE)
        self.tag_page.delete_source()

        self.driver.quit()

    def test_create_legend_success(self):
        self.edit_page.open_leg_lib()
        self.edit_page.create_legend(self.LEGEND_NAME)
        alert = self.edit_page.accept_alert_text()
        self.assertEqual(alert, self.SUCCESS)

    def test_create_legend_no_tag_failed(self):
        self.edit_page.open_leg_lib()
        self.edit_page.create_legend("")
        alert = self.edit_page.do_not_wait_alert()
        self.assertFalse(alert)

    def test_create_pin_success(self):
        self.edit_page.open_pin_lib()
        pin_id = self.edit_page.choose_pin(self.MIDDLE_SOURCE)
        self.edit_page.save_pin(pin_id)
        result = self.edit_page.pin_presence(pin_id)
        self.assertIn(self.SUCCESS_PIN.format(pin_id), result)

    def test_create_pin_wrong_id_failed(self):
        self.edit_page.open_pin_lib()
        self.edit_page.save_pin("0")
        alert = self.edit_page.accept_alert_text()
        self.assertEqual(alert, self.FAILED_PIN)

    def test_create_layer_success(self):
        self.edit_page.open_pic_lib()
        self.edit_page.create_layer(self.MIDDLE_SOURCE, self.MIDDLE_SOURCE)
        result = self.edit_page.layer_presence()
        self.assertIn(self.MIDDLE_STRING, result)

    def test_create_layer_no_name_failed(self):
        self.edit_page.open_pic_lib()
        self.edit_page.create_layer(self.MIDDLE_SOURCE, "")
        result = self.edit_page.do_not_wait_alert()
        self.assertFalse(result)

    def test_create_text_success(self):
        self.edit_page.open_text_lib()
        self.edit_page.create_text(self.TEXT_SIZE)
        result = self.edit_page.default_text_size_presence()
        self.assertIn(self.SUCCESS_TEXT.format(self.TEXT_SIZE), result)

    def test_create_text_wrong_size_failed(self):
        self.edit_page.open_text_lib()
        self.edit_page.create_text("a")
        alert = self.edit_page.accept_alert_text()
        self.assertEqual(self.FAILED_TEXT, alert)

    def test_save_success(self):
        self.edit_page.open_control_lib()
        alert = self.edit_page.save_proj()
        self.assertEqual(alert, self.SUCCESS_SAVE)






