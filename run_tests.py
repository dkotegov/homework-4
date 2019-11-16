# -*- coding: utf-8 -*-

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def login(self): 
        driver = self.driver
        driver.implicitly_wait(10) # seconds
        driver.get("https://e.mail.ru/settings/userinfo?afterReload=1")
        self.assertIn("Mail.ru", driver.title)

        frame = self.driver.find_element_by_css_selector('#auth-form iframe')
        self.driver.switch_to.frame(frame)

        email = driver.find_element_by_css_selector('input[name=Login]')
        email.send_keys("yekaterina.kirillova.1998@bk.ru")
        email.submit()

        password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=Password]"))
        )
        password.send_keys("qwerYtuarRyYY12")
        password.submit()


    # REWRITE!!!
    def wait(self, wait_until=None, timeout=15):
        return WebDriverWait(self.driver, timeout).until(wait_until)

    # REWRITE!!!
    def wait_redirect(self, url=None):
        if url is None:
            self.wait(EC.url_changes(self.driver.current_url))
        else:
            self.wait(EC.url_matches(url))
        

    def test_tick_in_time_zone(self):   
        self.login()
        driver = self.driver
        tick = driver.find_element_by_css_selector('input[name=UseAutoTimezone]')
        if tick.is_selected():
            tick.click()
        
        selectList = driver.find_element_by_css_selector('select[name=TimeZone]')
        # selectList = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, "select[name=TimeZone]"))
        # )

        submit = self.driver.find_element_by_css_selector('div.form__actions__inner button[type="submit"]')
        submit.click()

        self.wait_redirect('https://e.mail.ru/settings?.*')

    def test_phone_redirect(self):
        self.login()
        driver = self.driver
        link = self.driver.find_element_by_css_selector('#phonesContainer > div > div:nth-child(2) > a')
        
        new_window_url = link.get_attribute("href")
        driver.get(new_window_url)

        self.assertEqual(driver.current_url, new_window_url)
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.url_to_be('https://account.mail.ru/security/recovery'))

    def test_load_image(self):
        self.login()
        driver = self.driver
        loadImage = self.driver.find_element_by_css_selector('#js-edit-avatar > div.form__row__widget > span.form__row__avatar__infotext > div:nth-child(2) > div:nth-child(1) > div.js-browse.js-fileapi-wrapper > input')
        loadImage.send_keys("/home/kate/Изображения/MacBook-Pro.png")

        saveButton = self.driver.find_element_by_css_selector('#MailRuConfirm > div > div.is-avatar_in.popup_avatar > div.js-content.popup_avatar__content > div.popup__controls > div > div:nth-child(1)')
        cancelButton = self.driver.find_element_by_css_selector('#MailRuConfirm > div > div.is-avatar_in.popup_avatar > div.js-content.popup_avatar__content > div.popup__controls > div > div:nth-child(2)')
        
    def test_do_snapshot(self):
        self.login()
        driver = self.driver
        makeSnapshot = self.driver.find_element_by_css_selector('#js-edit-avatar > div.form__row__widget > span.form__row__avatar__infotext > div:nth-child(2) > div:nth-child(2) > button')
        if makeSnapshot.is_enabled():    
            makeSnapshot.click()
            driver.switch_to_alert()
            Alert(driver).dismiss()
         
    def test_cancel(self):
        self.login()
        driver = self.driver
        name = self.driver.find_element_by_css_selector('#FirstName')
        oldValue = name.get_attribute("value")
        name.send_keys('New name')
        
        cancel = self.driver.find_element_by_css_selector('#formPersonal > div.form__actions__wrapper > div > div > a')
        cancel.click()

        driver.get("https://e.mail.ru/settings/userinfo?afterReload=1")
        name = self.driver.find_element_by_css_selector('#FirstName')
        newValue = name.get_attribute("value")
        self.assertEqual(oldValue, newValue)

    def test_error_saving(self):
        self.login()
        driver = self.driver
        name = self.driver.find_element_by_css_selector('#FirstName')
        name.clear()
        
        submit = self.driver.find_element_by_css_selector('div.form__actions__inner button[type="submit"]')
        submit.click()

        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".form__top-message_error"))
        )
        self.assertEqual('Не заполнены необходимые поля', error.text)

        errorName = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#formPersonal > div:nth-child(12) > div.form__row__widget > div"))
        )
        self.assertEqual('Заполните обязательное поле', errorName.text)

 


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()