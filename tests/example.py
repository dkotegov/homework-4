#!/usr/bin/python

import time
import unittest
# import src.page_object
import sys
print sys.path

if __name__ == '__main__':

    try:
        page = src.page_object.PageObject('https://e.mail.ru/login/')
        page.login()
        page.move_n_msgs(2)
        time.sleep(3)
        
    
    finally:
        # driver.close()
        pass
