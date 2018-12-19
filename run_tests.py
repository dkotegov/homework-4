# -*- coding: utf-8 -*-
import os
import unittest
from tests.admin_users_adding_tests import AdminUsersAddingTests
from tests.admin_sources_adding_tests import AdminSourcesAddingTests
from tests.user_office_login_tests import UserOfficeLoginTests
from tests.user_office_things_taking_tests import UserOfficeThingsTakingTests
from tests.user_office_things_return_tests import UserOfficeThingsReturnTests
from tests.user_office_color_theme_tests import UserOfficeColorThemeTests

from selenium.webdriver import DesiredCapabilities, Remote
from tests.pages.admin_page import AdminPage

import sys

if __name__ == '__main__':
    browser = os.environ.get('BROWSER', 'CHROME')
    driver = Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )
    admin_page = AdminPage(driver)
    admin_page.open()
    admin_page.reset()
    driver.quit()

    suite = unittest.TestSuite((
        unittest.makeSuite(AdminUsersAddingTests),
        unittest.makeSuite(AdminSourcesAddingTests),
        unittest.makeSuite(UserOfficeLoginTests),
        unittest.makeSuite(UserOfficeThingsTakingTests),
        unittest.makeSuite(UserOfficeThingsReturnTests),
        unittest.makeSuite(UserOfficeColorThemeTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
