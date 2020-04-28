from setup.setup import Accessor

accessor: Accessor = None


def pytest_sessionstart(session):
    global accessor
    accessor = Accessor()


def pytest_sessionfinish(session, exitstatus):
    global accessor
    accessor.shutdown()
