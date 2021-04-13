#!/usr/bin/env python3

import sys
import unittest
from cases.auth_case import AuthTest
from cases.profile_case import ProfileTest
from cases.meetings_case import MeetingsTest
from cases.people_case import PeopleTest
from cases.meeting_case import MeetingTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            unittest.makeSuite(AuthTest),
            unittest.makeSuite(PeopleTest),
            # unittest.makeSuite(ProfileTest),
            unittest.makeSuite(MeetingsTest),
            unittest.makeSuite(MeetingTest),
        )
    )

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
