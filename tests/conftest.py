import os

import pytest

from setup.setup import Accessor

accessor: Accessor = None


def pytest_sessionstart(session):
    global accessor
    accessor = Accessor()


def pytest_sessionfinish(session, exitstatus):
    global accessor
    accessor.shutdown()


@pytest.fixture
def user():
    from tests.steps.auth.steps import Steps
    Steps.open_site()
    Steps.open_auth_page()
    Steps.enter_credentials()
    Steps.login()


def open_user_profile():
    from tests.steps.profile.steps import Steps
    Steps.open_site()
    Steps.open_edit_page()


def unsubscribe(actor_id):
    from tests.steps.subscription.steps import Steps
    Steps.unsubscribe(actor_id)


@pytest.fixture
def user_profile(user):
    open_user_profile()


@pytest.fixture
def user_restore_default():
    from tests.steps.profile.steps import Steps
    yield
    Steps.open_edit_page()
    Steps.open_modal()
    Steps.enter_profile_info("default", "default")
    Steps.upload_avatar(f'{os.getcwd()}/../../test_data/default.png')
    Steps.save_profile()


@pytest.fixture(autouse=True)
def logout():
    yield
    accessor.driver.delete_all_cookies()


def create_review():
    from tests.steps.review.steps import Steps
    Steps.get_film(1)
    Steps.enter_review_text('review title', 'review body')
    Steps.submit_review()


@pytest.fixture
def user_review(user):
    create_review()
