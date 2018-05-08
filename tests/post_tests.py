# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopForumPage
from tests.common import getDriver, Auth, Shop, Main


class PostTests(unittest.TestCase):
    SHOP_NAME = u'Магазин'

    def setUp(self):
        self.driver = getDriver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()

        shop = Shop(self.driver)
        shop.create(self.SHOP_NAME)
        shop.open_forum_page()

    def tearDown(self):
        # TODO Element <a ...> is not clickable
        import time; time.sleep(1)

        Shop(self.driver).remove()
        self.driver.quit()

    def test_create_delete_theme(self):
        shop_forum_page = ShopForumPage(self.driver)
        topic_popup = shop_forum_page.topic_popup
        topic_popup.open_popup()
        topic_popup.set_text()
        topic_popup.submit()
