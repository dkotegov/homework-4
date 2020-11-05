#!/usr/bin/env python3

# import sys
import unittest

from nikita.tests.virusmusic.profile.settings.small_avatar_load_test import SmallAvatarLoadTest
from nikita.tests.virusmusic.profile.settings.big_avatar_load_test import BigAvatarLoadTest
from nikita.tests.virusmusic.profile.settings.pdf_avatar_load_test import PdfAvatarLoadTest

from nikita.tests.virusmusic.profile.settings.valid_name_change_test import ValidNameChangeTest
from nikita.tests.virusmusic.profile.settings.empty_name_change_test import EmptyNameChangeTest

from nikita.tests.virusmusic.profile.settings.valid_email_change_test import ValidEmailChangeTest
from nikita.tests.virusmusic.profile.settings.invalid_email_change_test import InvalidEmailChangeTest
from nikita.tests.virusmusic.profile.settings.empty_email_change_test import EmptyEmailChangeTest

from nikita.tests.virusmusic.profile.settings.no_old_password_change_test import NoOldPasswordChangeTest
from nikita.tests.virusmusic.profile.settings.wrong_old_password_change_test import WrongOldPasswordChangeTest
from nikita.tests.virusmusic.profile.settings.mismatch_password_change_test import MismatchPasswordChangeTest
from nikita.tests.virusmusic.profile.settings.length_password_change_test import LengthPasswordChangeTest
from nikita.tests.virusmusic.profile.settings.cyrillic_password_change_test import CyrillicPasswordChangeTest
from nikita.tests.virusmusic.profile.settings.valid_password_change_test import ValidPasswordChangeTest

from nikita.tests.virusmusic.profile.settings.theme_change_test import ThemeChangeTest
from nikita.tests.virusmusic.profile.settings.language_change_test import LanguageChangeTest

from nikita.tests.virusmusic.profile.playlists.playlist_creation_test import PlaylistCreationTest
from nikita.tests.virusmusic.profile.playlists.playlist_with_empty_name_creation_test import PlaylistWithEmptyNameCreationTest
from nikita.tests.virusmusic.profile.playlists.playlist_delete_test import PlaylistDeleteTest as ProfilePlaylistDeleteTest
from nikita.tests.virusmusic.profile.playlists.playlist_name_change_test import PlaylistNameChangeTest as ProfilePlaylistNameChangeTest

from nikita.tests.virusmusic.profile.playlists.small_playlist_image_load_test import SmallPlaylistImageLoadTest as ProfileSmallPlaylistImageLoadTest
from nikita.tests.virusmusic.profile.playlists.big_playlist_image_load_test import BigPlaylistImageLoadTest as ProfileBigPlaylistImageLoadTest
from nikita.tests.virusmusic.profile.playlists.pdf_playlist_image_load_test import PdfPlaylistImageLoadTest as ProfilePdfPlaylistImageLoadTest

# настройка приватности + доступ
# один аккаунт делает два плейлиста: приватный и публичный, другой пробует получить доступ
# from nikita.tests.public_playlist_access_test import PublicPlaylistAccessTest
# from nikita.tests.private_playlist_access_test import PrivatePlaylistAccessTest

from nikita.tests.virusmusic.playlist.playlist_delete_test import PlaylistDeleteTest
from nikita.tests.virusmusic.playlist.small_playlist_image_load_test import SmallPlaylistImageLoadTest
from nikita.tests.virusmusic.playlist.playlist_name_change_test import PlaylistNameChangeTest
from nikita.tests.virusmusic.playlist.playlist_empty_name_change_test import PlaylistEmptyNameChangeTest
from nikita.tests.virusmusic.playlist.playlist_copy_link_test import PlaylistCopyLinkTest
from nikita.tests.virusmusic.playlist.playlist_vk_share_test import PlaylistVkShareTest

from nikita.tests.todo.list_creation.list_creation_test import ListCreationTest
from nikita.tests.todo.list_creation.list_empty_name_creation_test import ListEmptyNameCreationTest
from nikita.tests.todo.list_creation.list_long_name_creation_test import ListLongNameCreationTest
from nikita.tests.todo.list_creation.list_spaces_name_creation_test import ListSpacesNameCreationTest
from nikita.tests.todo.list_creation.list_xss_name_creation_test import ListXssNameCreationTest

from nikita.tests.todo.list_deletion.list_deletion_left_menu_test import ListDeletionLeftMenuTest
from nikita.tests.todo.list_deletion.list_deletion_test import ListDeletionTest

from nikita.tests.todo.list_change.general.list_name_change_test import ListNameChangeTest
from nikita.tests.todo.list_change.general.list_empty_name_change_test import ListEmptyNameChangeTest
from nikita.tests.todo.list_change.general.list_long_name_change_test import ListLongNameChangeTest
from nikita.tests.todo.list_change.general.list_spaces_name_change_test import ListSpacesNameChangeTest

from nikita.tests.todo.list_change.general.list_description_change_test import ListDescriptionChangeTest
from nikita.tests.todo.list_change.general.list_long_description_change_test import ListLongDescriptionChangeTest
from nikita.tests.todo.list_change.general.list_space_description_change_test import ListSpaceDescriptionChangeTest

from nikita.tests.todo.list_change.general.list_color_change_test import ListColorChangeTest

from nikita.tests.todo.list_change.modal.list_name_change_test import ListNameChangeTest as ListNameModalChangeTest
from nikita.tests.todo.list_change.modal.list_empty_name_change_test import ListEmptyNameChangeTest as ListEmptyNameModalChangeTest
from nikita.tests.todo.list_change.modal.list_long_name_change_test import ListLongNameChangeTest as ListLongNameModalChangeTest
from nikita.tests.todo.list_change.modal.list_spaces_name_change_test import ListSpacesNameChangeTest as ListSpacesNameModalChangeTest

from nikita.tests.todo.list_change.modal.list_description_change_test import ListDescriptionChangeTest as ListDescriptionModalChangeTest
from nikita.tests.todo.list_change.modal.list_long_description_change_test import ListLongDescriptionChangeTest as ListLongDescriptionModalChangeTest
from nikita.tests.todo.list_change.modal.list_space_description_change_test import ListSpaceDescriptionChangeTest as ListSpaceDescriptionModalChangeTest

from nikita.tests.todo.list_change.modal.list_color_change_test import ListColorChangeTest as ListColorModalChangeTest

from nikita.tests.todo.list_change.modal.cancel_test import ListCancelChangeTest

def run_tests():
    settingsSuite = unittest.TestSuite((
        unittest.makeSuite(SmallAvatarLoadTest),
        unittest.makeSuite(BigAvatarLoadTest),
        unittest.makeSuite(PdfAvatarLoadTest),
        unittest.makeSuite(ValidNameChangeTest),
        unittest.makeSuite(EmptyNameChangeTest),
        unittest.makeSuite(ValidEmailChangeTest),
        unittest.makeSuite(InvalidEmailChangeTest),
        unittest.makeSuite(EmptyEmailChangeTest),
        unittest.makeSuite(NoOldPasswordChangeTest),
        unittest.makeSuite(WrongOldPasswordChangeTest),
        unittest.makeSuite(MismatchPasswordChangeTest),
        unittest.makeSuite(LengthPasswordChangeTest),
        unittest.makeSuite(CyrillicPasswordChangeTest),
        unittest.makeSuite(ValidPasswordChangeTest),
        unittest.makeSuite(ThemeChangeTest),
        unittest.makeSuite(LanguageChangeTest),
    ))
    unittest.TextTestRunner().run(settingsSuite)
    # settingsResult = unittest.TextTestRunner().run(settingsSuite)
    # sys.exit(not settingsResult.wasSuccessful())
    profilePlaylistsSuite = unittest.TestSuite((
        unittest.makeSuite(PlaylistCreationTest),
        unittest.makeSuite(ProfilePlaylistDeleteTest),
        unittest.makeSuite(PlaylistWithEmptyNameCreationTest),
        unittest.makeSuite(ProfilePlaylistNameChangeTest),
        unittest.makeSuite(ProfileSmallPlaylistImageLoadTest),
        unittest.makeSuite(ProfileBigPlaylistImageLoadTest),
        unittest.makeSuite(ProfilePdfPlaylistImageLoadTest),
    ))
    unittest.TextTestRunner().run(profilePlaylistsSuite)
    # profileplaylistsResult = unittest.TextTestRunner().run(profilePlaylistsSuite)
    # sys.exit(not profileplaylistsResult.wasSuccessful())
    playlistSuite = unittest.TestSuite((
        unittest.makeSuite(PlaylistDeleteTest),
        unittest.makeSuite(PlaylistNameChangeTest),
        unittest.makeSuite(PlaylistEmptyNameChangeTest),
        unittest.makeSuite(SmallPlaylistImageLoadTest),
        unittest.makeSuite(PlaylistCopyLinkTest),
        unittest.makeSuite(PlaylistVkShareTest),
    ))
    unittest.TextTestRunner().run(playlistSuite)
    # playlistResult = unittest.TextTestRunner().run(playlistSuite)
    # sys.exit(not playlistsResult.wasSuccessful())

    listCreationDeletionSuite = unittest.TestSuite((
        unittest.makeSuite(ListCreationTest),
        unittest.makeSuite(ListEmptyNameCreationTest),
        unittest.makeSuite(ListLongNameCreationTest),
        unittest.makeSuite(ListSpacesNameCreationTest),
        unittest.makeSuite(ListXssNameCreationTest),
        unittest.makeSuite(ListDeletionLeftMenuTest),
        unittest.makeSuite(ListDeletionTest),
    ))
    unittest.TextTestRunner().run(listCreationDeletionSuite)
    # listCreationDeletionResult = unittest.TextTestRunner().run(listCreationDeletionSuite)
    # sys.exit(not listCreationDeletionResult.wasSuccessful())
    listChangeSuite = unittest.TestSuite((
        unittest.makeSuite(ListNameChangeTest),
        unittest.makeSuite(ListEmptyNameChangeTest),
        unittest.makeSuite(ListLongNameChangeTest),
        unittest.makeSuite(ListSpacesNameChangeTest),
        unittest.makeSuite(ListDescriptionChangeTest),
        unittest.makeSuite(ListLongDescriptionChangeTest),
        unittest.makeSuite(ListSpaceDescriptionChangeTest),
        unittest.makeSuite(ListColorChangeTest),
    ))
    unittest.TextTestRunner().run(listChangeSuite)
    # listChangeResult = unittest.TextTestRunner().run(listChangeSuite)
    # sys.exit(not listChangeResult.wasSuccessful())
    listModalChangeSuite = unittest.TestSuite((
        unittest.makeSuite(ListNameModalChangeTest),
        unittest.makeSuite(ListEmptyNameModalChangeTest),
        unittest.makeSuite(ListLongNameModalChangeTest),
        unittest.makeSuite(ListSpacesNameModalChangeTest),
        unittest.makeSuite(ListDescriptionModalChangeTest),
        unittest.makeSuite(ListLongDescriptionModalChangeTest),
        unittest.makeSuite(ListSpaceDescriptionModalChangeTest),
        unittest.makeSuite(ListColorModalChangeTest),
        unittest.makeSuite(ListCancelChangeTest),
    ))
    unittest.TextTestRunner().run(listModalChangeSuite)
    # listModalChangeResult = unittest.TextTestRunner().run(listModalChangeSuite)
    # sys.exit(not listModalChangeResult.wasSuccessful())
