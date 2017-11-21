# -*- coding: utf-8 -*-

from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome('./drivers/chromedriver_linux_64')
    # driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get("http://park.mail.ru/")
    driver.quit()
