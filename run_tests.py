#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import unittest
from src.page_object import PageObject


if __name__ == '__main__':
    page = PageObject()

    try:
        page.open('https://e.mail.ru/login/')
        page.login()
        
        page.move_all_msgs('Спам')
        time.sleep(3)

        page.go_to_spam()

        page.move_all_msgs('Входящие')
        
        time.sleep(3)

    
    finally:
        page.close()
        pass
