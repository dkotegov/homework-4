# -*- coding: utf-8 -*-

import unittest
from tests import ProductTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ProductTest)
    ))
    unittest.TextTestRunner().run(suite)

#driver = webdriver.Chrome('/Users/ivangorshkov/chromedriver')
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#time.sleep(5)
#driver.close()
