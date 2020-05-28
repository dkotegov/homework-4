import re
import time

from selenium.common.exceptions import TimeoutException

from tests.cases.base import TestAuthorized
from tests.pages.pin import PinDetailsPage
from tests.pages.search_global import GlobalSearchPage


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = GlobalSearchPage(self.driver, False)

    def test_search_explicit(self):
        query = "BridgeTM"
        type = "Username"

        self.page.search_form.search(type, query)
        results = self.page.result_form.get_search_results()

        for result in results:
            if result.lower() == query.lower():
                return
        self.assertTrue(False, "cannot find username in results")

    def test_search_partial(self):
        query = "bri"
        target = "BridgeTM"
        type = "Username"
        self.page.search_form.search(type, query)
        results = self.page.result_form.get_search_results()

        for result in results:
            if result.lower() == target.lower():
                return
        self.assertTrue(False, "cannot find username in results")

    def test_search_empty(self):
        query = ""
        type = "Username"
        self.page.search_form.search(type, query)

        try:
            self.page.result_form.wait_for_load(timeout=3)
            self.assertFalse(True, "It seems site searches an empty value")
        except TimeoutException:
            return

    def test_search_tag_existed(self):
        tag = "vscode"
        # tag = 'hohoho'
        type = "Tag"

        self.page.search_form.search(type, tag)

        def validate():
            page = PinDetailsPage(self.driver, open=False)
            tag_got = page.form.get_tag()
            self.assertTrue(
                re.match(".*" + tag.lower() + ".*", tag_got.lower()),
                "Tags does not equals",
            )

        self.page.result_form.check_search_results(validate)

    def test_search_user_inexistant(self):
        query = "qowjdwiqdowendwnedq9d32"
        type = "Username"
        self.page.search_form.search(type, query)
        self.assertTrue(self.page.result_form.wait_for_error(), "No error block")

    def test_search_tag_inexistant(self):
        query = "qowjdwiqdowendwnedq9d32"
        type = "Tag"
        self.page.search_form.search(type, query)
        self.assertTrue(self.page.result_form.wait_for_error(), "No error block")
