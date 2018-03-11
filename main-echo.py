#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Run Score Credit Habitat"""
from __future__ import print_function

import sys
from sch.common.app import AppContext

def main():
    """Main entry point for the script."""

    cfgFile = 'sch/mocks/app-for-unittests.cfg'

    with AppContext() as appContext:
        with appContext.new_configuration(cfgFile) as appConfiguration:

            with appContext.new_step ('echo') as step:
                with step.rscript() as r:
                    requiredParams = [ 'pathToData', 'pathToRawData', 'pathToLog' ]
                    r.call( 'echo.R',  requiredParams )

                with step.rscript() as r:
                    requiredParams = [ 'pathToData', 'pathToRawData', 'pathToLog' ]
                    r.call( 'echo.R',  requiredParams )

            with appContext.new_step ('echo') as step:
                with step.rscript() as r:
                    requiredParams = [ 'pathToData', 'pathToRawData', 'pathToLog' ]
                    r.call( 'echo.R',  requiredParams )

                with step.rscript() as r:
                    requiredParams = [ 'pathToData', 'pathToRawData', 'pathToLog' ]
                    r.call( 'echo.R',  requiredParams )



if __name__ == '__main__':
    sys.exit(main())
