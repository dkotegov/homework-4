# -*- coding: utf-8 -*-
import os
import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class Page(object):
    BASE_URL = 'http://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

class GroupsPage(Page):
    PATH = 'groups/'

    @property
    def form(self):
        return AllGroups(self.driver)

class GroupPage(Page):
    PATH = ''

    def __init__(self, driver, path):
	Page.__init__(self, driver)
	self.PATH = path

    @property
    def form(self):
        return Group(self.driver)

    @property
    def my_form(self):
        return MyGroup(self.driver)


class MyGroupsPage(Page):
    PATH = 'groups/mine/'

    @property
    def form(self):
        return MyGroups(self.driver)  


class Component(object):
    def __init__(self, driver):
        self.driver = driver

class Groups(Component):
    CHECK_IMG_GROUP = '//div[@class="stub-img stub-img stub-group-business-48 stub-img__48"]/img[@class="photo_img"]'
    GROUP_HREF = '//a[contains(@class,"o two-lines")]'
    CREATE_GROUP = '//a[@class="add-stub al add-stub__hor"]'
    PUBLIC_GROUP = '//a[@class="create-group-dialog_i"]'
    NAME_INPUT = '//input[@id="field_name"]'
    CREATE_BUTTON = '//input[@id="hook_FormButton_button_create"]'
    CATEGORY = '//select[@name="st.layer.pageMixedCategory"]'
    OPTION = '//option[@value="subcatVal12001"]'

    def check_group_in_left(self, name):
	self.driver.implicitly_wait(5)
	imgs = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_xpath(self.CHECK_IMG_GROUP)
        )
	for img in imgs:
		if img.get_attribute("alt") == name:
			return True
	return False
		
    def get_group_name(self):
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.presence_of_element_located((By.XPATH, self.GROUP_HREF))
	)
	return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.GROUP_HREF).text
        )

    def redirect(self):
	link = self.driver.find_element_by_xpath(self.GROUP_HREF).get_attribute("href")
	gp = GroupPage(self.driver, link)
	gp.open()
        return gp.form

    def in_groups(self, group_name):
	elems = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_xpath(self.GROUP_HREF)
        )
	for elem in elems:
		if elem.text == group_name:
			return True
	return False

    def create_public_group(self, group_name):
	self.driver.find_element_by_xpath(self.CREATE_GROUP).click()
	create_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PUBLIC_GROUP)
        )
        create_button.click()
	input_field = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NAME_INPUT)
        )
	input_field.send_keys(group_name)
	self.driver.find_element_by_xpath(self.CATEGORY).click()
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.presence_of_element_located((By.XPATH, self.OPTION))
	)
	self.driver.find_element_by_xpath(self.OPTION).click()
	self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(self.CREATE_BUTTON))
	return GroupPage(self.driver, self.driver.current_url).my_form


class AllGroups(Groups):
    JOIN_BUTTON = '//button[text()="Присоединиться"][@class="button-pro __small"]'	
		
    def join(self):
        self.driver.find_element_by_xpath(self.JOIN_BUTTON).click()



class MyGroups(Groups):	
    MODERATION = '//a[text()="Модерирую"]'
    VISISBILITY = '//a[@class="filter_i __active" and text()="Модерирую"]'
    
    def moderation_groups(self):
	moder = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MODERATION)
        )
	moder.click()
	WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.VISISBILITY)
        )


class Group(Component):
    MEMBER = '//span[text()="Участник" or text()="Запрос отправлен" or text()="В группе"]' 
    LEAVE_BUTTON = '//a[@class="dropdown_i"]'

    def leave(self):
	self.driver.find_element_by_xpath(self.MEMBER).click()
	leave = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LEAVE_BUTTON)
        )
	leave.click()

    def is_member(self):
	try:
       		self.driver.find_element_by_xpath(self.MEMBER)
		return True
	except NoSuchElementException:
		return False
        
class MyGroup(Component):
    ACTION_BUTTON = '//em[text()="Другие действия"]'
    DELETE_BUTTON = '//a/span[text()="Удалить"]'
    DELETE_BUTTON1 = '//input[@type = "submit"][@value = "Удалить"]'
    CREATE_THEME = '//div[text()="Создать новую тему"]'
    INSERT_TEXT = '//div[@id="posting_form_text_field"]'
    SHARE_BUTTON = '//input[@value="Поделиться" and @class="button-pro"]'
    TEXT = '//div[@class="media-text_cnt_tx textWrap"]'
    ARROW = '//div[@class="feed_menu"]'
    DELETE_THEME = '//a/span[text()="Удалить тему"]'
    PLACEHOLDER = '//div[@class="input_placeholder"]'
    SETTINGS = '//span[text()="Настройки"]'
    NAME = '//input[@name="st.name"]'
    SAVE = '//input[@value="Сохранить"]'
    MAIN_NAME = '//h1[@class="mctc_name_tx"]'
    OVERLAY = '//div[@class="posting-form_overlay invisible"]' #posting-form_overlay __active
    TOP_MENU = '//div[@id="mainTopContentRow"]'

    def delete(self):
	action = WebDriverWait(self.driver, 30, 0.1).until(
	    lambda d: d.find_element_by_xpath(self.ACTION_BUTTON)
	)
	actions = ActionChains(self.driver)
	actions.move_to_element(action).click().perform()
	delete = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUTTON)
        )
	delete.click()
	delete1 = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUTTON1)
        )
	delete1.click()
	return GroupsPage(self.driver).form

    def create_new_theme(self, text):
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.presence_of_element_located((By.XPATH, self.CREATE_THEME))
	)
	self.driver.find_element_by_xpath(self.CREATE_THEME).click()
	WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.OVERLAY)
        )
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.element_to_be_clickable((By.XPATH, self.INSERT_TEXT))
	)
	element = self.driver.find_element_by_xpath(self.INSERT_TEXT)
	self.driver.execute_script("arguments[0].click();", element)
	element.send_keys(text)
	self.driver.execute_script("arguments[0].remove();", self.driver.find_element_by_xpath(self.PLACEHOLDER))
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.presence_of_element_located((By.XPATH, self.SHARE_BUTTON))
	)
	self.driver.find_element_by_xpath(self.SHARE_BUTTON).click()
	WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TOP_MENU)
        )

    def check_theme(self, text):
	try:
		return self.driver.find_element_by_xpath(self.TEXT).text == text
	except NoSuchElementException:
		return False

    def delete_theme(self):
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.presence_of_element_located((By.XPATH, self.ARROW))
	)
	actions = ActionChains(self.driver)
	actions.move_to_element(self.driver.find_element_by_xpath(self.ARROW)).perform()
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.visibility_of_element_located((By.XPATH, self.DELETE_THEME))
	)
	self.driver.find_element_by_xpath(self.DELETE_THEME).click()

    def rename(self, text):
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.presence_of_element_located((By.XPATH, self.SETTINGS))
	)
	actions = ActionChains(self.driver)
	actions.move_to_element(self.driver.find_element_by_xpath(self.SETTINGS)).click().perform()
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.presence_of_element_located((By.XPATH, self.NAME))
	)
	self.driver.find_element_by_xpath(self.NAME).click()
	self.driver.find_element_by_xpath(self.NAME).send_keys(text)
	WebDriverWait(self.driver, 30, 0.1).until(
		expected_conditions.element_to_be_clickable((By.XPATH, self.SAVE))
	)
	self.driver.find_element_by_xpath(self.SAVE).click()

    def check_name(self, text):
	return self.driver.find_element_by_xpath(self.MAIN_NAME).text == text

        
class AuthForm(Component):
    LOGIN = '//input[@id="field_email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@type="submit"][@class="button-pro __wide"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


