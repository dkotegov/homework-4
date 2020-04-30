import re
from tests.cases.base import TestAuthorized
from tests.pages.pin import PinDetailsPage
from tests.pages.search_global import GlobalSearchPage


class Test(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = GlobalSearchPage(self.driver, False)

    def test_search_explicit(self):
        query = 'BridgeTM'
        type = 'Username'

        self._perform_search(type, query)
        results = self.page.result_form.get_search_results()

        for result in results:
            if result.lower() == query.lower():
                return
        assert False, "cannot find username in results"

    def test_search_partial(self):
        query = 'bri'
        target  = 'BridgeTM'
        type = 'Username'
        self._perform_search(type, query)
        results = self.page.result_form.get_search_results()

        for result in results:
            if result.lower() == target.lower():
                return
        assert False, "cannot find username in results"

    def test_search_empty(self):
        query = ''
        type = 'Username'
        self.page.search_form.wait_for_load()
        self.page.search_form.search(type, query)

        try:
            self.page.result_form.wait_for_load(timeout=3)
        except:
            return
        assert False, "It seems site searches an empty value"

    def test_search_tag_existed(self):
        # tag = 'vscode'
        tag = 'hohoho'
        type = 'Tag'

        self._perform_search(type, tag)

        results = self.page.result_form.get_search_results_raw()

        for i in range(len(results)):
            self.page.result_form.wait_for_load()
            s = self.page.result_form.get_search_results_raw()
            if len(s) <= i:
                continue
            result = s[i]
            self.page.result_form.click_pin(result)
            page = PinDetailsPage(self.driver, open=False)
            page.form.wait_for_load()
            tag_got = page.form.get_tag()

            assert re.match('.*' + tag.lower() + '.*', tag_got.lower())
            self.driver.back()
            self.driver.refresh()

    def test_search_user_inexistant(self):
        query = 'qowjdwiqdowendwnedq9d32'
        type = 'Username'
        self._perform_search(type, query)
        assert self.page.result_form.wait_for_error(), 'No error block'

    def test_search_tag_inexistant(self):
        query = 'qowjdwiqdowendwnedq9d32'
        type = 'Tag'
        self._perform_search(type, query)
        assert self.page.result_form.wait_for_error(), 'No error block'

    def _perform_search(self, type, query):
        self.page.search_form.wait_for_load()
        self.page.search_form.search(type, query)

        self.page.result_form.wait_for_load()


