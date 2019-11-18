from selenium import webdriver
import os

if __name__ == '__main__':
    browserName = os.environ['BROWSER']
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={
            "browserName": browserName,
        }
    )
    driver.get("http://park.mail.ru/")
    driver.quit()
