# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.auth import AuthPage
from pages.create_repo import CreateRepoPage
from pages.list_repos import ListRepoPage
from pages.remove_repo import RemoveRepoPage
from pages.main import MainPage
from pages.show_repo import ShowRepoPage
from pages.wiki import WikiPage


class GitTest(unittest.TestCase):
    USERNAME = unicode(os.environ['USERNAME'], 'utf-8')
    PASSWORD = unicode(os.environ['PASSWORD'], 'utf-8')
    REPONAME = 'testrepo'
    NEW_REPONAME = 'testreponew'
    REPO_GITIGNORE = 'gitignorerepo'
    WIKI_TITLE = 'Wiki_title'
    WIKI_TEXT = 'Wiki text'
    WIKI_TITLE_NEW = 'Wiki_title_new'
    WIKI_TEXT_NEW = 'Wiki text new'
    GITIGNORE = '.gitignore'

    created_topic = None

    def setUp(self):
        # browser = os.environ.get('BROWSER', 'FIREFOX')
        browser = os.environ.get('BROWSER', 'CHROME')

        # Create a desired capabilities object as a starting point.
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['platform'] = "ANY"
        capabilities['version'] = ""

        self.driver = Remote(
            command_executor='http://172.20.10.2:5555/wd/hub',
            desired_capabilities=capabilities
        )
        auth_page = AuthPage(self.driver)
        auth_page.sign_in(self.USERNAME, self.PASSWORD)
        main_page = MainPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_01_create_repo(self):
        create_page = CreateRepoPage(self.driver)
        create_page.navigate()
        self.created_repo = create_page \
            .set_repo_name(self.REPONAME) \
            .create(self.REPONAME)

        list_repo_page = ListRepoPage(self.driver)
        list_repo_page.navigate()
        self.assertEqual(True, list_repo_page.check_repo_exist(self.REPONAME))

    def test_02_rename_repo(self):
        remove_page = RemoveRepoPage(self.driver, self.USERNAME, self.REPONAME)
        remove_page.navigate()
        remove_page.rename_repo(self.NEW_REPONAME)
        remove_page.submit_rename()

        list_repo_page = ListRepoPage(self.driver)
        list_repo_page.navigate()
        self.assertEqual(True, list_repo_page.check_repo_exist(self.NEW_REPONAME))

    def test_03_create_wiki(self):
        wiki_page = WikiPage(self.driver, self.USERNAME, self.REPONAME, '')
        wiki_page.navigate()

        wiki_page.create_wiki()
        wiki_page.set_title(self.WIKI_TITLE)
        wiki_page.set_text(self.WIKI_TEXT)
        self.assertEqual(True, wiki_page.submit_create(self.WIKI_TITLE))

    def test_04_edit_wiki(self):
        wiki_page = WikiPage(self.driver, self.USERNAME, self.REPONAME, self.WIKI_TITLE)
        wiki_page.navigate()

        self.assertEqual(True, wiki_page.edit_wiki(self.WIKI_TITLE_NEW, self.WIKI_TEXT_NEW))

    def test_05_delete_wiki(self):
        wiki_page = WikiPage(self.driver, self.USERNAME, self.REPONAME, self.WIKI_TITLE_NEW)
        wiki_page.navigate()

        self.assertEqual(True, wiki_page.delete_wiki(self.WIKI_TITLE_NEW))

    def test_06_create_repo_with_gitignore(self):
        create_page = CreateRepoPage(self.driver)
        create_page.navigate()
        self.created_repo = create_page \
            .set_repo_name(self.REPO_GITIGNORE) \
            .add_gitignore() \
            .create(self.REPO_GITIGNORE)

        list_repo_page = ListRepoPage(self.driver)
        list_repo_page.navigate()
        self.assertEqual(True, list_repo_page.check_repo_exist(self.REPO_GITIGNORE))

        repo_page = ShowRepoPage(self.driver, self.REPO_GITIGNORE)
        repo_page.navigate()
        self.assertEqual(self.GITIGNORE, repo_page.get_repo_gitignore())

    def test_07_delete_repo(self):
        remove_page = RemoveRepoPage(self.driver, self.USERNAME, self.REPO_GITIGNORE)
        remove_page.navigate()
        remove_page.submit_remove(self.REPO_GITIGNORE)

        list_repo_page = ListRepoPage(self.driver)
        list_repo_page.navigate()
        self.assertEqual(True, list_repo_page.check_repo_exist(self.REPO_GITIGNORE))
