#-*- coding: utf-8 -*-
"""App Tests"""
from __future__ import print_function

import unittest

import sch.common.app as app

class TestAppContext(unittest.TestCase):

    def test_constructor(self):
        appContext = app.AppContext('A')
        self.assertEqual( appContext.get_status(), -1 )
        self.assertEqual( str('appContext'), 'SCH' )



# -----------------

import ConfigParser

from sch.common.exceptions import ExecutionError

class xTestAppContextMethods(unittest.TestCase):

    def test_constructor(self):
        appContext = app.AppContext()
        self.assertEqual(appContext.get_status(), -1)

    def test_set_status(self):
        appContext = app.AppContext()
        appContext.set_status(21)
        self.assertEqual(appContext.get_status(), 21)

    def test_set_attribute(self):
        appContext = app.AppContext()
        config = ConfigParser.SafeConfigParser()
        config.add_section('Path')
        config.set('Path', 'code', '/opt/code')
        appContext.add_attribute('configuration', config)
        configuration = appContext.get_attribute('configuration')
        self.assertEqual(configuration.get('Path', 'code'), '/opt/code')

    def test_str(self):
        appContext = app.AppContext()
        self.assertEqual(str(appContext),'Job status is -1')


class xTestAppStepMethods(unittest.TestCase):

    def test_completion(self):
        appContext = app.AppContext()
        with appContext.new_step ('step1') as step:
           self.assertEqual( str(step), 'step1' )
           self.assertEqual( step.status, 'Started' )
        self.assertEqual( step.status, 'Completed' )


    def test_aborted(self):
        appContext = app.AppContext()
        try:
            with appContext.new_step ('step2') as step:
               self.assertEqual( str(step), 'step2' )
               raise ExecutionError(str(step), "Failure")
        except:
            self.assertEqual( step.status, 'Aborted' )



if __name__ == '__main__':
    unittest.main()
