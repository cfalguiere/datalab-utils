#-*- coding: utf-8 -*-
"""App Tests"""
from __future__ import print_function

import unittest

import easydatalab.common.app as app

class TestAppContext(unittest.TestCase):

    def test_constructor(self):
        appContext = app.AppContext('APP')
        self.assertEqual( appContext.get_status(), -1 )
        self.assertEqual( str(appContext), 'APP' )

