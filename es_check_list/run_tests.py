import unittest

from es_check_list.set_marks_test import AllMarkValuesTest, SelfMarkTest, UpdateMarkTest
from es_check_list.remove_marks_test import RemoveMarkTest, CancelRemoveMarkTest, SetNewMarkTest
from es_check_list.events_modal_test import HasNewEventTest, CheckMarksEventTest, RemoveMarkEventTest, \
    CancelRemoveMarkEventTest


def es_tests():
    return [
        unittest.makeSuite(AllMarkValuesTest),
        unittest.makeSuite(SelfMarkTest),
        unittest.makeSuite(UpdateMarkTest),
        unittest.makeSuite(RemoveMarkTest),
        unittest.makeSuite(CancelRemoveMarkTest),
        unittest.makeSuite(SetNewMarkTest),
        unittest.makeSuite(HasNewEventTest),
        unittest.makeSuite(CheckMarksEventTest),
        unittest.makeSuite(RemoveMarkEventTest),
        unittest.makeSuite(CancelRemoveMarkEventTest),
    ]
