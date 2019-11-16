import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote
from pages.auth_page import AuthPage

class UserinfoTest(unittest.TestCase):
    USERNAME = u'Дмитрий Котегов'
    USEREMAIL = 'kotegov_dima@mail.ru'
    PASSWORD = os.environ['PASSWORD']
    BLOG = 'Флудилка'
    TITLE = u'ЗаГоЛоВоК'
    MAIN_TEXT = u'Текст под катом! Отображается внутри топика!'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.authorize()

        # user_name = auth_page.top_menu.get_username()
        # self.assertEqual(self.USERNAME, user_name)

        # create_page = CreatePage(self.driver)
        # create_page.open()

        # create_form = create_page.form
        # create_form.blog_select_open()
        # create_form.blog_select_set_option(self.BLOG)
        # create_form.set_title(self.TITLE)
        # create_form.set_main_text(self.MAIN_TEXT)
        # create_form.set_unpublish()
        # create_form.submit()

        # topic_page = TopicPage(self.driver)
        # topic_title = topic_page.topic.get_title()
        # topic_text = topic_page.topic.get_text()
        # self.assertEqual(self.TITLE, topic_title)
        # self.assertEqual(self.MAIN_TEXT, topic_text)

        # blog_page = BlogPage(self.driver)
        # blog_page.topic.delete()
        # topic_title = blog_page.topic.get_title()
        # topic_text = blog_page.topic.get_text()
        # self.assertNotEqual(self.TITLE, topic_title)
        # self.assertNotEqual(self.MAIN_TEXT, topic_text)