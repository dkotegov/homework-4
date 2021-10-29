import sys
import unittest
from cases.create_new_file import CreateNewFileTests
from cases.create_new_folder_popup import CreateNewFolderPopupTests
from cases.hover_over_file import HoverOverFileTests
from cases.file_dropdown_menu import FileDropDownMenuTests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CreateNewFileTests),
        unittest.makeSuite(CreateNewFolderPopupTests),
        unittest.makeSuite(HoverOverFileTests),
        unittest.makeSuite(FileDropDownMenuTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
