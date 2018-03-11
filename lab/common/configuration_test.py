#-*- coding: utf-8 -*-
from __future__ import print_function

import unittest

from lab.common.configuration import AppConfiguration

class TestAppConfiguration(unittest.TestCase):

    def test_constructor(self):
        cfgFile = 'sch/mocks/app-for-unittests.cfg'
        appConfiguration = AppConfiguration(cfgFile)
        self.assertEqual( repr(appConfiguration), 'AppConfiguration: from=sch/mocks/app-for-unittests.cfg' )
