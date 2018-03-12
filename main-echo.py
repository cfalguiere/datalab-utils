#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Run Score Credit Habitat"""
from __future__ import print_function

import sys
from easydatalab.common.app import AppContext
from easydatalab.r.rutils import RScript

def main():
    """Main entry point for the script."""

    cfgFile = 'easydatalab/tests/resources/config_for_r_unittests.cfg'

    with AppContext() as appContext:
        with appContext.new_configuration(cfgFile) as appConfiguration:
            appConfiguration.show()
            appConfiguration.add_parameter('d1', 'val_d1')
            with appContext.new_step('echo') as step:
                with step.subprocess(RScript) as r:
                    requiredParams = [ 'd1' ]
                    r.call( 'echo.r',  requiredParams )



if __name__ == '__main__':
    sys.exit(main())
