# -*- coding: utf-8 -*-

import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('./cases')

    runner = unittest.TextTestRunner()
    runner.run(suite)
