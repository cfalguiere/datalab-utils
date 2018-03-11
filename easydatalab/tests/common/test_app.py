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


class TestAppStep(unittest.TestCase):

    def test_constructor(self):
        appContext = app.AppContext('APP')
        appStep = app.AppStep('STEP1', appContext)
        self.assertEqual( appStep.get_status(), 'Not Started' )
        self.assertEqual( str(appStep), 'STEP1' )

    def test_enter(self):
        appContext = app.AppContext('APP')
        appStep = app.AppStep('STEP1', appContext)
        appStep.__enter__()
        self.assertEqual( appStep.get_status(), 'Started' )

