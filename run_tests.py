# -*- coding: utf-8 -*-

import unittest

from tests.edit_job_test import EditJobTest
from tests.job_list_manage_test import JobListManageTest
from tests.job_manage_test import JobManageTest
from tests.login_test import LoginTest
from tests.create_job_test import CreateJobTest
import sys


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(CreateJobTest),
        unittest.makeSuite(EditJobTest),
        unittest.makeSuite(JobManageTest),
        unittest.makeSuite(JobListManageTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
