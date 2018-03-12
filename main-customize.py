#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Run Score Credit Habitat"""
from __future__ import print_function

import sys
from easydatalab.common.app import AppContext
from easydatalab.r.rutils import RScript

def customize_fun(configuration):
    print( "customize" )
    add = configuration.add_parameter
    get = configuration.get_parameter
    add('start', get('PERIOD:start'))

def main():
    """Main entry point for the script."""

    cfgFile = 'easydatalab/tests/resources/config_for_r_unittests.cfg'

    with AppContext() as appContext:
        with appContext.new_configuration(cfgFile) as appConfiguration:
            appConfiguration.customize(customize_fun)
            appConfiguration.add_parameter('d1', 'val_d1')
            with appContext.new_step('echo') as step:
                with step.subprocess(RScript) as r:
                    requiredParams = [ 'd1', 'start' ]
                    r.call( 'echo.R',  requiredParams )



if __name__ == '__main__':
    sys.exit(main())
