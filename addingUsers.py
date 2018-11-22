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
driver.get(startUrl + "get/page/admin")

def get(s):
	return driver.find_element_by_id(s)
	
def delay():
	pass
	#time.sleep(2)
	
print("  ")
print("Clear content and add users test:")
print("  ")
delay()

get("dropContentPanelShowBtn").click()
delay()

get("clearContentBtn").click()

try:
	WebDriverWait(driver, 5).until (EC.text_to_be_present_in_element((By.ID, 'clearContentAlertBox'), "Очистка прошла успешно."))
finally:
	print("Clear content test OK")
	delay()
		
def tryAddUser(department, login, password, box, waitMessage, logMessage):
	departmentClickElem = get("otdel_" + str(int(int(department) / 10)))
	departmentClickElem.click()
	get("loginField").clear()
	get("passwordField").clear()
	get("loginField").send_keys(login)
	get("passwordField").send_keys(password)
	get("addUserBtn").click()
	try:
		WebDriverWait(driver, 5).until (EC.text_to_be_present_in_element((By.ID, box), waitMessage))
	finally:
		print(logMessage)
		delay()
		
get("usersPanelShowBtn").click()
delay()
		
tryAddUser("20", "maxim", "123", "addUserAlert", "Добавление пользователя прошло успешно.", "Add user 1 text OK")
tryAddUser("20", "maxim", "paspas", "alertBox", "Пользователь уже существует.", "Block user 1 text OK")

tryAddUser("30", "george", "456", "addUserAlert", "Добавление пользователя прошло успешно.", "Add user 2 text OK")
tryAddUser("30", "george", "paspas", "alertBox", "Пользователь уже существует.", "Block user 2 text OK")

tryAddUser("10", "alex", "789", "addUserAlert", "Добавление пользователя прошло успешно.", "Add user 3 text OK")
tryAddUser("10", "alex", "paspas", "alertBox", "Пользователь уже существует.", "Block user 3 text OK")

get("getUsersBtn").click()
delay()

def waitPrintingUser(ID, login, department):
	# control ID
	try:
		WebDriverWait(driver, 5).until (EC.text_to_be_present_in_element((By.ID, "render_user_id_" + ID), ID))
	finally:
		print("Found ID " + ID + " OK")
	# control login
	try:
		WebDriverWait(driver, 5).until (EC.text_to_be_present_in_element((By.ID, "render_user_login_" + ID), login))
	finally:
		print("Found login " + login + " OK")
	# control department
	try:
		WebDriverWait(driver, 5).until (EC.text_to_be_present_in_element((By.ID, "render_user_department_" + ID), department))
	finally:
		print("Found department " + department + " OK")
		
waitPrintingUser("1", "maxim", "Отдел разработки мобильных приложений")
delay()
waitPrintingUser("2", "george", "Отдел разработки серверного программного обеспечения")
delay()
waitPrintingUser("3", "alex", "Отдел анализа статистики")
delay()

get("dropContentPanelShowBtn").click()
delay()

get("clearContentBtn").click()

try:
	WebDriverWait(driver, 5).until (EC.text_to_be_present_in_element((By.ID, 'clearContentAlertBox'), "Очистка прошла успешно."))
finally:
	print("Clear content test OK")
	delay()

driver.close()

