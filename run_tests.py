# -*- coding: utf-8 -*-

import sys
import unittest
import tests

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(tests.TestPlan),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

    # os.environ["LOGIN"] = "bikemaster2000@list.ru.local"
    # os.environ["PASSWORD"] = "park3791"
    # driver = webdriver.Safari()
    # driver.get("http://ftest.tech-mail.ru/pages/index/")
    #
    # login_page = Pages.LoginPage(driver)
    # login_page.open()
    # main_page = login_page.login("bikemaster2000@list.ru.local", "park3791")
    # post_page = main_page.get_post()
    # post_page.check_last_comment()
    #
    # driver.quit()
