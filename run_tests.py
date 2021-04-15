import unittest
import sys
from tests.profile.check_auth import CheckAuth
from tests.main.check_main import CheckMain
from tests.search.check_search import CheckSearch
from tests.content.check_content import CheckContent
from tests.film_popup.check_serial_popup import CheckSerialPopup
from tests.film_popup.check_film_popup import CheckFilmPopup
from tests.infoblock_film.check_infoblock import CheckInfoblock
from tests.my_list.check_my_list import CheckMyList
from tests.player.check_player import CheckPlayer
from tests.profile.check_regist import CheckRegist
from tests.profile.check_settings_change import CheckSettingsChange


if __name__ == '__main__':
    suite = unittest.TestSuite((
       unittest.makeSuite(CheckAuth),
       unittest.makeSuite(CheckMain),
       unittest.makeSuite(CheckSearch),
       unittest.makeSuite(CheckContent),
       unittest.makeSuite(CheckSerialPopup),
       unittest.makeSuite(CheckFilmPopup),
       unittest.makeSuite(CheckInfoblock),
       unittest.makeSuite(CheckMyList),
       unittest.makeSuite(CheckPlayer),
       unittest.makeSuite(CheckRegist),
       unittest.makeSuite(CheckSettingsChange),
    ))
    result = unittest.TextTestRunner().run(suite)

    sys.exit(not result.wasSuccessful())
