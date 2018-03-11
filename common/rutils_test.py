#-*- coding: utf-8 -*-
"""R Utils Tests"""

import unittest
import ConfigParser

from sch.common.rutils import RWrapper
from sch.common.app import AppContext
from sch.common.exceptions import ExecutionError

class TestRWrapperMethods(unittest.TestCase):

    def test_call(self):
        appContext = AppContext()

        config = ConfigParser.SafeConfigParser()
        config.read('sch/mocks/app-for-unittests.cfg')
        appContext.add_attribute('configuration', config)

        argsList = [ 'pathToCode='+config.get('PATH', 'rscript'), 'varId=VAR_ID', 'minDate=MIN_DATE' ]
        r = RWrapper( appContext, config.get('PATH', 'rscript'))
        r.call( 'Echo', 'sch/mocks/echo.R',  argsList )

    def test_call_wrong_path(self):
        appContext = AppContext()

        config = ConfigParser.SafeConfigParser()
        config.read('sch/mocks/app-for-unittests.cfg')
        appContext.add_attribute('configuration', config)

        argsList = [ 'pathToCode='+config.get('PATH', 'rscript'), 'varId=VAR_ID', 'minDate=MIN_DATE' ]
        r = RWrapper( appContext, config.get('PATH', 'rscript'))
        r.call( 'Echo', 'sch/mocks/doesnotexists.R',  argsList )
        with self.assertRaises(ExecutionError) as ctx:
            self.assertEqual('ExecutionError: error in step Echo - R program not found at ' + config.get('PATH', 'rscript') + 'sch/mocks/doesnotexists.R')


if __name__ == '__main__':
    unittest.main()
