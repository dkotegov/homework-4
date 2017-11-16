import unittest

from es_check_list.all_marks_test import TestAllMarkValues
from es_check_list.self_mark_test import TestSelfMark
from es_check_list.check_marks_test import TestCheckMarks
from es_check_list.remove_mark_test import TestRemoveMark

tests = (
    # unittest.makeSuite(TestAllMarkValues),
    # unittest.makeSuite(TestSelfMark),
    # unittest.makeSuite(TestCheckMarks)
    unittest.makeSuite(TestRemoveMark)
)