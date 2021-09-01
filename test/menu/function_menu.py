import os
import unittest

from pages.load_page import HomePage
from utils.auth import setup_auth
from utils.create_some_elements import create_elements, delete_elements, \
                                       upload_elements, favorite_add
from test.default_setup import default_setup


class MenuTests(unittest.TestCase):
    NEW_NAME_FILE = 'test_rename'
    NEW_NAME_FOLDER = 'test_folder'
    COPY_FOLDER = 'test_folder_copy'
    NAME_CREATE = 'test_create_folder'
    NAME_CREATE_TOOLBAR = 'test_create_folder_toolbar'
    NAME_CREATE_SHARE = 'test_create_folder_share'
    NAME_CREATE_SHARE_TOOLBAR = 'test_create_folder_share_toolbar'
    REPLACE = 'test_folder_replace'
    LIST_USER = ['Только смотреть', 'Смотреть и загружать файлы']
    LIST_TIME = ['Всегда', 'Час', 'День', 'Неделя', 'Месяц']
    OFFER = ['На месяц', 'На год', 'Профессионалам',
             'В подарок', 'Спецпредложение']
    TYPE_MAIL = ['Фото и картинки', 'Документы', 'Музыка',
                 'Видео', 'Другие', 'Все']

    def setUp(self):
        default_setup(self)
        setup_auth(self)
        self.home_page = HomePage(self.driver)

    def test_load_file_menu(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE])
        elements_list = self.home_page.take_all_elements()
        self.home_page.open_drop_menu(elements_list[1])
        self.home_page.save_element_from_the_menu()
        self.home_page.swap_first()
        delete_elements(self)

    def test_load_file_from_icon(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE])
        self.home_page.select_element()
        self.home_page.save_elements_by_icon()
        delete_elements(self)

    def test_highlight_all_elements(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE])
        all_elements = self.home_page.take_all_elements()
        self.home_page.take_all_highlight()
        highlight_elements = self.home_page.check_highlight_elements()
        self.assertEqual(len(all_elements) - 1, len(highlight_elements))
        delete_elements(self)

    def test_load_all_elements(self):
        upload_elements(self)
        self.home_page.take_all_highlight()
        self.home_page.save_elements()
        delete_elements(self)

    def test_off_all_highlight(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE])
        self.home_page.take_all_highlight()
        self.home_page.take_all_highlight()
        element_highlight = self.home_page.check_highlight_elements()
        self.assertEqual(0, len(element_highlight))
        delete_elements(self)

    def test_copy_element_from_menu_this_create_folder(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE])
        elements_list = self.home_page.take_all_elements()
        elem = self.home_page.open_drop_menu(elements_list[1])
        self.home_page.copy_element()
        self.home_page.create_folder()
        self.home_page.input_info(self.COPY_FOLDER)
        self.home_page.click_create()
        self.home_page.click_button_copy()
        self.home_page.double_click_element(self.COPY_FOLDER)
        self.home_page.find(elem)
        delete_elements(self)

    def test_copy_element_from_menu(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE])
        elements_list = self.home_page.take_all_elements()
        elem = self.home_page.open_drop_menu(elements_list[1])
        self.home_page.copy_element()
        folders = self.home_page.take_folders()
        self.home_page.click_element_folder(folders[2].text)
        self.home_page.click_button_copy()
        self.home_page.double_click_element(folders[2].text)
        self.home_page.find(elem)
        delete_elements(self)

    def test_delete_elements(self):
        create_elements(self, [self.NEW_NAME_FOLDER])
        self.home_page.click_close_dialog()
        self.home_page.click_element(self.NEW_NAME_FOLDER)
        self.home_page.del_elements()
        self.home_page.click_button_delete()
        res = self.home_page.find_element(self.NEW_NAME_FOLDER)
        self.assertEqual(False, res)

    def test_delete_elements_for_menu(self):
        create_elements(self, [self.NEW_NAME_FOLDER])
        self.home_page.click_close_dialog()
        element = self.home_page.find(self.NEW_NAME_FOLDER)
        self.home_page.open_drop_menu(element)
        self.home_page.del_elements()
        self.home_page.click_button_delete()
        res = self.home_page.find_element(self.NEW_NAME_FOLDER)
        self.assertEqual(False, res)

    def test_replace_element_from_menu_this_create_folder(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE])
        elements_list = self.home_page.take_all_elements()
        self.home_page.open_drop_menu(elements_list[1])
        self.home_page.move_element()
        self.home_page.create_folder()
        self.home_page.input_info(self.REPLACE)
        self.home_page.click_create()
        self.home_page.click_replace()
        self.home_page.double_click_element(self.REPLACE)
        self.home_page.find(self.REPLACE)
        delete_elements(self)

    def test_replace_element_from_menu(self):
        create_elements(self, [self.REPLACE, self.NAME_CREATE])
        elements_list = self.home_page.take_all_elements()
        self.home_page.open_drop_menu(elements_list[1])
        self.home_page.move_element()
        folders = self.home_page.take_folders()
        name = folders[2].text
        self.home_page.click_element_folder(name)
        self.home_page.click_replace()
        self.home_page.double_click_element(name)
        self.home_page.find(name)
        delete_elements(self)

    def test_rename_file(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE])
        elements_list = self.home_page.take_all_elements()
        self.home_page.open_drop_menu(elements_list[1])
        self.home_page.rename_element()
        self.home_page.input_new_name(self.NEW_NAME_FILE)
        self.home_page.click_button_rename()
        self.home_page.wait_rename(self.NEW_NAME_FILE)
        delete_elements(self)

    def test_open_new_tab_file(self):
        create_elements(self, [self.NAME_CREATE])
        elements_list = self.home_page.take_all_elements()
        elem = self.home_page.open_drop_menu(elements_list[1])
        self.home_page.open_new_tab()
        url = self.home_page.check_url()
        self.assertEqual(f'https://cloud.mail.ru/home/{elem}/', url)
        delete_elements(self)

    def test_add_to_favorite_from_menu(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE, self.NEW_NAME_FOLDER])
        elements_list = self.home_page.take_all_elements()
        elem = self.home_page.open_drop_menu(elements_list[1])
        self.home_page.add_to_favorite()
        self.home_page.check_favorite(elem, True)
        delete_elements(self)

    def test_add_to_favorite_toolbar(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE, self.NEW_NAME_FOLDER])
        elements_list = self.home_page.take_all_elements()
        self.home_page.click_element(elements_list[2].text)
        self.home_page.add_to_favorite_toolbar()
        self.home_page.check_favorite(elements_list[2].text, True)
        delete_elements(self)

    def test_remove_to_favorite_from_menu(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE, self.NEW_NAME_FOLDER])
        elements_list = self.home_page.take_all_elements()
        favorite_add(self, elements_list)
        elem = self.home_page.open_drop_menu(elements_list[1])
        self.home_page.remove_to_favorite()
        self.home_page.check_favorite(elem, False)
        delete_elements(self)

    def test_remove_to_favorite_toolbar(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE, self.NEW_NAME_FOLDER])
        elements_list = self.home_page.take_all_elements()
        favorite_add(self, elements_list)
        self.home_page.click_element(elements_list[1].text)
        self.home_page.remove_to_favorite_toolbar()
        self.home_page.check_favorite(elements_list[1].text, False)
        delete_elements(self)

    def test_share_link(self):
        create_elements(self, [self.NAME_CREATE, self.NEW_NAME_FOLDER])
        elements_list = self.home_page.take_all_elements()
        elem = self.home_page.open_drop_menu(elements_list[1])
        self.home_page.share_link()
        for user_settings in self.LIST_USER:
            self.home_page.open_dropbox_user()
            self.home_page.change_dropbox_item(user_settings)
        for time_settings in self.LIST_TIME:
            self.home_page.open_dropbox_time_share()
            self.home_page.change_dropbox_item(time_settings)
        url = self.home_page.take_share()
        self.home_page.click_close_window()
        self.home_page.click_logout()
        self.driver.get(url)
        self.home_page.find(elem)
        self.setUp()
        delete_elements(self)

    def test_upload_file(self):
        self.home_page.click_close_dialog()
        list_file = os.listdir('data')
        for name_file in list_file:
            self.home_page.click_upload()
            delete_elements(self)
            self.home_page.input_file(name_file)
            result = self.home_page.wait_load()
            self.assertEqual('Загрузка успешно завершена', result)
        delete_elements(self)

    def test_upload_files(self):
        list_file = os.listdir('data')
        for name_file in list_file:
            self.home_page.click_upload_blue_button(name_file)
            result = self.home_page.wait_load()
            self.assertEqual('Загрузка успешно завершена', result)

    def test_create_folder(self):
        elements = self.home_page.take_all_elements()
        elements[0].click()
        self.home_page.create_folder_home_page()
        self.home_page.input_info(self.NAME_CREATE)
        self.home_page.click_create()
        self.home_page.open_cloud()
        self.home_page.find(self.NAME_CREATE)
        delete_elements(self)

    def test_create_folder_share(self):
        elements = self.home_page.take_all_elements()
        elements[0].click()
        self.home_page.create_folder_share_home_page()
        self.home_page.input_info(self.NAME_CREATE_SHARE)
        self.home_page.click_create_and_share()
        self.home_page.click_close_window()
        url = self.driver.current_url
        self.assertEqual(
            f'https://cloud.mail.ru/home/{self.NAME_CREATE_SHARE}/',
            url)
        delete_elements(self)

    def test_create_document(self):
        elements = self.home_page.take_all_elements()
        elements[0].click()
        self.home_page.create_document()
        self.home_page.swap_first()
        self.home_page.wait_create_element('Новый документ.docx')
        url = self.home_page.check_url()
        self.assertEqual(
            'https://cloud.mail.ru/office/edit/home/%D0%9D%D0%BE%D0%B2%D1%8B'
            '%D0%B9%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82.docx',
            url)
        self.home_page.swap_first()
        delete_elements(self)

    def test_create_table(self):
        elements = self.home_page.take_all_elements()
        elements[0].click()
        self.home_page.create_table()
        self.home_page.swap_first()
        self.home_page.wait_create_element('Новая таблица.xlsx')
        url = self.home_page.check_url()
        self.assertEqual(
            'https://cloud.mail.ru/office/edit/home/%D0%9D%D0%BE%D0%B2%D0%B0'
            '%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0.xlsx',
            url)
        self.home_page.swap_first()
        delete_elements(self)

    def test_create_presentation(self):
        elements = self.home_page.take_all_elements()
        elements[0].click()
        self.home_page.create_presentation()
        self.home_page.swap_first()
        self.home_page.wait_create_element('Новая презентация.pptx')
        url = self.home_page.check_url()
        self.assertEqual(
            'https://cloud.mail.ru/office/edit/home/%D0%9D%D0%BE%D0%B2%D0%B0'
            '%D1%8F%20%D0%BF%D1%80%D0%B5%D0%B7%D0%B5%D0%BD%D1%82%D0%B0%D1%86'
            '%D0%B8%D1%8F.pptx',
            url)
        self.home_page.swap_first()
        delete_elements(self)

    def test_create_folder_toolbar(self):
        self.home_page.click_close_dialog()
        self.home_page.create_from_toolbar()
        self.home_page.create_folder_home_page()
        self.home_page.input_info(self.NAME_CREATE_TOOLBAR)
        self.home_page.click_create()
        self.home_page.find(self.NAME_CREATE_TOOLBAR)
        delete_elements(self)

    def test_create_folder_share_toolbar(self):
        self.home_page.click_close_dialog()
        self.home_page.create_from_toolbar()
        self.home_page.create_folder_share_home_page()
        self.home_page.input_info(self.NAME_CREATE_SHARE_TOOLBAR)
        self.home_page.click_create_and_share()
        self.home_page.click_close_window()
        url = self.driver.current_url
        self.assertEqual(
            f'https://cloud.mail.ru/home/{self.NAME_CREATE_SHARE_TOOLBAR}/',
            url)
        delete_elements(self)

    def test_create_document_toolbar(self):
        self.home_page.click_close_dialog()
        self.home_page.create_from_toolbar()
        self.home_page.create_documentx()
        self.home_page.swap_first()
        self.home_page.wait_create_element('Новый документ.docx')
        url = self.home_page.check_url()
        self.assertEqual(
            'https://cloud.mail.ru/office/edit/home/'
            '%D0%9D%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82.docx',
            url)
        self.home_page.swap_first()
        delete_elements(self)

    def test_create_table_toolbar(self):
        self.home_page.click_close_dialog()
        self.home_page.create_from_toolbar()
        self.home_page.create_tablex()
        self.home_page.swap_first()
        self.home_page.wait_create_element('Новая таблица.xlsx')
        url = self.home_page.check_url()
        self.assertEqual(
            'https://cloud.mail.ru/office/edit/home/%D0%9D%D0%BE%D0%B2%D0%B0'
            '%D1%8F%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0.xlsx',
            url)
        self.home_page.swap_first()
        delete_elements(self)

    def test_ads_disable(self):
        self.home_page.click_disable_ads()
        url = self.home_page.check_url()
        self.assertEqual(
            'https://cloud.mail.ru/subscriptions/?utm_source=cloud-pro-ads-up'
            '-buy&utm_medium=referral&utm_campaign=pro-ads-upline#pro',
            url)

    def test_ads_offer_swap(self):
        self.home_page.click_disable_ads()
        self.home_page.check_url()
        for name_offer in self.OFFER:
            self.home_page.click_swap(name_offer)
            select_offer = self.home_page.check_select_offer(name_offer)
            self.assertEqual(name_offer, select_offer)

    def test_open_subscription(self):
        self.home_page.click_disable_ads()
        self.home_page.check_url()
        self.home_page.click_close_dialog()
        self.home_page.click_active_sub()
        active_sub = self.home_page.check_sub()
        self.assertEqual('Бесплатный объём Облака', active_sub)

    def test_open_subscription_history(self):
        self.home_page.click_disable_ads()
        self.home_page.check_url()
        self.home_page.click_close_dialog()
        self.home_page.click_active_sub()
        self.home_page.click_history_buy()
        history_buy = self.home_page.check_history_buy()
        self.assertEqual('Покупок не было', history_buy)

    def test_open_basket(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE, self.NEW_NAME_FOLDER])
        delete_elements(self)
        self.home_page.click_basket()

    def test_clear_basket(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE, self.NEW_NAME_FOLDER])
        delete_elements(self)
        self.home_page.click_basket()
        self.home_page.click_clear_basket()
        self.home_page.click_button_clear()
        self.home_page.check_empty_basket()

    def test_restore_element(self):
        create_elements(self, [self.NAME_CREATE, self.NAME_CREATE_SHARE, self.NEW_NAME_FOLDER])
        delete_elements(self)
        restore_phrase = 'Все файлы восстановлены'

        self.home_page.click_basket()
        self.home_page.click_button_restore()
        result = self.home_page.wait_restore()
        self.assertEqual(restore_phrase, result)
        delete_elements(self)

    def test_open_recommendation(self):
        self.home_page.click_recommend()
        url = self.driver.current_url
        self.assertEqual('https://cloud.mail.ru/recommend/', url)

    def test_open_mail(self):
        self.home_page.click_mail()
        url = self.driver.current_url
        self.assertEqual('https://cloud.mail.ru/attaches/', url)

    def test_mail_swap(self):
        self.home_page.click_mail()
        for filter in self.TYPE_MAIL:
            self.home_page.click_swap(filter)
            self.home_page.check_select_filter_mail()

    def test_change_view_list(self):
        upload_elements(self)
        self.home_page.click_view()
        self.home_page.select_view_list()
        delete_elements(self)

    def test_change_view_table(self):
        upload_elements(self)
        self.home_page.click_view()
        self.home_page.select_view_table()
        delete_elements(self)

    def test_change_sort_date(self):
        upload_elements(self)
        self.home_page.click_sort()
        self.home_page.select_sort_date()
        delete_elements(self)

    def test_change_sort_size(self):
        upload_elements(self)
        self.home_page.click_sort()
        self.home_page.select_sort_size()
        delete_elements(self)

    def test_change_sort_alfa(self):
        upload_elements(self)
        self.home_page.click_sort()
        self.home_page.select_sort_alfa()
        delete_elements(self)
