# -*- coding: utf-8 -*-
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class TopMenuTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://sport.mail.ru")

        dropDown = ['Футбол', 'Хоккей', 'Летние', 'Баскетбол']
        for drop in dropDown:
            bimIds = []
            myPath = "//span[contains(text(),'" + drop + "')]/../../following-sibling::span/span/span"
            elements = driver.find_elements_by_xpath(myPath)
            for element in elements:
                bimIds.append(element.get_attribute("bem-id"))
            for bemId in bimIds:
                dDown = driver.find_element_by_link_text(drop)
                action = ActionChains(driver)
                hover = action.move_to_element(dDown)
                hover.perform()
                time.sleep(0.1)
                myPath = "//span[@bem-id=" + bemId + "]"
                element = WebDriverWait(driver, 30, 0.1).until(
                    lambda d: d.find_element_by_xpath(myPath)
                )
                element.click()
                self.assertTrue(driver.find_element_by_xpath("//title[contains(text(),'" + drop + "')]"))

        notDropDown = ['Бокс', 'Теннис', 'Биатлон', 'Формула-1']
        for notDrop in notDropDown:
            myPath = "//span[contains(text(),'" + notDrop + "')]"
            element = WebDriverWait(driver, 30, 0.1).until(
                lambda d: d.find_element_by_xpath(myPath)
            )
            element.click()
            self.assertTrue(driver.find_element_by_xpath("//title[contains(text(),'" + notDrop + "')]"))

        myPath = "//span[contains(text(),'Другие')]"
        dDown = WebDriverWait(driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(myPath)
        )
        action = ActionChains(driver)
        hover = action.move_to_element(dDown)
        hover.perform()
        time.sleep(0.1)
        myPath = "//span[contains(text(),'Другие')]/../../following-sibling::span/span/div/div/div"
        elements = driver.find_elements_by_xpath(myPath)
        for element in elements:
            myPath = "./div"
            innerElements = element.find_elements_by_xpath(myPath)
            for innerElement in innerElements:
                ActionChains(driver).key_down(Keys.COMMAND).click(innerElement).key_up(Keys.COMMAND).perform()
            curr_window = driver.current_window_handle
            for handle in driver.window_handles:
                if handle != curr_window:
                    driver.switch_to_window(handle)
                    self.assertTrue(driver.find_element_by_xpath("//title"))
                    driver.close()
            driver.switch_to_window(curr_window)
        myPath = "//span[contains(text(),'Соцсети')]/../a"
        elements = driver.find_elements_by_xpath(myPath)
        for element in elements:
            ActionChains(driver).key_down(Keys.COMMAND).click(element).key_up(Keys.COMMAND).perform()
        curr_window = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != curr_window:
                driver.switch_to_window(handle)
                self.assertTrue(driver.find_element_by_xpath("//title"))
                driver.close()
        driver.switch_to_window(curr_window)

        myPath = "//div[@bem-id=3]"
        element = driver.find_element_by_xpath(myPath)
        element.click()
        self.assertTrue(driver.find_element_by_xpath("//title[contains(text(),'Все новости спорта')]"))

        myPath = "//span[@bem-id=407]"
        element = driver.find_element_by_xpath(myPath)
        element.click()
        myPath = "//input[@bem-id=416]"
        search = driver.find_element_by_xpath(myPath)
        search.send_keys("Ronaldo")
        search.send_keys(Keys.RETURN)
        self.assertTrue(driver.find_element_by_xpath("//title[contains(text(),'Результаты поиска')]"))

    def tearDown(self):
        self.driver.quit()
