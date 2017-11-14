# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from vp_check_list.pages.base_page import Component


class LastCommentUserAvatar(Component):
	COMMENTS_LIST = '//div[@class="hookBlock photo-layer_bottom"]//div[@class="comments_lst_cnt"]//div[last()]' \
	                '//div[contains(@class, "comments_text")]//div'
	COMMENTS_DELETE_BUTTON = '//div[@class="hookBlock photo-layer_bottom"]//div[@class="comments_lst_cnt"]' \
	                         '//div[last()]//div[contains(@class, "comments_controls-t")]' \
	                         '//a[@class="fade-on-hover comments_remove ic10 ic10_close-g"]'
	COMMENTS_LIKES_TEXT = '//div[@class="hookBlock photo-layer_bottom"]//div[@class="comments_lst_cnt"]//div' \
	                      '//i[@class="tico_img ic12 ic12_klass tico_img__on-hover"]'

	def __init__(self, driver, avatar_footer):
		super(LastCommentUserAvatar, self).__init__(driver)

		self.__avatar_footer__ = avatar_footer
		self.__comment__ = self.get_last_comment()

	def get_last_comment(self):
		list_comments = self.__avatar_footer__.find_elements_by_xpath(self.COMMENTS_LIST)

		return list_comments[-1]

	def text(self):
		return self.get_text(self.__comment__)

	def get_delete_button(self):
		return WebDriverWait(self.__avatar_footer__, 5, 0.1).until(
			lambda d: d.find_elements_by_xpath(self.COMMENTS_DELETE_BUTTON)
		)

	def delete_comment(self):
		self.execute(self.get_delete_button()[-1])


class CommentsUserAvatar(Component):
	AVATAR_FOOTER = '//div[@class="hookBlock photo-layer_bottom"]'
	AVATAR_INPUT = './/div[@class="itx js-comments_add js-ok-e comments_add-ceditable "]'
	AVATAR_INPUT_BUTTON = './/button[@class="button-pro form-actions_yes" and text()="Добавить"]'
	AVATAR_COMMENTS_COUNT = '//div[@id="hook_Block_PhotoLayerFooterRB"]//span[@class="widget_count js-count"]'

	def __init__(self, driver):
		super(CommentsUserAvatar, self).__init__(driver)
		self.__footer__ = self.get_avatar_footer()

	@property
	def last_comment(self):
		return LastCommentUserAvatar(self.driver, self.__footer__)

	def get_avatar_footer(self):
		return WebDriverWait(self.driver, 5, 0.1).until(
			lambda d: d.find_element_by_xpath(self.AVATAR_FOOTER)
		)

	def get_avatar_input(self):
		return WebDriverWait(self.__footer__, 5, 0.1).until(
			lambda d: d.find_element_by_xpath(self.AVATAR_INPUT)
		)

	def get_comment_amount(self):
		counter = self.driver.find_element_by_xpath(self.AVATAR_COMMENTS_COUNT)
		return int(self.get_text(counter))

	def add_comment_to_avatar(self, message):
		comment_input = self.get_avatar_input()
		before_add = self.get_comment_amount()

		self.execute(comment_input)
		self.set_text_content(comment_input, message)

		button = self.__footer__.find_element_by_xpath(self.AVATAR_INPUT_BUTTON)
		self.execute(button)

		WebDriverWait(self, 10, 0.1).until(
			lambda d: d.get_comment_amount() == before_add + 1
		)

	def delete_comment_from_avatar(self):
		before_add = self.get_comment_amount()

		self.last_comment.delete_comment()

		WebDriverWait(self, 10, 0.1).until(
			lambda d: d.get_comment_amount() == before_add - 1
		)


class UserAvatar(Component):
	AVATAR = '//img[@id="viewImageLinkId"]'

	def __init__(self, driver):
		super(UserAvatar, self).__init__(driver)
		self.__avatar__ = self.get_avatar()

	def get_avatar(self):
		return WebDriverWait(self.driver, 5, 0.1).until(
			lambda d: d.find_element_by_xpath(self.AVATAR)
		)

	def open_avatar(self):
		self.execute(self.__avatar__)

	@property
	def comments(self):
		return CommentsUserAvatar(self.driver)
