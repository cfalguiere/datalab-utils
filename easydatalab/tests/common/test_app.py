#-*- coding: utf-8 -*-
"""App Tests"""
from __future__ import print_function

import unittest

import easydatalab.common.app as app
from easydatalab.common.exceptions import ExecutionError

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

    def test_assert_input_file(self):
        appContext = app.AppContext('APP')
        appStep = app.AppStep('STEP1', appContext)
        appStep.__enter__()
        appStep.assert_input_file('easydatalab/tests/resources/data/fileAB.csv')

    def test_assert_input_file_no_match(self):
        appContext = app.AppContext('APP')
        appStep = app.AppStep('STEP1', appContext)
        appStep.__enter__()
        with self.assertRaises(ExecutionError) as ctx:
             filePath = 'easydatalab/tests/resources/data/does_not_exists.csv'
             appStep.assert_input_file(filePath)
             self.assertTrue('ExecutionError' in ctx.exception)

    def test_assert_input_file_wildcard(self):
        appContext = app.AppContext('APP')
        appStep = app.AppStep('STEP1', appContext)
        appStep.__enter__()
        appStep.assert_input_file('easydatalab/tests/resources/data/file*.csv')

    def test_assert_input_file_wildcard_no_match(self):
        appContext = app.AppContext('APP')
        appStep = app.AppStep('STEP1', appContext)
        appStep.__enter__()
        with self.assertRaises(ExecutionError) as ctx:
             filePath = 'easydatalab/tests/resources/data/does_not_*_exists.csv'
             appStep.assert_input_file(filePath)
             self.assertTrue('ExecutionError' in ctx.exception)

