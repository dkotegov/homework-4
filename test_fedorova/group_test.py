# -*- coding: utf-8 -*-

from base_test import BaseTest
from page import GroupsPage, MyGroupsPage

class GroupTest(BaseTest):

    def test_join_group(self):						#добавление,переход через общие группы
	all_groups_form = GroupsPage(self.driver).form
	all_groups_form.join()
	group_form = all_groups_form.redirect()
	self.assertTrue(group_form.is_member())

    def test_leave_group(self):					#удаление, переход через общие группы
	while True:
		all_groups_form = GroupsPage(self.driver).form
		all_groups_form.join()
		group_form = all_groups_form.redirect()
  		if not group_form.is_close_group():
			break;
		GroupsPage(self.driver).open()
	group_form.leave()
	self.driver.refresh();
	self.assertFalse(group_form.is_member())		

    def test_join_group_assert_appear_left(self):		#проверка появилось ли слева при добавлении
	all_groups_form = GroupsPage(self.driver).form
	all_groups_form.join()
	name = all_groups_form.get_group_name()
	my_groups_page = MyGroupsPage(self.driver)
	my_groups_page.open()
	my_groups_form = my_groups_page.form
	self.assertTrue(my_groups_form.check_group_in_left(name))


    def test_join_group_assert_appear_in_my_groups(self):	#добавление, проверка что появилось в моих группах
	all_groups_form = GroupsPage(self.driver).form
	all_groups_form.join()
	group_name = all_groups_form.get_group_name()
	my_groups_page = MyGroupsPage(self.driver)
	my_groups_page.open()
	my_groups_form = my_groups_page.form
	self.assertTrue(my_groups_form.assert_in_groups(group_name))


    def test_leave_group_assert_not_in_my_groups(self):		# удаление, проверка что нет в моих группах
	while True:
		all_groups_form = GroupsPage(self.driver).form
		all_groups_form.join()
		name = all_groups_form.get_group_name()
		group_form = all_groups_form.redirect()
  		if not group_form.is_close_group():
			break;
		GroupsPage(self.driver).open()
	group_form.leave()
	my_groups_page = MyGroupsPage(self.driver)		
	my_groups_page.open()
	my_groups_form = my_groups_page.form
	self.assertFalse(my_groups_form.assert_in_groups(name))





