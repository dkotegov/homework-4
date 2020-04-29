import pytest

from setup.constants import PROJECT_URL
from setup.setup import Accessor

accessor: Accessor = None


def pytest_sessionstart(session):
    global accessor
    accessor = Accessor()


def pytest_sessionfinish(session, exitstatus):
    global accessor
    accessor.shutdown()


@pytest.fixture
def test_user():
    from tests.steps.auth.steps import Steps
    Steps.open_site()
    Steps.open_auth_page()
    Steps.enter_credentials()
    Steps.login()


@pytest.fixture
def test_user_profile(test_user):
    from tests.steps.profile.steps import Steps
    Steps.open_site()
    Steps.open_edit_page()


@pytest.fixture
def test_user_restore_default():
    from tests.steps.profile.steps import Steps

    def reset():
        Steps.open_edit_page()
        Steps.open_modal()
        Steps.enter_profile_info("default", "default")
        Steps.save_profile()

    return reset


@pytest.fixture(autouse=True)
def logout():
    yield
    accessor.driver.delete_all_cookies()
