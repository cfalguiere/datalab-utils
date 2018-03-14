#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Run Score Credit Habitat"""
from __future__ import print_function

import sys
from easydatalab.common.app import AppContext

def main():
    """Main entry point for the script."""

    cfgFileEnv = 'easydatalab/resources/env.cfg'
    cfgFileApp = 'easydatalab/resources/app.cfg'


    with AppContext() as appContext:
        with appContext.new_configuration( [cfgFileEnv, cfgFileApp] ) as appConfiguration:
            appConfiguration.show()

            with appContext.new_step ('something') as step:
                 print(appConfiguration.get_parameter("PATH:rcode"))

            with appContext.new_step ('something else') as step:
                 print(appConfiguration.get_parameter("MODULE:module1"))


if __name__ == '__main__':
    sys.exit(main())
