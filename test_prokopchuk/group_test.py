# -*- coding: utf-8 -*-

from test_prokopchuk.base_test import BaseTest
from test_prokopchuk.page import *
from test_prokopchuk.utils import Utils


class GroupsTest(BaseTest):

    def test_add_to_bookmarks(self):  # добавление в закладки
        new_group_name = Utils.random_str(8)
        groups_form = GroupsPage(self.driver).form
        my_group_form = groups_form.create_public_group(new_group_name)
        my_group_form.set_bookmark()
        self.assertTrue(my_group_form.is_added_to_bookmarks() is True)

    def test_change_group_desc(self):  # Смена описания группы
        new_group_name = Utils.random_str(5)
        groups_form = GroupsPage(self.driver).form
        my_group_form = groups_form.create_public_group(new_group_name)
        new_description = Utils.random_str(10)
        my_group_form.change_description(new_description)
        my_group_page = MyGroupPage(self.driver, self.driver.current_url.replace('settings', ''))
        my_group_page.open()
        self.assertTrue(my_group_form.check_group_description(new_description))

    def test_photo_section(self):  # Сокрытие и Показ фото в группе
        new_group_name = Utils.random_str(5)
        groups_form = GroupsPage(self.driver).form
        my_group_form = groups_form.create_public_group(new_group_name)

        def _test_hide_photo_section():  # Скрытие видимости фото
            settings_form = my_group_form.open_settings()
            settings_form.change_section_visibility(False, GroupSettings.PHOTOS_SECTION)
            my_group_page = MyGroupPage(self.driver, self.driver.current_url.replace('/settings/details', ''))
            my_group_page.open()
            self.assertFalse(my_group_form.check_section_visible(u'Фото '))

        def _test_show_photo_section():  # Включение видимости фото
            settings_form = my_group_form.open_settings()
            settings_form.change_section_visibility(True, GroupSettings.PHOTOS_SECTION)
            my_group_page = MyGroupPage(self.driver, self.driver.current_url.replace('/settings/details', ''))
            my_group_page.open()
            self.assertTrue(my_group_form.check_section_visible(u'Фото '))

        _test_hide_photo_section()
        _test_show_photo_section()

    def test_video_section(self):  # Сокрытие и Показ Видео в группе
        new_group_name = Utils.random_str(5)
        groups_form = GroupsPage(self.driver).form
        my_group_form = groups_form.create_public_group(new_group_name)

        def _test_hide_video_section():  # Скрытие видимости видео
            settings_form = my_group_form.open_settings()
            settings_form.change_section_visibility(False, GroupSettings.VIDEOS_SECTION)
            my_group_page = MyGroupPage(self.driver, self.driver.current_url.replace('/settings/details', ''))
            my_group_page.open()
            self.assertFalse(my_group_form.check_section_visible(u'Видео '))

        def _test_show_video_section():  # Включение видимости видео
            settings_form = my_group_form.open_settings()
            settings_form.change_section_visibility(True, GroupSettings.VIDEOS_SECTION)
            my_group_page = MyGroupPage(self.driver, self.driver.current_url.replace('/settings/details', ''))
            my_group_page.open()
            self.assertTrue(my_group_form.check_section_visible(u'Видео '))

        _test_hide_video_section()
        _test_show_video_section()

    def test_change_group_category(self):  # Смена категории группы
        new_group_name = Utils.random_str(5)
        groups_form = GroupsPage(self.driver).form
        my_group_form = groups_form.create_public_group(new_group_name)
        settings_form = my_group_form.open_settings()
        settings_form.change_group_category_to_star()
        my_group_page = MyGroupPage(self.driver, self.driver.current_url.replace('/settings', ''))
        my_group_page.open()
        self.assertTrue(my_group_form.check_group_category_is_star())

    def test_posts_natural_order(self):  # порядок отображения постов - сверху вниз в порядке снижения свежести 6
        new_group_name = Utils.random_str(5)
        groups_form = GroupsPage(self.driver).form
        my_group_form = groups_form.create_public_group(new_group_name)
        post1_text = Utils.random_str(5).decode('utf-8')  # to UNICODE
        post2_text = Utils.random_str(5).decode('utf-8')
        my_group_form.create_new_theme(post1_text)
        my_group_form.create_new_theme(post2_text)
        texts_in_natural_order = my_group_form.get_all_posts_texts()
        self.assertTrue(texts_in_natural_order[0] == post2_text)
        self.assertTrue(texts_in_natural_order[1] == post1_text)

    def test_post_pinning(self):
        new_group_name = Utils.random_str(5)
        groups_form = GroupsPage(self.driver).form
        my_group_form = groups_form.create_public_group(new_group_name)
        post1_text = Utils.random_str(5).decode('utf-8')  # to UNICODE
        post2_text = Utils.random_str(5).decode('utf-8')
        my_group_form.create_new_theme(post1_text)
        my_group_form.create_new_theme(post2_text)

        def _test_check_posts_order_after_pin():  # порядок отображения постов при закрепленном старом посте
            my_group_form.click_pin_post(1)  # прикрепляем более ранний пост
            texts_after_pin = my_group_form.get_all_posts_texts()
            self.assertTrue(texts_after_pin[0] == post1_text)
            self.assertTrue(texts_after_pin[1] == post2_text)

        def _test_check_posts_order_after_unpin():  # порядок отображения постов после открепления поста
            my_group_form.click_unpin_post(0)  # открепить
            texts_after_pin = my_group_form.get_all_posts_texts()
            self.assertTrue(texts_after_pin[0] == post2_text)
            self.assertTrue(texts_after_pin[1] == post1_text)

        _test_check_posts_order_after_pin()
        _test_check_posts_order_after_unpin()

    def test_post_KLASS(self):
        new_group_name = Utils.random_str(5)
        groups_form = GroupsPage(self.driver).form
        my_group_form = groups_form.create_public_group(new_group_name)
        post1_text = Utils.random_str(5).decode('utf-8')  # to UNICODE
        my_group_form.create_new_theme(post1_text)
        self._test_post_STAV_KLASS(my_group_form)
        self._test_post_NE_STAV_KLASS(my_group_form)

    def _test_post_STAV_KLASS(self, my_group_form):
        self.assertTrue(my_group_form.get_post_likes_count() is None)
        my_group_form.click_like_post()
        self.assertTrue(my_group_form.get_post_likes_count() == u'1')

    def _test_post_NE_STAV_KLASS(self, my_group_form):
        my_group_form.click_like_post()
        self.assertTrue(my_group_form.get_post_likes_count() is None)