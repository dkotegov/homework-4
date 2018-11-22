## -*- coding: utf-8 -*-

import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):
	def equal(self, v1, v2):
		self.assertEqual(v1, v2)
		
startUrl = "http://176.119.156.90/"
		
driver = webdriver.Firefox()
driver.get(startUrl + "get/page/index")

def get(s):
	return driver.find_element_by_id(s)
	
def delay():
	pass
	#time.sleep(2)
	
print("  ")
print("Signin form test:")
print("  ")
delay()

def controlAuthInputFields(login, password, waitMessage, logMessage):
	get("loginField").clear()
	get("passwordField").clear()
	get("loginField").send_keys(login)
	get("passwordField").send_keys(password)
	get("signInBtn").click()
	try:
		WebDriverWait(driver, 5).until (EC.text_to_be_present_in_element((By.ID, 'alertBox'), waitMessage))
	finally:
		print(logMessage)
		delay()
		
controlAuthInputFields("aaabbbcccddddeeefffggghhhkkk", "pas123", "Логин слишком длинный.", "Long login test OK")
controlAuthInputFields("login123", "ppppppaaaaassssswwwwooorrrddd", "Пароль слишком длинный.", "Long password test OK")

controlAuthInputFields("", "pas123", "Поле ввода логина пусто.", "Empty login test OK")
controlAuthInputFields("login123", "", "Поле ввода пароля пусто.", "Empty password test OK")

controlAuthInputFields("login*1_23", "pAsWd123", "Некорректный логин. Логин может состоять только из латинских букв и цифр.", "Bad login test OK")
controlAuthInputFields("LoGIn123", "pas-pas-12@3", "Некорректный пароль. Пароль может состоять только из латинских букв и цифр.", "Bad password test OK")

controlAuthInputFields("login123", "pas123", "Неверный логин или пароль.", "Bad user test OK")

driver.close()

def controlAddingUserByAdminInputFields(login, password, waitMessage, logMessage):
	get("loginField").clear()
	get("passwordField").clear()
	get("loginField").send_keys(login)
	get("passwordField").send_keys(password)
	get("addUserBtn").click()
	try:
		WebDriverWait(driver, 5).until (EC.text_to_be_present_in_element((By.ID, 'alertBox'), waitMessage))
	finally:
		print(logMessage)
		delay()

driver = webdriver.Firefox()
driver.get(startUrl + "get/page/admin")

print("  ")
print("Admin adding user form test:")
print("  ")
delay()

get("usersPanelShowBtn").click()
delay()

controlAddingUserByAdminInputFields("aaabbbcccddddeeefffggghhhkkk", "pas123", "Логин слишком длинный.", "Long login test OK")
controlAddingUserByAdminInputFields("login123", "ppppppaaaaassssswwwwooorrrddd", "Пароль слишком длинный.", "Long password test OK")

controlAddingUserByAdminInputFields("", "pas123", "Поле ввода логина пусто.", "Empty login test OK")
controlAddingUserByAdminInputFields("login123", "", "Поле ввода пароля пусто.", "Empty password test OK")

controlAddingUserByAdminInputFields("login*1_23", "pAsWd123", "Некорректный логин. Логин может состоять только из латинских букв и цифр.", "Bad login test OK")
controlAddingUserByAdminInputFields("LoGIn123", "pas-pas-12@3", "Некорректный пароль. Пароль может состоять только из латинских букв и цифр.", "Bad password test OK")

driver.close()

