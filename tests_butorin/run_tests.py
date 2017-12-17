import unittest


from photos_test import UploadPhotoTest, \
    OpenPhotoTest, \
    MakeMainPhotoTest, \
    ClosePhotoOverlayTest, \
    ClosePhotoButtonTest, \
    DeletePhotoTest, \
    RestorePhotoTest, \
    AddDescriptionTest, \
    ShowLinkTest, \
    AddCommentTest


tests_butorin = [
    # photo_tests
    UploadPhotoTest,
    OpenPhotoTest,
    MakeMainPhotoTest,
    ClosePhotoOverlayTest,
    ClosePhotoButtonTest,
    DeletePhotoTest,
    RestorePhotoTest,
    AddDescriptionTest,
    ShowLinkTest,
    AddCommentTest,
]

run_tests_butorin = list(map(
    lambda test:
        unittest.TestSuite((
            unittest.makeSuite(test),
        )),
    tests_butorin
))
