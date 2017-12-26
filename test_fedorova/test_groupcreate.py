# -*- coding: utf-8 -*-
import random
import string


from base_test import BaseTest
from page import GroupsPage, MyGroupsPage, GroupPage

class BaseWithGroupCreate(BaseTest):

    def setUp(self):
        super(BaseWithGroupCreate, self).setUp()

	self.group_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
	self.all_groups_form = GroupsPage(self.driver).form
	self.my_group_form = self.all_groups_form.create_public_group(self.group_name)

class TestsWithGroupCreate(BaseWithGroupCreate):

    def test_create_group(self):				#создание группы
	my_groups_page = MyGroupsPage(self.driver)
	my_groups_page.open()
	my_groups_form = my_groups_page.form
	my_groups_form.moderation_groups()
	my_group = my_groups_form.get_group_name()
	self.assertEquals(self.group_name, my_group)

    def test_delete_group(self):				#удаление группы 
	self.my_group_form.delete()
	my_groups_page = MyGroupsPage(self.driver)
	my_groups_page.open()
	my_groups_form = my_groups_page.form
	my_groups_form.moderation_groups()
	self.assertFalse(my_groups_form.assert_in_groups(self.group_name))

    def test_create_post(self):					#создание поста 
	text = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
	self.my_group_form.create_new_theme(text)
	self.assertTrue(self.my_group_form.check_theme(text))

    def test_delete_post(self):					#удаление поста 
	text = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
	self.my_group_form.create_new_theme(text)
	self.my_group_form.delete_theme()
	self.driver.refresh();
	self.assertFalse(self.my_group_form.check_theme(text))

    def test_edit_name(self):					#rename
	self.my_group_form.rename(self.group_name)
	my_group_page = GroupPage(self.driver, self.driver.current_url.replace('settings',''))
	my_group_page.open()
	self.assertTrue(self.my_group_form.check_name(self.group_name*2))
